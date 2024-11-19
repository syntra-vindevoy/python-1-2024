bot_name: str = 'Dave'
print(f'Hello! My name is {bot_name}, how can I help you?')

def bot():
    while True:
        user_input: str = input('You: ').lower()
        if user_input in ['goodbye','see you', 'bye','quit','exit']:
            print(f'{bot_name}: Goodbye, have a great day!')
            break
        elif user_input in ['hi','hello','good day']:
            print(f'{bot_name}: Hi there, how can I help you?')
        elif user_input in ['+','add']:
            print(f'{bot_name}: let\'s do some additions, please enter two numbers.')
            try:
                num1: float = float(input('First number: '))
                num2: float = float(input('Second number: '))
                print(f'{bot_name}: {num1 + num2}')
            except ValueError:
                print(f'{bot_name}: Oops, your input is not a number. Make sure to enter a valid number.')
        else:
            print(f'{bot_name}: I\'m sorry, I don\'t understand your input. Please try again.')

bot()