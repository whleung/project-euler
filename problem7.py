i = 2
ans = 0
num_primes = 0

while num_primes < 10001:
    for j in xrange(2, i):
        if i % j == 0:
            break
    else:
        ans = i
        num_primes += 1

    i += 1

print ans

