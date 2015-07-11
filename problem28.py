from math import sqrt

ans = 1

for i in xrange(3, 1002, 2):
    a = i * i
    b = a - i + 1
    c = b - i + 1
    d = c - i + 1
    ans += a + b + c + d

print ans

