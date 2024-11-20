"""
What is Python Event-Driven Programming?
Python's event-driven programming model revolves around the concept of an event loop. An event loop continuously
monitors events and dispatches them to the appropriate event handlers.
This allows the program to efficiently handle multiple asynchronous tasks concurrently.
"""

import asyncio


async def event_handler():
    print("Event Triggered!")
    await asyncio.sleep(1)


async def main():
    print("Waiting for event...")
    await asyncio.gather(event_handler(), asyncio.sleep(2))


asyncio.run(main())

"""
Basic Event-Driven Programming in Python
"""


class Event:
    def __init__(self):
        self.handlers = []

    def subscribe(self, handler):
        self.handlers.append(handler)

    def trigger(self, *args, **kwargs):
        for handler in self.handlers:
            handler(*args, **kwargs)


# Define event and handlers
def on_event_fired(message):
    print(f"Event: {message}")


event = Event()
event.subscribe(on_event_fired)

# Trigger event
event.trigger("Hello, World!")

"""
Python Event-Driven Tasks
Tasks (asyncio.Task) are used to schedule and manage coroutines within the event loop. They represent asynchronous 
units of work and allow for better control over execution. Here, we create two coroutines 
foo() and bar() representing two asynchronous tasks. We use loop.create_task() to create 
Task objects for each coroutine and run them concurrently using asyncio.wait().
"""
import asyncio


async def foo():
    print("Foo")
    await asyncio.sleep(1)
    print("End Foo")


async def bar():
    print("Bar")
    await asyncio.sleep(2)
    print("End Bar")


loop = asyncio.get_event_loop()
task1 = loop.create_task(foo())
task2 = loop.create_task(bar())

loop.run_until_complete(asyncio.wait([task1, task2]))

import asyncio


@asyncio.coroutine
def countdown(n):
    while n > 0:
        print("T-minus", n)
        yield from asyncio.sleep(1)
        n -= 1


loop = asyncio.get_event_loop()
loop.run_until_complete(countdown(3))
