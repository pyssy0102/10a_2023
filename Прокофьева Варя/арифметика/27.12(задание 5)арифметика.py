z = 0
print ('¬вод основани€ системы')
print ('¬ведите p (2<p<=16): ')
p = int(input())
print ( p, '- рична€ таблица умножени€')
for x in range (1,p):
    for y in range (1,p):
        z /= (x*y // p)*10 + (x*y)%p
        print('(:3d)'.format(z), end='')
    print()
