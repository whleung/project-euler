a0, a1, total = 1, 2, 2

while a1 < 4000000:
    a0, a1 = a1, a0 + a1
    if a1 % 2 == 0:
        total += a1

print total

