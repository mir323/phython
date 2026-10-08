n = int(input())
n = abs(n)

if n == 0:
    print(1)
else:
    count = 0
    while n > 0:
        n //= 10
        count += 1
    print(count)