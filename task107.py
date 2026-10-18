n = int(input())
word1 = input()
word2 = input()

for _ in range(n):
 line = input()
 if word1 in line and word2 in line:
    print(line)