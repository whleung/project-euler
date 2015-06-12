from math import sqrt

def divisors(n):
    for i in xrange(1, int(sqrt(n) + 1)):
        if n % i == 0:
            yield i
            yield n / i

def d(n):
    s = set(divisors(n))
    if n in s:
        s.remove(n)
    return sum(s)

print sum(i for i in xrange(1, 10000) if i == d(d(i)) and i != d(i))

