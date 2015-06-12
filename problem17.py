def f(n):
    words = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety',
        100: 'hundred',
        1000: 'thousand'
    }

    result = 0

    if n < 20:
        result += len(words[n])
    elif n < 100:
        result += len(words[n - n % 10])

        if n % 10 != 0:
            result += f(n % 10)
    elif n < 1000:
        result += len(words[n / 100])
        result += len(words[100])

        if n % 100 != 0:
            result += len('and')
            result += f(n % 100)
    else:
        result += len(words[n / 1000])
        result += len(words[1000])

    return result

print sum(f(i) for i in xrange(1, 1001))

