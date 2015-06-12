from math import sqrt

def num_divisors(n):
    result = 0

    for i in xrange(1, int(sqrt(n)) + 1):
        if n % i == 0:
            if n / i == sqrt(n):
                result += 1
            else:
                result += 2

    return result

n = 0
i = 0

while num_divisors(n) < 500:
    n += i
    i += 1

print n
    
