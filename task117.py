n = int(input())

numbers = list(map(int, input().split()))

unique_numbers = list(set(numbers))

print(len(unique_numbers))
