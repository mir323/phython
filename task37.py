total_sum = 0  

while True:
    try:
        num = int(input())
        if num == 0:
            break
        total_sum += num  
    except ValueError:
        print("Пожалуйста, введите целое число.")

print(total_sum)
