a = int(input())
b = int(input())
c = 1
for i in range(2, min(a, b)):
  if a % i == 0 and b % i == 0:
    c *= i
    i -= 1
print(c)
