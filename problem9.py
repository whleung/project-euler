ans = 0
c = 0

while ans == 0:
    for b in xrange(c):
        for a in xrange(b):
            if a * a + b * b == c * c and a + b + c == 1000:
                ans = a * b * c
                break
        else:
            continue
        break
    c += 1

print ans

