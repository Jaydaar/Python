import sys

def my_range(n: int):
    start = 0
    while start < n:
        yield start
        start += 1

big_range = my_range(10000)

print("big_range is {} bytes".format(sys.getsizeof(big_range)))

big_list = []
for val in big_range:
    big_list.append(val)

print("big_list is {} bytes".format(sys.getsizeof(big_list)))

big_w = range(10000)

print("big_w is {} bytes".format(sys.getsizeof(big_w)))

big_list2 = []
for val2 in big_w:
    big_list2.append(val2)

print("big_list2 is {} bytes".format(sys.getsizeof(big_list2)))
