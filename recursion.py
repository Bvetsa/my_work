def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

print(fact(3))


def power(a,b):
    if b == 0:
        return 1
    else:
        return power(a,b-1) * a

print(power(2,10))