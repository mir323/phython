s = input()
if s.startswith(('Не', 'не')):
    print(s[2:])
else:
    print(s)