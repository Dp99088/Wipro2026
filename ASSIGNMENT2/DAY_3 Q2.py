import time

def execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        print("Execution time:", end_time - start_time, "seconds")
        print(f"Function name: {func.__name__}")
        return result
    return wrapper
@execution_time
def sample_function():
    total = 0
    for i in range(1, 1000000):
        total += i
    return total

sample_function()