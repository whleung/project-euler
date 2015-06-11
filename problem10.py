primes = [True] * 2000001
primes[0] = False
primes[1] = False

for i in xrange(2, len(primes)):
    for j in xrange(2, len(primes) / i + 1):
        if i * j < len(primes):
            primes[i * j] = False

print sum(i for i in xrange(len(primes)) if primes[i])

