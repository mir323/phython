n = int(input())

strings = [input() for _ in range(n)]

for string in reversed(strings):
    print(string)