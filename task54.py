count = 0  # Количество строк с «кот» или «Кот»
first_cat_line = -1  # Номер первой такой строки (-1 если не найдено)
line_number = 0  # Текущий номер строки

while True:
    line = input()
    line_number += 1
    if line == "СТОП":
        break
    if 'кот' in line.lower():
        count += 1
        if first_cat_line == -1:
            first_cat_line = line_number

print(count, first_cat_line)
