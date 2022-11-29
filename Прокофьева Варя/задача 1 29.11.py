print ("Введите первое число")
a = int(input())
print ("Введите второе число") 
b = int(input())
def NOD (a, b):
    while a != b:
        if a > b:
            a = a - b
        else: 
            b = b - a
    return b
print("Результат: ", NOD(a,b))
a=int(input("First"))
b=int(input("Second"))
print("NOK=",(a*b)/NOD (a,b))

