cars = ["BMW","MB","LADA","KIA","HONDA"]
cars_count = 0
shag=0
for i in cars:
    shag+=1
    print("Шаг №:",shag)
    print("Я езжу на автомабиле марки:",i)
    if shag >=2:
        cars_count+=10
    print("Значение переменной cars_count=",cars_count)
    print()

