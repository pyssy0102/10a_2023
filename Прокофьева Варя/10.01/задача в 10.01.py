s = input('Введите строку: ')
count = 0
for i in range (1, len(s)):
    if s[i] == ' ' and s[i-1] != ' ':
        count += 1
print(count)
