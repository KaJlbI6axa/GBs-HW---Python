'''
Реализовать функцию, принимающую два числа
(позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.
'''
def division(a,b):
    try:
        c = (float(a) / float(b))
        return c
    except (ValueError, TypeError, ZeroDivisionError):
        print('Error. So u get', end= ' ')

print(f"Result  -  [{division(input('Enter frist number    '),input('Enter second number    '))}]")
print("-" * 50)
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать
параметры как именованные аргументы. Реализовать вывод данных
о пользователе одной строкой.
'''
def urself(name, surname, year, city, email, number):
     return ' | '.join([name, surname, year, city, email, number])
print(urself(name = 'Ilya',surname = 'Barabanshchikov',  year = '1998', city = 'Moscow', email = 'ILuvBigBoobs@ya.ru', number = '8-800-555-35-35'), sep = '//')
print("-" * 50)
#  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
Реализовать функцию my_func(), которая принимает три позиционных
аргумента, и возвращает сумму наибольших двух аргументов.
'''
def my_func(a,b,c):
    try:
        b = [a, b, c]
        b.remove(min(b))
        result = float(b[0]) + float(b[1])
        return result
    except (ValueError, TypeError):
        print('Error. So u get', end= ' ')

print(f'Result  -  [{my_func(a = (input("Enter frist number    ")),b = (input("Enter second number    ")), c = (input("Enter third number    ")))}]')
print("-" * 50)
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
Программа принимает действительное положительное число x
и целое отрицательное число y. Необходимо выполнить возведение
числа x в степень y. Задание необходимо реализовать в виде функции
my_func(x, y). При решении задания необходимо обойтись без встроенной
функции возведения числа в степень.
'''
def division(x,y):
    try:
        # return float(x) ** (-float(y)) - можно и так 
        return 1 / float(x) ** float(y)
    except (ValueError, TypeError):
        print('Error. So u get', end= ' ')

print(f"Result  -  [{division(input('Enter X:   '),input('Enter Y:   '))}]")
print("-" * 50)
#  -----------------------------------------------------------------------------------------Вариант решения------------------------------------------------------------------------------------------------------------
def division(x,y):
    try:
        x = float(x)
        y = float(y)
        if  y < 0:
            r = float(1)
            while (y < 0):
                r = r * x
                y = y + 1
            print(f'Result - [{1/r}]')
        else:
            r = float(1)
            while (y > 0):
                r = r * x
                y = y - 1
            print(f'Result - [{1/r}]')
       
    except (ValueError, TypeError):
        print('Error. So... u get nothing. U LOSE!')

division(input('Enter X:   '),input('Enter Y:   '))
print("-" * 50)
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
Программа запрашивает у пользователя строку чисел, разделенных
 пробелом. При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и
снова нажать Enter. Сумма вновь введенных чисел будет добавляться
к уже подсчитанной сумме. Но если вместо числа вводится специальный
символ, выполнение программы завершается. Если специальный символ
введен после нескольких чисел, то вначале нужно добавить сумму этих
чисел к полученной ранее сумме и после этого завершить программу.
'''

def my_sum ():
    sumResult = 0
    ex = False
    while ex == False:
        userNumbers = input('Enter a string of numbers.\nType"Q" for quit.\n').split()

        res = 0
        for el in range(len(userNumbers)):
            if userNumbers[el] == 'q' or userNumbers[el] == 'Q' or userNumbers[el] == 'й' or userNumbers[el] == 'Й':
                ex = True
                break
            else:
                res = res + float(userNumbers[el])
        sumResult = sumResult + res
        print(f'Current sum is {sumResult}')
    print(f'Ur final sum is {sumResult}')

my_sum() 
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
Реализовать функцию int_func(), принимающую слово из маленьких
латинских букв и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать
строка из слов, разделенных пробелом. Каждое слово состоит
из латинских букв в нижнем регистре. Сделать вывод исходной
строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().

a = "testтёст"
if re.search(r'[^a-zA-Zа-яА-ЯёЁйЙ]',a ):
     print("error")
else:
     print("ok")
'''
import re
int_func = (lambda userText: print("Error. Make sure that u type A-z") if re.search(r'[^a-z]',userText) else print(userText.title()))(userText = input("Type ur text:     ").lower())

#  -----------------------------------------------------------------------------------------Вариант решения------------------------------------------------------------------------------------------------------------

''' У меня лямбда работающая, я ХЗ как впихнуть ее в другую функцию. Там требует чтобы все было приведено к INT или SLICES, а не строковое. Буду признателен, если поможете

import re
userStr = input("Enter ur string:\n")
my_word = []
num = 1
for el in range(userStr.count(' ') + 1):
    my_word = userStr.split()
for el in range(my_word):
    int_func = (lambda element: print("Error. Make sure that u type A-z") if re.search(r'[^a-z]',element) else print(element.title()))(my_word[el]).lower()

'''
# рабочая, сделал иначе
def my_func(text):
    separate_word = text.split(' ')
    if re.search(r'[^a-z\s+]',text):
        print("Error. Make sure that u type A-z")
    else:
        wordsList = []
        for i in separate_word:
            string_element = str(i)
            word = string_element.title()
            wordsList.append(word)
        return wordsList
print(my_func(input("Type ur text        ").lower()))