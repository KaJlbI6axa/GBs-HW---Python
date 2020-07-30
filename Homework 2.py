# -------------------------------------------------------------------------------------------------1------------------------------------------------------------------------------------------------------------------
# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя,
# а указать явно, в программе.

my_list = [12, None, -77, 'True', True, 9.5]
def my_type(el):
    for el in range(len(my_list)):
        print(type(my_list[el]))
    return
my_type(my_list)
print("-" *100)
#  -----------------------------------------------------------------------------------------Вариант решения------------------------------------------------------------------------------------------------------------
listInt = 5
listFloat = 2.5
listStr = "Putin is the real King!"
listList = ['a', '2']
listTuple = ('b', '3')
listDict = {'city': 'Moscow', 'country': 'Russia'}

superMegalist = [listInt, listFloat, listStr, listList, listTuple, listDict]
for i in superMegalist:
    print(f'{i} is {type(i)}')
print("-" *100)
#  -------------------------------------------------------------------------------------------------2------------------------------------------------------------------------------------------------------------------
# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить
# на своем месте.
# Для заполнения списка элементов необходимо использовать
# функцию input().

a = 1
while a == 1:
    try:
        el_count = int(input(f'Enter count of list: '))
        a = 0
    except ValueError:
        print('Write only numbers!')
my_list = []
i = 0
el = 0
while i < el_count:
    attempts = el_count - i
    my_list.append(input(f"Enter next value. Attempts remain {attempts}\n"))
    i += 1

for elem in range(int(len(my_list)/2)):
        my_list[el], my_list[el + 1] = my_list [el + 1], my_list[el]
        el += 2
print(my_list)
# -------------------------------------------------------------------------------------------------3------------------------------------------------------------------------------------------------------------------
# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна,
# лето, осень).
# Напишите решения через list и через dict.
        
seasons_list = ['winter', 'spring', 'summer', 'autumn']
seasons_dict = {1 : 'winter', 2 : 'spring', 3 : 'summer', 4 : 'autumn'}
while True:
    month = input(f'Enter number of month: \n Type "q" or "й" to quit\n')
    if month == 'q' or month == 'й' :
        print('Bye, Bye!')
        break
    else:
        check = True if month.isdigit() else False
        if check == False:
            print("---------Enter the integer!!!--------")
        else:
            changeType = int(month)
            if changeType ==1 or changeType == 12 or changeType == 2:
                    print(f"It's a {seasons_dict.get(1)} in the Dict")
                    print(f"It's a {seasons_list[0]} in the List")
            elif changeType == 3 or changeType == 4 or changeType ==5:
                print(f"It's a {seasons_dict.get(2)} in the Dict")
                print(f"It's a {seasons_list[1]} in the List")
            elif changeType == 6 or changeType == 7 or changeType == 8:
                print(f"It's a {seasons_dict.get(3)} in the Dict")
                print(f"It's a {seasons_list[2]} in the List")

            elif changeType == 9 or changeType == 10 or changeType == 11:
                print(f"It's a {seasons_dict.get(4)} in the Dict")
                print(f"It's a {seasons_list[3]} in the List")
            else:
                    print("Такого месяца не существует") 
# -------------------------------------------------------------------------------------------------4------------------------------------------------------------------------------------------------------------------
# Пользователь вводит строку из нескольких слов, разделённых
# пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное,
# выводить только первые 10 букв в слове.\

my_str = input("Enter ur string:\n")
my_word = []
num = 1
for el in range(my_str.count(' ') + 1):
    my_word = my_str.split()
    if len(str(my_word)) <= 10:
        print(f" {num} {my_word [el]}")
        num += 1
    else:
        print(f" {num} {my_word [el] [0:10]}")
        num += 1
# -------------------------------------------------------------------------------------------------5------------------------------------------------------------------------------------------------------------------
# Реализовать структуру «Рейтинг», представляющую собой
# не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться
# после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, 
# например, my_list = [7, 5, 3, 3, 2].

my_list = [7, 5, 3, 3, 2]
print(f"Rating - {my_list}")
while True:
    digit = (input("Enter ur number ('q' or 'й' - quit) \n"))
    if digit == 'q' or digit == 'й' :
        print('Bye, Bye!')
        break
    else:
        check = True if digit.isdigit() else False
        if check == False:
            print("---------Enter the integer!!!--------")
        else:
            digit =  int(digit)
            for el in range(len(my_list)):
                if my_list[el] == digit:
                    my_list.insert(el + 1, digit)
                    break
                elif my_list[0] < digit:
                    my_list.insert(0, digit)
                elif my_list[-1] > digit:
                    my_list.append(digit)
                elif my_list[el] > digit and my_list[el + 1] < digit:
                    my_list.insert(el + 1, digit)
            print(f"Current list - {my_list}")
# -------------------------------------------------------------------------------------------------5------------------------------------------------------------------------------------------------------------------
# Реализовать структуру данных «Товары». Она должна представлять
# собой список кортежей. Каждый кортеж хранит информацию об
# отдельном товаре. В кортеже должно быть два элемента —
# номер товара и словарь с параметрами (характеристиками товара:
# название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е.
# запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
#     (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#     (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#     (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь,
# в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик,
# например список названий товаров.
# Пример:
# {
#     “название”: [“компьютер”, “принтер”, “сканер”],
#     “цена”: [20000, 6000, 2000],
#     “количество”: [5, 2, 7],
#     “ед”: [“шт.”]
# }

goods = []
features = {'name': '', 'price': '', 'quantity': '', 'unit': ''}
analytics = {'name': [], 'price': [], 'quantity': [], 'unit': []}
num = 0
feature_ = None
control = None
while True:
    control = input("For quit type 'Q', for continue press 'Enter', for analytics type 'A'").upper()
    if control == 'Q':
        break
    num += 1
    if control == 'A':
        print(f'\n Current analytics \n {"-" * 20}')
        for key, value in analytics.items():
            print(f'{key[:15]:>20}: {value}')
            print("-" * 20)
    for f in features.keys():
        feature_ = input(f'Input feature "{f}"')
        features[f] = int(feature_) if (f == 'price' or f == 'quantity') else feature_
        analytics[f].append(features[f])
    goods.append((num, features))
# ----------------------------------------------------------------------------------------------Дополнение------------------------------------------------------------------------------------------------------------
goods = int(input("Type count of thing "))
n = 1
my_dict = []
my_list = []
my_analys = {}
while n <= goods:
    my_dict = dict({'Name': input("Type name "), 'Price': input("Enter the price "),
                    'Count': input('Type count '), 'QTY': input("Type measure unit ")})
    my_list.append((n, my_dict))
    n += 1
    my_analys = dict(
        {'Name': my_dict.get('Name'), 'Price': my_dict.get('Price'), 'Count': my_dict.get('Count'),
         'QTY': my_dict.get('QTY')})
for el in my_list:
    print(el)
print(my_analys)
