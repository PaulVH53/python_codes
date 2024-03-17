import time

def performance_monitor(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} executed in {end_time - start_time} seconds")
        return result
    return wrapper

@performance_monitor
def heavy_computation():
    # Some heavy computation
    time.sleep(10)

heavy_computation()  # Output: "heavy_computation executed in 3.0 seconds"

@performance_monitor
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

fibonacci(150)