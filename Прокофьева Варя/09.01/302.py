x=6**203+5*(6**405)-3*(6**144)+76
sum=0
while x:
    sum+=x%6

    x//=6
print(sum)
