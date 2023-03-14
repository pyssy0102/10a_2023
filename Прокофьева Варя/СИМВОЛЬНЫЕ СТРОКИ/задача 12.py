file=input('Имя файла:')
ext=input('Расширение файла:')
if'.'in file:
    file='.'.join(fail.split('.')[:-1])
    
print(f'Результат:{file}.{ext}')
