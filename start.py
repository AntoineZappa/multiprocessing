#!/usr/bin/env python3

import multiprocessing
import time

start = time.perf_counter()

#that is a sismple function to sleep 1 second = time.sleep(1)
def do_something():
    """"""
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')
# A list to store the joining of
processes = []

# This is a loop start the processes
for _ in range(10): #underscore indicates a throwaway variable name
    p = multiprocessing.Process(target=do_something)
    p.start()
    processes.append(p)
#loop to join
for process in processes:
    process.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
