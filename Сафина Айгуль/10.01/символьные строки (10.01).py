s=input("введите строку")
s1=""
for c in s:
    if c=="а":
        c="б"
    if c=="А":
        c="Б"
    s1=s1+c
print(s1)
