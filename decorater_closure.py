def welcome_decorator(func):
    def wrapper():
        print("Welcome to the decorated function!")
        func("welcome")
        print("Thank you for using the decorated function!")
    return wrapper()

welcome_decorator(print)
