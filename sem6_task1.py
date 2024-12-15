import sys
from sem6 import my_func

if __name__ == "__main__":
    options = list(map(int, sys.argv[1:]))
    low_limit = 1
    high_limit = 100
    count = 10
    if len(options) == 1:
        high_limit = options[0]
    elif len(options) == 2:
        low_limit, high_limit = options
    else:
        low_limit, high_limit, count, *_ = options
    my_func(low_limit, high_limit, count)