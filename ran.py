from random import randint
from pprint import pprint

with open('stats.txt', 'r+') as f:
    answers = dict()
    for line in f:
        # удаляем начальные пробелы слева в первой строке
        name, count = line.lstrip().split()
        answers.update({name: int(count)})
    yourName = input("Введите ваше имя: ")
    print(yourName + ", новичкам везёт!!!")
    pprint("Текущая статистика игры: " + str(answers))
    a, b = 1, 10
    randNumber = randint(a, b)
    print("Компьютер загадал число в диапазоне от {0} до {1}".format(a, b))
    print("У вас есть 3 попытки удачи")
    n = 0
    # флаг угадали ли мы
    y = False
    while n < 3:
        try:
            num = int(input("Введите число в диапазоне от {0} до {1}: ".format(a, b)))
        except Exception as e:
            print("Вы ввели не число!!!!")
            continue

        if num > randNumber:
            print("Число больше")
        elif num < randNumber:
            print("Число меньше")
        else:
            y = True
            print("Вы угадали")
            print("Игра окончена!!!!")
            answers.update({yourName: n+1})
            break
        n += 1
    if not y:
        print("Игра окончена!!!!")
        print("Вы не угадали")
    else:
        # очищаем содержимое, если угадали
        f.truncate(0)
        ansItems = sorted(answers.items(), key=lambda x: x[1])
        for name, count in ansItems[:3]:
            ans = str(name + " " + str(count) + "\n")
            f.write(ans)
        pprint("Обновленная статистика по игре: " + str([{name:count} for name, count in ansItems[:3]]))
        print("Рейтинг игры")
        i = 1
        for name, count in ansItems[:3]:
            print("место: {0} имя игрока: {1} количество попыток: {2}".format(i, name, count))
            i += 1
