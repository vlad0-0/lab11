f1 = 0
f2 = 1
n = 2
k = int(input())
while f2 < k:
  f1, f2 = f2, f1+f2
  n += 1
if f2 != k:
  print("Неверный параметр")
else:
  print(n)
