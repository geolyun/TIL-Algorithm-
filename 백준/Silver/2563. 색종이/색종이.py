l = [[0 for _ in range(101)] for _ in range(101)]

n = int(input())
for i in range(n):
  x, y = map(int, input().split())
  for j in range(x, x+10):
    for k in range(y, y+10):
      l[j][k] = 1

result = 0

for i in l:
  result += i.count(1)

print(result)