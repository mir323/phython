n = int(input()) 

found_cat = False 
found_dog = False 

for _ in range(n): 
    line = input() 
    line = line.lower()  

    if "кот" in line: 
        found_cat = True 
    if "пёс" in line: 
        found_dog = True 

if found_cat and not found_dog: 
    print("МЯУ") 
else: 
    print("НЕТ")