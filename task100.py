username = input()

for char in username:
 if not (char.Isalnum() or char == '_'):
   print(f"Неверный символ: {char}")
 break
else:
 print("OK")