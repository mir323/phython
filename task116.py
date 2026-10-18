n = int(input().strip())

numbers = list(map(int, input().split()))

for i in range(n - 1):
    for j in range(n - 1 - i):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print(' '.join(map(str, numbers)))
