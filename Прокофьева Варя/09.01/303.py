x=4**1103+3*(4**1444)-2*(4**144)+66
sum=0
while x:
    sum+=x%4

    x//=4
print(sum)
