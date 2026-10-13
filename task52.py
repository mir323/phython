n = int(input())  
for _ in range(n):   
    line = input()
    if 'кот' in line or 'Кот' in line:
        print("МЯУ")
        break 
else:
    print("НЕТ")
