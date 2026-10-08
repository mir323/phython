a = int(input())
b = int(input())
op = input().strip()

if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    if b == 0:
        print("ОШИБКА")
    else:
        print(a / b)
else:
    print("ОШИБКА")
