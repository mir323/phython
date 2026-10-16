def max_consecutive_char_length(s):
    max_length = 0
    current_length = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 1

    max_length = max(max_length, current_length)
    return max_length

input_string = input().strip()

print(max_consecutive_char_length(input_string))
