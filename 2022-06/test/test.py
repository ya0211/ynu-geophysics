import threading
from concurrent.futures import ThreadPoolExecutor


def func(a, b):
    return a + b


with ThreadPoolExecutor(2) as pool:
    futures = [pool.submit(lambda x: func(*x), i) for i in [(1, 2), (2, 3)]]
    for f in futures:
        print(f.result())

with ThreadPoolExecutor(2) as pool:
    results = pool.map(lambda x: func(*x), [(1, 2), (2, 3)])
    results = [r for r in results]
    print(results)
