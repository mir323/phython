a = []
c = 0
for i in range(int(input())):
    a.append(int(input()))
n = int(input())
for i in a:
    for j in a:
        if i != j and i * j == n:
            c += 1
if c == 0:
    print('НЕТ')
else:
    print('ДА')