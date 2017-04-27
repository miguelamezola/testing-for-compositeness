
DATASETS_DIR = "./datasets/"
DATASET_SIZE = 1000
PRIME_LIST_DIR = "./prime_lists/"
RANGE_MAX = 982451653

from random import sample
from time import time

def is_prime(n):


    if n < 2:
        return 0
    if n == 2:
        return 1
    if n % 2 == 0:
        return 0

    if n <= 15485863:
        fn = "015485863"
    elif n <= 32452843:
        fn = "032452843"
    elif n <= 49979687:
        fn = "049979687"
    elif n <= 67867967:
        fn = "067867967"
    elif n <= 86028121:
        fn = "086028121"
    elif n <= 104395301:
        fn = "104395301"
    elif n <= 122949823:
        fn = "122949823"
    elif n <= 141650939:
        fn = "141650939"
    elif n <= 160481183:
        fn = "160481183"
    elif n <= 179424673:
        fn = "179424673"
    elif n <= 198491317:
        fn = "198491317" 
    elif n <= 217645177:
        fn = "217645177"
    elif n <= 236887691:
        fn = "236887691"
    elif n <= 256203161:
        fn = "256203161"
    elif n <= 275604541:
        fn = "275604541"
    elif n <= 295075147:
        fn = "295075147"
    elif n <= 314606869:
        fn = "314606869"
    elif n <= 334214459:
        fn = "334214459"
    elif n <= 353868013:
        fn = "353868013"
    elif n <= 373587883:
        fn = "373587883"
    elif n <= 393342739:
        fn = "393342739"
    elif n <= 413158511:
        fn = "413158511"
    elif n <= 433024223:
        fn = "433024223"
    elif n <= 452930459:
        fn = "452930459"
    elif n <= 472882027:
        fn = "472882027"
    elif n <= 492876847:
        fn = "492876847"
    elif n <= 512927357:
        fn = "512927357"
    elif n <= 533000389:
        fn = "533000389"
    elif n <= 553105243:
        fn = "553105243"
    elif n <= 573259391:
        fn = "573259391"
    elif n <= 593441843:
        fn = "593441843"
    elif n <= 613651349:
        fn = "613651349"
    elif n <= 633910099:
        fn = "633910099"
    elif n <= 654188383:
        fn = "654188383"
    elif n <= 674506081:
        fn = "674506081"
    elif n <= 694847533:
        fn = "694847533"
    elif n <= 715225739:
        fn = "715225739"
    elif n <= 735632791:
        fn = "735632791"
    elif n <= 756065159:
        fn = "756065159"
    elif n <= 776531401:
        fn = "776531401"
    elif n <= 797003413:
        fn = "797003413"
    elif n <= 817504243:
        fn = "817504243"
    elif n <= 838041641:
        fn = "838041641"
    elif n <= 858599503:
        fn = "858599503"
    elif n <= 879190747:
        fn = "879190747"
    elif n <= 899809343:
        fn = "899809343"
    elif n <= 920419813:
        fn = "920419813"
    elif n <= 941083981:
        fn = "941083981"
    elif n <= 961748927:
        fn = "961748927"
    elif n <= 982451653:
        fn = "982451653"
    else:
        raise ValueError("%d is greater than 982451653" % n)

    with open(PRIME_LIST_DIR + fn, "r") as f:
        content = f.readlines()

    for line in content[4:]:
        line = line.strip()
        if line:
            if str(n) in line.split():
                return 1
    return 0


def get(dataset_size=DATASET_SIZE, range_max=RANGE_MAX):
    if dataset_size >= range_max:
        raise ValueError("dataset size should be less than or equal to range max")
    pop = range(2, range_max+1)
    sam = sample(pop, dataset_size)

    with open(DATASETS_DIR + "%d_%d_%d.dataset" % (int(time()), range_max, dataset_size), "w") as f:
        for n in sam:
            f.write("%d\t%d\n" % (n, is_prime(n)))


