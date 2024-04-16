import time
from multiprocessing import Pool, freeze_support

def expensive_computation(num):
    result = sum([i ** 2 for i in range(num)])
    return result

def sequential_execution(numbers):
    results = []
    for num in numbers:
        results.append(expensive_computation(num))
    return results

def parallel_execution(numbers):
    with Pool() as pool:
        results = pool.map(expensive_computation, numbers)
    return results

if __name__ == '__main__':
    freeze_support()  # Required for Windows
    numbers = [1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000] * 4

    start_time = time.time()
    sequential_results = sequential_execution(numbers)
    sequential_time = time.time() - start_time

    start_time = time.time()
    parallel_results = parallel_execution(numbers)
    parallel_time = time.time() - start_time

    print(f"Sequential execution time: {sequential_time:.5f} seconds")
    print(f"Parallel execution time: {parallel_time:.5f} seconds")

"""
Sequential execution time: 16.46976 seconds
Parallel execution time: 5.30785 seconds
"""