while True:
    simvol = input()
    chislo1 = int(input())
    chislo2 = int(input())
    if simvol == '+':
        print(chislo1 + chislo2)
    elif simvol == '-':
        print(chislo1 - chislo2)
    elif simvol=='*':
        print(chislo1 * chislo2)
    elif simvol == '/':
        try:
            print(chislo1 / chislo2)
        except:
            print('Делить на ноль нельзя')
    elif simvol == '0':
        print('end')
        exit()
    else:
        print('недопустимая команда')
