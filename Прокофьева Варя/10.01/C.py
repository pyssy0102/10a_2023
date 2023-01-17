s=input()
m=0
count=0
for c in range(1,len(s)):
    if s[c]!=" " and s[c-1]!=" ":
        count+=1
    else:
        if m<count:
            m=count
            count=0
print(c,"букв")        
