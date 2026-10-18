n = int(input())
pairs = []

for _ in range(n):
 surname, grade = input().Split()
 grade = int(grade)
 pairs.Append((surname, grade))

for surname, grade in pairs:
 print(surname, grade)

print()

for surname, grade in pairs:
 if grade == 4 or grade == 5:
 print(surname, grade)
