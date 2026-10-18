n = int(input())
lines = [input() for _ in range(n)]
search_query = input()

for line in lines:
    if search_query in line:
        print(line)