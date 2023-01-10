x=7**103+6*(7**104)-3*(7**57)+98
sum=0
while x:
    sum+=x%7

    x//=7
print(sum)
