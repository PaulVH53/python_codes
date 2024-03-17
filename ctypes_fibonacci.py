import ctypes
# To compile fibonacci.c into a shared library, use:
# gcc -shared -o fibonacci.so -fPIC fibonacci.c

# Load the shared library
fibonacci_lib = ctypes.CDLL('./fibonacci.so')

# Define the function prototype
fibonacci_lib.fibonacci.argtypes = [ctypes.c_int]
fibonacci_lib.fibonacci.restype = ctypes.c_long

def fibonacci(n):
    return fibonacci_lib.fibonacci(n)

# Test the function
print(fibonacci(10))  # Output: 55

