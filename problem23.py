from math import sqrt

def divisors(n):
    for i in xrange(1, int(sqrt(n) + 1)):
        if n % i == 0:
            yield i
            yield n / i

def proper_divisors(n):
    s = set(divisors(n))
    if n in s:
        s.remove(n)
    return s

abundants = []

for i in xrange(1, 28124):
    if sum(proper_divisors(i)) > i:
        abundants.append(i)

sum_abundant_pairs = set()

for i in xrange(len(abundants)):
    for j in xrange(i + 1):
        sum_abundant_pairs.add(abundants[i] + abundants[j])

print sum(set(range(1, 28124)) - sum_abundant_pairs)

