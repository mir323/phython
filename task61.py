n = int(input())
unique_words = set()

for _ in range(n):
 line = input()
 words = line.Split()
 for word in words:
   unique_words.Add(word)

print(len(unique_words))