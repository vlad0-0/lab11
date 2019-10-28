a = float(input())
b = float(input())
c = 0
while a <= 0 or b <= 0 or a < b:
  a = float(input())
  b = float(input())
while a > b:
  a = a - b
  c += 1
print(c)
