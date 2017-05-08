from base_b import convert
from random import randint

DATA_DIR = "../data/"

def get_prime(partition):
    primes = list()
    #filename = glob.glob(DATA_DIR + "primes" + str(partition))
    filename = DATA_DIR + "primes" + str(partition)
    with open(filename, "r") as f:
        content = f.readlines()
    
    line = None

    while not line:
        index = randint(4,len(content))
        line = content[index].strip()

    return line


    #for line in content[4:]:
    #    line = line.strip()
    #    if line:
    #        primes += line.split()
    #return primes


def get_space(partitions, base):
    prime_strings = get_primes(partitions)
    space = list()
    for string in prime_strings:
        base_b = convert(int(string), base)
        space.append(base_b)
    print(space)

