def print_params(a=1, b="строка",c=True): #ринимющая функция со значениями по умолчанию
    print("Параметр а:",a)
    print("Параметр b:",b)
    print("Параметр c:",c)

print("\033[4m 1 часть ДЗ - Функция с параметрами по умолчанию \033[0m")

print("Вывод параметров функции 'print_params' без аргументов:")
print_params()
print()

print("Вывод параметров функции 'print_params' с аргументом a=10:")
print_params(a=10)
print()

print("Вывод параметров функции 'print_params' с двумя аргументами a=10, b='банан':")
print_params(a=10,b="банан")
print()

print("Вывод параметров функции 'print_params' с тремя аргументами a=10, b='банан', с=False:")
print_params(a=10,b="банан",c=False)
print()

print("Проверка вызова print_params(b = 25) print_params(c = [1,2,3])")
print_params(b=25,c=[1,2,3])
print('Результат проверки: вызов работает, тип данных аргумента по умолчанию можно изменять')
print()

print("\033[4m 2 часть ДЗ - Распаковка параметров \033[0m")

print('Вывод параметров функции "print_params" с распаковкой параметров из списка values_list')
values_list=[True, 666, "1типстрока"]    #список
print_params(*values_list)
print()

print("Вывод параметров функции 'print_params' с распаковкой параметров из словаря values_dict")
values_dict ={'a': True, 'b': 666, 'c': "1типстрока"}   #словарь
print_params(**values_dict)
print()

print("\033[4m 3 часть ДЗ - Распаковка+отдельные параметры \033[0m")
print("Проверка работы print_params(*values_list_2, 42) - сочетания распаковки и отдельного парметра")
values_list_2=['1значение',999]
print_params(*values_list_2,42)
print('Результат проверки: функции можно передавать сочетание распакованных и отдельных параметров в качестве аргументов')
