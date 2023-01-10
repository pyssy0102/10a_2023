x=4**103+3*(4**444)-2*(4**44)+67
count3=0
while x:
    if x % 4==3:count3+=1

    x//=4
print(count3)
