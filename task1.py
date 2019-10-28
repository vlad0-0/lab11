a = int(input())
b = int(input())
while b > a:
  a = int(input())
  b = int(input())
for i in range(a, b-1, -1):
  for j in range(abs(i)):
    print(i)
