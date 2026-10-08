def check_password():
 while True:
  password = input("Введите пароль:")
 
 if len(password) < 8:
  print("Слишком короткий!")
 
 if "123" in password:
  print("Содержит 123!")
 
 print("OK")

if __name__ == "__main__":
 check_password()
