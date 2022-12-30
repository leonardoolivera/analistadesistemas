def eh_trio(a, b, c):
    a = a**2
    b = b**2
    c = c**2
    return a + b == c


for a in range(1, 999):
    for b in range(a, 1000):
        c = 1000 - a - b
        if c < a or c < b or b == a:
            continue
        if eh_trio(a, b, c):
            print(a*b*c)
            