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
    results = [executor.submit(do_something, sec) for sec in secs] #list comprehension

    for f in concurrent.futures.as_completed(results): #execute futures in completed order
        print(f.result())

# A list to store the joining of
processes = []


# # This is a loop to start the processes
# for _ in range(10): #underscore indicates a throwaway variable name
#     # Because the variable seconds it's added, we need an arg to the multiprocessing
#     p = multiprocessing.Process(target=do_something, args=[1.5])
#     p.start()
#     processes.append(p)
# #loop to join
# for process in processes:
#     process.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
