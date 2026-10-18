n = int(input())

numbers = [int(input()) for _ in range(n)]

p = int(input())
q = int(input())

result = sum(numbers[p:q+1])
print(result)