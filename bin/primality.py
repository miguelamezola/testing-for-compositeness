from utils import are_integers
from utils import power_mod
from math import sqrt
from math import floor
from random import randint

def trial_division(n):

    if n < 2:
        raise Exception("every integer n greater than or equal to 2 has a prime factor")
    if not are_integers(n):
        raise Exception("n must be an integer")

    k = floor(sqrt(n))

    for i in range(2, k + 1):
        if (n / i) % 1 == 0:
            return False

    return True


def fermats_test(n):

    if not are_integers(n):
        raise Exception("n must be an integer")
    if not n > 0:
        raise Exception("n must be a positive integer")
    
    nonwitnesses = []
    witnesses = []

    for a in range(1,n):
        right_hand_side = pow(a,n-1,n)
        if right_hand_side is 1:
                nonwitnesses.append(a)
        else:
                witnesses.append(a)

    return {"nonwitnesses": nonwitnesses, "witnesses": witnesses}

def miller_rabin(n):
 
    if not are_integers(n):
        raise Exception("n must be an integer")
    if not n > 0:
        raise Exception("n must be a positive integer")
    if n % 2 == 0:
        raise Exception("n must be odd")

    base = randint(1,n-1)

    for k in range(1, (n-1) // 2 + 1):
        exp = (n-1) // pow(2,k)
        rhs = pow(base, exp, n)
        print(base, exp, rhs)

        #if not (rhs + 1) % n:
        #    return False

        if (exp / 2) % 1 != 0:
            #if not (rhs - 1) % n:
            #    return False
            #return {base, True}
            print(base, exp, rhs)
            break
