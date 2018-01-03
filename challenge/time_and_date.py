# This program prints information about the 4 timing functions.
# time, monotonic, perf_counter and process_time
from time import get_clock_info

timeNames = [
    'monotonic',
    'perf_counter',
    'process_time',
    'time'
]
for i in timeNames:
    print("{:<12}: {}".format(i, get_clock_info(i)))

