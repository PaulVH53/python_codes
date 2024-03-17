import cProfile
import timeit

def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Benchmarking with timeit
recursive_time = timeit.timeit(lambda: fibonacci_recursive(30), number=1000)
iterative_time = timeit.timeit(lambda: fibonacci_iterative(30), number=1000)

print("Recursive Approach Time:", recursive_time)
print("Iterative Approach Time:", iterative_time)

# Profiling with cProfile
# to identify performance bottlenecks
print("\nProfiling Recursive Approach:")
cProfile.run('fibonacci_recursive(30)')

print("\nProfiling Iterative Approach:")
cProfile.run('fibonacci_iterative(30)')

