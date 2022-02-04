def decorator(func):
    def wrapper():
        print("First string")
        func()
        print("Third string")
    return wrapper


@decorator
def func_1():
    print("Second string")

print(func_1())