n = int(input())  
total = 0 

for _ in range(n):
    num = int(input())  
    if num <= 0: 
        continue  
    total += num  

print(total)  
