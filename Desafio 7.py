primes = []
i = 2
while len(primes) <10001:
    divider = 2
    while divider != i:
        if i % divider == 0:
            break
        else:
            divider += 1
    if divider == i:
        primes.append(i)
    i += 1
print(primes[10000])