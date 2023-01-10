s11="0123456789a"
s12="0123456789ab"
s14="0123456789abcd"
for x in s11:
    for y in s12:
       for z in s14: 
               a1="3364"+x
               a2=x+"7946"
               a3="55"+x+"87"

            if summ%10==int(a3,14):
               print(int(a3))
               break
