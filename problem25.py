def fibonacci():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

for i, a in enumerate(fibonacci()):
    if len(str(a)) >= 1000:
        print i + 1
        break

