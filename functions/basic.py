def greet(firstName, lastName):
    print('Hello', firstName)
    print('Welcome abroad!')

greet('Tobi', 'Adesokan')


def return_greeting(name):
    return f'hi {name}'

message = return_greeting("Tobi")
print(message)