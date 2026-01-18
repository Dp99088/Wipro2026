import time
def execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()
        print(f"Function '{func.__name__}' executed in {end_time - start_time:.6f} seconds")
        return result
    return wrapper
@execution_time
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
print("Factorial", factorial(5))