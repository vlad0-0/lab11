p = float(input())
m = 1000
c = 0
while p < 0 or p > 25:
  p = float(input())
p = p / 100
while m < 1100:
  c += 1
  m += m*p
print(c)
print(m)
