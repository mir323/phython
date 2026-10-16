text = input().lower()

vowels = "аеёиоуыэюя"

count = sum(1 for char in text if char in vowels)

print(count)