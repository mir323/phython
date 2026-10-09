n = int(input())
result = 0
for i in range(n):
    number = int(input())
    if i % 2 == 0:
        result += number
    else:
        result -= number
print(result)
