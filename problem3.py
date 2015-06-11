n = 600851475143;
prime_factors = set()

i = 2

while i <= n:
    if n % i == 0:
        prime_factors.add(i)
        while n % i == 0:
            n /= i;
    i += 1

print max(prime_factors)

