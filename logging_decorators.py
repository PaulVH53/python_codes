def log(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@log
def add(x, y):
    return x + y

print("Output will be logged, with args")
add(2, 3)  # Output will be logged

print("Output will be logged, with kwargs")
add(x=2, y=3)  #  containing {'x': 2, 'y': 3}