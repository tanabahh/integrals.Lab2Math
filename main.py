from method import LeftRectangles, RightRectangles, CenterRectangles
from functions import f, z, g, c, s, q


def input_float():
    try:
        e = float(input().replace(',', '.'))
        return e
    except ValueError:
        print("Вы ввели не число, попробуйте еще раз")
        return "*"


print("Введите номер функции (x - 1, sqrt(x) - 2, sin(x) - 3, lnx - 4, x/abs(x) - 5)")
index = int(input())
if index == 1:
    function = f
elif index == 2:
    function = z
elif index == 3:
    function = s
elif index == 4:
    function = c
elif index == 5:
    function = q
else:
    function = g
    print("Поздравляю вы открыли пасхалку, ваша функция - 1/x")

print("Введите верхнюю границу: ")
b = input_float()
while b == "*":
    b = input_float()
print("Введите нижюю границу: ")
a = input_float()
while a == "*":
    a = input_float()
print("Введите точность: ")
e = input_float()
while (e == "*") or (e <= 0.00000001):
    print("Введите точность еще раз, это должно быть положительное число больше 0.00000001: ")
    e = input_float()
if b < a:
    t = a
    a = b
    b = t

if (index == 4) and (a == 0):
    print("На этом промежутке интаграл не определен, но мы попробуем посчитать примерно")


left = LeftRectangles(function, a, b, e)
right = RightRectangles(function, a, b, e)
center = CenterRectangles(function, a, b, e)
left_list = left.get_answer_and_count()
right_list = right.get_answer_and_count()
center_list = center.get_answer_and_count()
if type(left_list) == list and type(right_list) == list and type(center_list) == list:
    if left_list[1] > 4000000:
        print("Точность для левых прямоугольников недосягаема")
    else:
        print("\nОтвет для левых прямоугольников:", left_list[0], "\nКоличество разбиений:", left_list[1],
              "\nПогрешность интегрирования: ", left_list[2])
    if right_list[1] > 4000000:
        print("Точность для правых прямоугольников недосягаема")
    else:
        print("\nОтвет для правых прямоугольников:", right_list[0], "\nКоличество разбиений:", right_list[1],
              "\nПогрешность интегрирования: ", right_list[2])
    if center_list[1] > 4000000:
        print("Точность для средних прямоугольников недосягаема")
    else:
        print("\nОтвет для средних прямоугольников:", center_list[0], "\nКоличество разбиений:", center_list[1],
              "\nПогрешность интегрирования: ", center_list[2])
else:
    print("Ошибка в границах, скорее всего не выполнеятся необходимое условие существования интеграла")
