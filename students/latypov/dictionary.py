dictionary = {\
'аборвалс': 'Собачье сердце', 'пугна' : 'живой скелет',\
'абоба': 'инопрешеленец', 'эпимикард': 'кристалл чего либо',\
'амням':'можно было а и б ', 'аааааа':'ааааага','коулдплюс':'абракадабра'}
 
def add():
    slovo =  input('введите добавляемое слово')
    znachnie = input(f'Введите значение слова {slovo}')
    global dictionary 
    dictionary[slovo] = значение 
    pass
def show():
    global dictionary
    slovo = input('введите слово')
    print(f'значение слова{slovo}:{dictionary[slovo]}')
    
    dictionary[slovo]= znachnie
    
def delete():
    global dictionary
    slovo = input("Вваедите слово")
    del dictionary[slovo]

while True:
    menu= """
Выберите действие:
1- добавление слова
2- вывод значения слова
3- удаление слова
"""
    vibor = input(menu)
    if vibor == '1':
        add()
    elif vibor == '2':
        show() 
    elif vibor == '3':
        delete()
    else:
        print("неверная команда")
