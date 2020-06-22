#!/usr/bin/env python3

import concurrent.futures  #different way to do multiprocessing
import time

start = time.perf_counter()

# passing a variable throw the function
def do_something(seconds):
    """"""
    print(f'Sleeping {seconds} second(s)...')
    #that is a sismple function to sleep 1 second = time.sleep(1)
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'


with concurrent.futures.ProcessPoolExecutor() as executor:

    secs=[5, 4, 3, 2, 1]
    results = executor.map(do_something, secs) # map is a loop for iterable objects
    # when using submit method returns future objects
    # map return the results
    # for result in results: # results are in order
    #     print(result) # exceptions should be here


finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
