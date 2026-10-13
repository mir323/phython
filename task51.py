n = int(input())
found = False

for _ in range(n):
 line = input()
 if "кот" in line or "Кот" in line:
  found = True

if found:
 print("МЯУ")
else:
 print("НЕТ")
