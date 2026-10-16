def main():
    m = int(input().strip())  # количество листков
    # Считаем фамилии из первого листка и сохраним в множество
    first_lesson = set()
    k = int(input().strip())
    for _ in range(k):
        surname = input().strip()
        first_lesson.add(surname)
    
    # Для каждого следующего листка будем проверять, кто из учеников в нём есть
    for _ in range(m - 1):
        k = int(input().strip())
        # Создаём новое множество для текущего листка
        current_lesson = set()
        for _ in range(k):
            surname = input().strip()
            current_lesson.add(surname)
        # Обновляем пересечение: оставляем только тех, кто был и на предыдущем уроке
        first_lesson &= current_lesson
    
    # Выводим результат
    for surname in sorted(first_lesson):  # сортировка для красивого вывода
        print(surname)

if __name__ == "__main__":
    main()
