n = int(input())

letters = [''] * n

for _ in range(n):
    position, char = input().split()
    letters[int(position) - 1] = char

result = ''.join(letters)
print(result)