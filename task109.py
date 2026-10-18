white_list = set()

print("Введите элементы белого списка (для завершения введите пустую строку):")
while True:
    item = input()
    if item == "": 
        break
    white_list.add(item) 

print("Введите запросы (для завершения введите пустую строку):")
while True:
    query = input()
    if query == "":
        break
    if query in white_list:
        print(query)