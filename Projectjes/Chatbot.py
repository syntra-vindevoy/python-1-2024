bot_name: str = 'Dave'
print(f'Hello! My name is {bot_name}, how can I help you?')

def bot():
    while True:
        user_input: str = input('You: ').lower()
        if user_input == 'quit':
            print('See you later')  # Move this before the break
            break
        else:
            print(f'{bot_name}: I heard you say "{user_input}"')  # Example response

bot()
#test