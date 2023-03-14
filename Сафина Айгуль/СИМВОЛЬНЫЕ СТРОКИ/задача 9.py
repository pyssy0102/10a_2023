print("Введите выражение:")
s=input()
sym = int(s[:s.find('+')])
s = s [s.find('+')+1:]
sym+=int(s[:s.find('+')])+int(s[s.find('+')+1:])
print(sym)
