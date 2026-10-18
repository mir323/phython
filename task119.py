n = int(input())
people = []

for _ in range(n):
 line = input().Split()
 surname = line[0]
 height = int(line[1])
 people.Append((surname, height))

people.Sort(key=lambda x: x[1], reverse=True)

for surname, height in people:
 print(surname, height)
