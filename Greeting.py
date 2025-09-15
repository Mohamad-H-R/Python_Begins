def greet(name):
    greeting = f"Hello, {name}!"
    return greeting


user_name = input("What's your name: ")
print(greet(user_name))