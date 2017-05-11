import primality

def miller_rabin(n):
    witnesses, nonwitnesses = list(), list()
    for a in range(1, n):
        res = primality.miller_rabin(n=n, a=a)
        if res == "composite":
            witnesses.append(a)
        else:
            nonwitnesses.append(a)

    print(str(len(witnesses)) + " witnesses:" + str(witnesses))
    print(str(len(nonwitnesses)) + " nonwitnesses:" + str(nonwitnesses))

