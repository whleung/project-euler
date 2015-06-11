ans = 0

for a in range(1000):
    for b in range(a, 1000):
        p = a * b
        s = str(p)
        if s[::-1] == s and p > ans:
            ans = p

print ans

