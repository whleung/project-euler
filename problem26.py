recurring_cycles = []

for i in xrange(2, 1000):
    r = 1
    decimals = []
    remainders = [0]

    while r != 0:
        while r // i == 0:
            decimals.append(r // i)
            r *= 10
        if r / 10 in remainders:
            break
        decimals.append(r // i)
        remainders.append(r / 10)
        r = r % i * 10

    if r == 0:
        recurring_cycle_len = 0
    else:
        recurring_cycle_len = len(remainders) - remainders.index(r / 10)

    recurring_cycles.append((recurring_cycle_len, i))

print max(recurring_cycles)[1]

