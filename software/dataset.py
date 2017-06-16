
DATASETS_DIR = "./data/"
DATASET_SIZE = 1000
RANGE_MAX = 982451653

from random import shuffle
from time import time
from math import sqrt
from math import floor


def get(minimum, maximum, range_max=RANGE_MAX):
    if minimum < 2:
        raise ValueError("dataset: minimum should be greater than or equal to 2")
    if range_max > RANGE_MAX:
        raise ValueError("dataset: range_max should be less than or equal to %d" % RANGE_MAX)
    if maximum > range_max:
        raise ValueError("dataset: maximum shoudl be less than or equal to %d" % range_max)
    int_list = list(range(minimum, maximum + 1))

    shuffle(int_list)
    
    with open(DATASETS_DIR + "%d_%d_%d.csv" % (int(time()), minimum, maximum), "w") as f:
        for n in int_list:
            f.write("%d, %d\n" % (n, trial_division(n)))


def trial_division(n):
    if n < 2:
        raise Exception("every integer n greater than or equal to 2 has a prime factor")
    if n % 1 != 0:
        raise Exception("n must be an integer")

    k = floor(sqrt(n))

    for i in range(2, k + 1):
        if (n / i) % 1 == 0:
            return False

    return True

