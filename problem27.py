from math import sqrt

d = {}

def divisors(n):
    for i in xrange(1, int(sqrt(n) + 1)):
        if n % i == 0:
            yield i
            yield n / i

def isPrime(n):
    if n not in d:
        d[n] = len(set(divisors(n))) == 2

    return d[n]

max_a = 0
max_b = 0
max_n = 0

for a in xrange(-1000, 1001):
    for b in xrange(-1000, 1001):
        n = 0
        k = n * n + a * n + b

        while k > 0 and isPrime(k):
            n += 1
            k = n * n + a * n + b

        if n > max_n:
            max_n = n
            max_a = a
            max_b = b

print max_a * max_b

