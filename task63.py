def read_numbers_until_empty():
    numbers = []
    while True:
        try:
            line = input().strip()
        except EOFError:
            break
        if line == "":
            break
        for num_str in line.split():
            numbers.append(int(num_str))
    return numbers

list1 = read_numbers_until_empty()

list2 = read_numbers_until_empty()

set2 = set(list2)
result = []
seen = set()
for num in list1:
    if num in set2 and num not in seen:
        result.append(num)
        seen.add(num)

if result:
    print(" ".join(map(str, result)))
else:
    print("EMPTY")