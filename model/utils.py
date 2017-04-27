def are_integers(*args):
    for arg in args:
        if not isinstance(arg, int):
            return False
    return True

def power_mod(a, b, n):
    return int(pow(a, b) % n)

