x=7**103+6*(7**104)-3*(7**57)+98
count6=0
while x:
    if x % 7==6:count6+=1

    x//=7
print(count6)
