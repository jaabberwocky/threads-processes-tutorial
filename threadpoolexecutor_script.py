from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
import time
import random


data = [
    1452526,
    244567788,
    31123,
    93333,
    11231234,
    1,
    3414,
    11133,
    51232,
    5124123123,
]


def calc_square(i: int) -> str:
    """Calculates square of a number.

    Args:
        i (int): number

    Returns:
        str: String representation of results
    """
    sleep_time = random.randint(1, 10)
    print(f"Calculating square of {i} with sleep of {sleep_time}\n")
    time.sleep(sleep_time)
    return f"Square of {i}: {i ** 2}"


def performance_tracker(func):
    def wrapper():
        t1 = time.perf_counter()
        func()
        t2 = time.perf_counter()
        print(f"Time elapsed: {t2 - t1}s")
    return wrapper


@performance_tracker
def run_thread_pool():
    with ThreadPoolExecutor() as executor:
        future_list = []
        for i in data:
            future = executor.submit(calc_square, i)
            future_list.append(future)

        for f in as_completed(future_list):
            print(f.result())


@performance_tracker
def run_process_pool():
    with ProcessPoolExecutor() as executor:
        future_list = []
        for i in data:
            future = executor.submit(calc_square, i)
            future_list.append(future)

        for f in as_completed(future_list):
            print(f.result())


if __name__ == "__main__":
    print("Running ThreadPoolExecutor...")
    run_thread_pool()
    print("Running ProcessPoolExecutor")
    run_process_pool()
