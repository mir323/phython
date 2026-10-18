n = int(input())

strings = [input() for _ in range(n)]

print(*sorted(strings))