from utils import are_integers
from primality import trial_division
from math import pow

def legendre_symbol(a, p):
    # a and p must be integers
    if not are_integers(a, p):
        raise Exception('a and p must be integers')
    # p must be greater than 2
    if not p > 2:
        raise Exception('p must be greater than 2')
    # p must be prime
    if not trial_division(p):
        raise Exception('p must be a prime number')

    # euler's identity
    e_identity = pow(a, (p-1)/2) % p
    
    # p - 1 = -1 mod p
    if e_identity > 1:
        e_identity = e_identity - p

    return int(e_identity)

