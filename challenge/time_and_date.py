from time import get_clock_info

timeNames = [
    'monotonic',
    'perf_counter',
    'process_time',
    'time'
]
for i in timeNames:
    print("{:<12}: {}".format(i, get_clock_info(i)))

