import pickle
from pathlib import Path
from typing import Optional

import pika
import requests
import yaml

from src.logs.abstract_logger import AbstractLogger
from src.logs.log_item import LogItem
from src.logs.logging_level import LoggingLevel


class MQLogger(AbstractLogger):
    __logging_queue = {
        LoggingLevel.INFO.name: "logs.info",
        LoggingLevel.ERROR.name: "logs.error",
        LoggingLevel.DEBUG.name: "logs.debug",
        LoggingLevel.WARNING.name: "logs.warning",
        LoggingLevel.CRITICAL.name: "logs.critical"}

    def __init__(self, config_path: str = "log.yml", *, routing_key: str = None, name: str = ""):
        """
        Initialize MQLogger by loading RabbitMQ configuration from a YAML file.
        :param config_path: Path to the RabbitMQ YAML configuration file.
        :param routing_key: Routing key for message publishing.
        :param name: Logger name for message tagging.
        """
        self.config = self._load_config(config_path)
        self.is_configured = self.config is not None
        self.routing_key = routing_key or "logs"
        self.name = name

        # Setup RabbitMQ (only if configuration is valid)
        if self.is_configured:
            self.create_exchange()
            self.setup_queues()

    def _load_config(self, path: str) -> Optional[dict]:
        """Load RabbitMQ configuration from a YAML file."""
        config_file = Path(path)
        if not config_file.exists():
            print(f"Configuration file '{path}' not found. RabbitMQ logging will be disabled.")
            return None

        try:
            with open(config_file, "r") as file:
                config = yaml.safe_load(file)
            return config.get("rabbitmq")
        except Exception as e:
            print(f"Error loading RabbitMQ config: {e}. RabbitMQ logging will be disabled.")
            return None

    def log(self, message: str, log_level: LoggingLevel = LoggingLevel.INFO):
        """Log a message to RabbitMQ or standard output if not configured."""
        formatted_message = self._make_message(message, name=self.name)
        log_item = LogItem(message=message, level=log_level)
        if self.is_configured:
            self.publish_log(log_item)
        else:
            print(f"LOG: {log_item}")

    # Additional log severity methods
    def warning(self, message: str):
        self.log(f"WARNING : {message}", log_level=LoggingLevel.WARNING)

    def error(self, message: str):
        self.log(f"ERROR : {message}", log_level=LoggingLevel.ERROR)

    def info(self, message: str):
        self.log(f"INFO : {message}", log_level=LoggingLevel.INFO)

    def debug(self, message: str):
        self.log(f"DEBUG : {message}", log_level=LoggingLevel.DEBUG)

    def critical(self, message: str):
        self.log(f"CRITICAL : {message}", log_level=LoggingLevel.CRITICAL)

    def exception(self, message: str):
        self.log(f"EXCEPTION : {message}")

    def publish_log(self, message: LogItem):
        """Publish a log message to RabbitMQ."""
        try:
            # Get RabbitMQ settings from configuration
            rabbitmq_host = self.config["host"]
            rabbitmq_username = self.config["user"]
            rabbitmq_password = self.config["password"]
            exchange_name = self.config["exchange_name"]

            # Set up credentials for RabbitMQ
            credentials = pika.PlainCredentials(rabbitmq_username, rabbitmq_password)

            # Create a RabbitMQ connection
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(host=rabbitmq_host, credentials=credentials)
            )
            channel = connection.channel()

            # Publish the log message

            serialized_message = pickle.dumps(message)
            channel.basic_publish(
                exchange=exchange_name,
                routing_key=message.level.name,
                body=serialized_message
            )

            connection.close()
        except Exception as e:
            print(f"Error publishing log to RabbitMQ: {e}")  # Handle publishing errors gracefully

    def create_exchange(self):
        """Create the exchange in RabbitMQ if it doesn't already exist."""
        try:
            url = f"http://{self.config['host']}:15672/api/exchanges/%2F/{self.config['exchange_name']}"
            auth = (self.config['user'], self.config['password'])
            # Check if the exchange already exists
            response = requests.get(url, auth=auth)
            if response.status_code == 200:
                print(f"Exchange '{self.config['exchange_name']}' already exists.")
                return

            # Create the exchange if it doesn't exist
            data = {"type": "topic", "durable": True}
            response = requests.put(url, auth=auth, json=data)

            if response.status_code == 201:
                print(f"Exchange '{self.config['exchange_name']}' created successfully.")
            else:
                print(f"Failed to create exchange. Status: {response.status_code}. Message: {response.text}")
        except Exception as e:
            print(f"Error creating exchange: {e}")

    def setup_queues(self):
        """Set up queues and bindings in RabbitMQ if they don't already exist."""
        try:

            auth = (self.config['user'], self.config['password'])

            for routing_key, queue_name in self.__logging_queue.items():
                # Check if the queue already exists
                queue_url = f"http://{self.config['host']}:15672/api/queues/%2F/{queue_name}"
                response = requests.get(queue_url, auth=auth)

                if response.status_code == 200:
                    print(f"Queue '{queue_name}' already exists.")
                else:
                    # Create the queue if it doesn't exist
                    queue_data = {"durable": True}
                    response = requests.put(queue_url, auth=auth, json=queue_data)

                    if response.status_code == 201:
                        print(f"Queue '{queue_name}' created successfully.")
                    else:
                        print(
                            f"Failed to create queue '{queue_name}'. Status: {response.status_code}. Message: {response.text}")

                # Bind the queue to the exchange
                binding_url = f"http://{self.config['host']}:15672/api/bindings/%2F/e/{self.config['exchange_name']}/q/{queue_name}"
                binding_data = {"routing_key": routing_key}

                # Check if the binding already exists by querying the bindings for the exchange
                bindings_url = f"http://{self.config['host']}:15672/api/bindings/%2F/e/{self.config['exchange_name']}/q/{queue_name}"
                binding_response = requests.get(bindings_url, auth=auth)

                # Check if the specific binding exists
                binding_exists = False
                if binding_response.status_code == 200:
                    existing_bindings = binding_response.json()
                    for binding in existing_bindings:
                        if binding.get("routing_key") == routing_key:
                            binding_exists = True
                            break

                if binding_exists:
                    print(
                        f"Queue '{queue_name}' is already bound to exchange '{self.config['exchange_name']}' with routing key '{routing_key}'.")
                else:
                    # Create the binding if it doesn't exist
                    response = requests.post(binding_url, auth=auth, json=binding_data)

                    if response.status_code == 201:
                        print(
                            f"Queue '{queue_name}' successfully bound to exchange '{self.config['exchange_name']}' with routing key '{routing_key}'.")
                    else:
                        print(
                            f"Failed to bind queue '{queue_name}' to exchange. Status: {response.status_code}. Message: {response.text}")
        except Exception as e:
            print(f"Error setting up queues: {e}")
