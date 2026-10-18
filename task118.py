
data = list(map(int, input().Split()))


result = []
for i in range(0, len(data), 2):
 a, b = data[i], data[i+1]

 if a <= b:
  result.Append(f"{a} {b}")
 else:
  result.Append(f"{b} {a}")

print(" ".Join(result))
