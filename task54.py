count = 0  # Количество строк с «кот» или «Кот»
first_cat_line = -1  # Номер первой такой строки (-1 если не найдено)
line_number = 0  # Текущий номер строки

while True:
    line = input()
    line_number += 1
    if line == "СТОП":
        break
    # Проверяем, есть ли «кот» в строке (без учёта регистра)
    if 'кот' in line.lower():
        count += 1
        # Если это первая найденная строка с котом, запоминаем номер
        if first_cat_line == -1:
            first_cat_line = line_number

# Выводим результат
print(count, first_cat_line)
