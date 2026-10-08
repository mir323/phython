from random import randint
N=randint(1,10)
K=int(input("Угадайте целое число от 1 до 10:"))
while K!=N:
    K=int(input("Повторите попытку:"))
    if K<N:
        print("Меньше")
    elif K>N:
        print("Больше")
    else:
        print("Угадал!")
print(K)
print(N)

