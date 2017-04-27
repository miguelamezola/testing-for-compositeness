from utils import are_integers

def base_b(n, b):
    if not are_integers(a, b):
        raise Exception('a and b must be integers')   

    a = []
    while n > 0:
        r = n % b
        a = [r] + a
        n = n // b

    return a

def division_algorithm(a, b):
    if not are_integers(a, b):
        raise Exception('a and b must be integers')
    if not b > 0:
        raise Exception('b must be greater than 0')
  
    q = 0

    if a >= 0:
        while (q + 1) * b <= a:
            q = q + 1
    else:
        while q * b >= a:
            q = q - 1

    r = a - b * q

    return {'q': q, 'r': r}

