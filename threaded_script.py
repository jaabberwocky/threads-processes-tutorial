from threading import Thread
import os
import math

def calc():
    for i in range(0, 40000000000):
        math.sqrt(i)

threads = []

for i in range (os.cpu_count()):
    print(f'Registering thread {i}')
    threads.append(Thread(target=calc))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()