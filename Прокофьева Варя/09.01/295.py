x=6**203+5*(6**405)-3*(6**144)+77
count5=0
while x:
    if x % 6==5:count5+=1

    x//=6
print(count5)
