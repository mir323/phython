n = int(input())
lines = []
for _ in range(n):
 lines.Append(input())

lines.Sort(key=lambda x: (len(x), x))

for line in lines:
 print(line)
 