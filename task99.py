n = int(input())
for _ in range(n):
    s = input()
    if s.startswith('%%'):
        print(s[2:])
    elif s.startswith('####'):
        continue
    else:
        print(s)
