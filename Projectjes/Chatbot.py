bot_name: str = 'Den Dave'
print(f'{bot_name}: Hello! My name is {bot_name}, how can I help you?')

def calculate(expression: str) -> str:
    try:
        parts = expression.split()
        if len(parts) != 3:
            return "I can only calculate simple expressions like '2 + 2', '5 * 3', '7 - 3' or 9 + 2. \nMake sure to use spaces between numbers."

        num1, operator, num2 = parts
        num1, num2 = float(num1), float(num2)  # Convert numbers

        if operator == '+':
            return str(num1 + num2)
        elif operator == '-':
            return str(num1 - num2)
        elif operator == '*':
            return str(num1 * num2)
        elif operator == '/':
            if num2 == 0:
                return "I can't divide by zero!"
            return str(num1 / num2)
        else:
            return f"I don't recognize the operator '{operator}'. Try +, -, *, or /."
    except ValueError:
        return "Please provide a valid math expression like '2 + 2'."

def bot():
    while True:
        user_input: str = input('You: ').lower()
        if user_input in ['goodbye','see you', 'bye','quit','exit']:
            print(f'{bot_name}: Goodbye, have a great day!')
            break
        elif user_input in ['hi','hello','good day']:
            print(f'{bot_name}: Hi there, how can I help you?')
        elif any(op in user_input for op in ['+', '-', '*', '/']):
            response = calculate(user_input)
            print(f'{bot_name}: {response}')
        else:
            print(f'{bot_name}: I\'m sorry, I don\'t understand your input. Please try again.')

bot()