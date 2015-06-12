from collections import Counter

LIMIT = 1000000

steps = Counter()

def collatz(n):
    if steps[n] == 0:
        if n == 1:
            steps[n] = 1
        elif n % 2 == 0:
            steps[n] = 1 + collatz(n / 2)
        else:
            steps[n] = 1 + collatz(3 * n + 1)

    return steps[n]

for i in xrange(1, LIMIT):
    collatz(i)

print max(steps.iterkeys(), key=(lambda key: steps[key]))

