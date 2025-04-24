city_list = ["Москва"]
city_tuple = ("Москва")
city_set =  {"Москва"}
city_dict = {"Москва":"Столица"}

while True:
    menu = """
    Выберите действие:
    1 - добавление города
    2 - вывод 
    """
    vibor = input(menu)
    if vibor == '1':
        add()
    elif vibor == '2':
        show()
    elif vibor == '3':
        delete()
    else:
        print("не верная команда.")
def sort():
    global city_dict
    global city_set
    global city_tuple
    global city_list
    
    city_list = sorted(city_list, key = lambda x: len(x))
    city_dict = sorted(sity_dict, key  = lambda x: len(x[0]))
    print(city_dict)
    print(city_set)
    print(city_tuple)
    print(city_list)
def add():
    global city_dict
    global city_set
    global city_tuple
    global city_list 
    gorod = input("Введите название города")
    dictionary[gorod] = 'город'
    city_list.append(gorod)
    city_set.add(gorod)
    
    sort()
    
def delete():
    global city_list
    global city_tuple 
    global city_set 
    global city_dict
    slovo = input("Вваедите слово")
