a=int(input('Введите a (2<p<=10):'))
for t in range(1, a+1):
      for b in range(1, a+1):
          c=t*b//a*10+t*b%a
          print(c)
      print()
