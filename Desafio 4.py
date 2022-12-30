x = 20
i = 1
while i <= 20:
  if x % i == 0:
    i += 1
  else:
    x = x + 1
    i = 1
print(x)