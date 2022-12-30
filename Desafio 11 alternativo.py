
n = 20
s = list(range(n+1))
s[0] = s[1] = 0
i = 2

while i < 11:
    for j in range(i**2, n + 1, i):
        s[j] = 0
    i += 1

print(sum(s))