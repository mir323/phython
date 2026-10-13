count = 0
while True:
    line = input()
    count += 1
    if line == "СТОП":
        break
    if "кот" in line.lower():  # Проверяем наличие слова «кот» без учёта регистра
        print(count)
        break
else:
    print(-1)  # Если «кот» не найден после ввода «СТОП»
