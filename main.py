#!/usr/bin/env python3
# coding=utf-8

import random


# функция для получения массива случайных чисел
def random_array(n, m=8, max_value=10):
    array = []  # основной массив
    for i in range(0, n):
        sub_array = []  # подмассив с числами
        for j in range(m):
            # от минимального числа (-10) до максимального -1 (max_value - 1 = 20) с шагом (1)
            k = random.choice([True, False])
            if k == True:
                number = random.uniform(0, max_value)
                sub_array.append(number)
            else:
                number = random.randint(0, max_value)
                sub_array.append(number)

        array.append(sub_array)  # добавление подмассива в массив
    return array  # возвращается массив с подмассивами внутри


# функция для вывода массива
def print_array(array):
    print()
    for i in array:  # перебор по подмассивам(строкам)
        for j in i:  # перебор по элементам строк
            print("%5.1f\t" % j, end='')
        print()


# функция для нахождения элементов условия (в этом случае максимум и минимум,
# может быть количество нулей, количество отрицательных чисел и т.д.)
def counting(array):
    print()
    # как начальное значение для макс/мин берется первый элемент массива
    zero = 0
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == 0:
                zero += 1
                return zero
    return zero


def main():
    rowCount = 4
    colCount = 5
    # вызов функции рандома массива, которая возвращает полученный массив
    array = random_array(rowCount, colCount)  # можно изменить размер
    print("Условие задания:\n"
          "Определить, имеется ли в таблице хотя бы один нулевой элемент.\n"
          "Если такой элемент есть, то заменить все\n"
          "вещественные значения таблицы единицами")
    # вызов функции вывода массива
    print_array(array)
    # вызов функции массива по условию, который возвращает элементы для проверки условия
    zero = counting(array)
    while True:
        print("1. Заполнить массив случайными числами;")
        print("2. Выполнить задание;")
        print("3. Выход.")
        key = input('Введите команду (1, 2, 3 или 4): ')
        if key == '1':  # рандом, вывод и новые значения по условию нового массива
            array = random_array(rowCount, colCount)
            print_array(array)
            zero = counting(array)
        elif key == '2':
            # проверка выполнения условия
            if zero == 0:
                print("Нет нулевого элемента")
            else:
                # выполнения результата совпадения условия,
                # в данном случае макс * 2, а мин / 2
                for i in range(len(array)):  # перебор каждую строку
                    for j in range(len(array[i])):  # цикл нужен, так как макс/мин не одни в массиве
                        try:
                            number = array[i][j]
                            if not isinstance(number, int):
                                array[i][j] = 1
                        except ValueError:
                            break

                print("Все вещественные значения таблицы стали единицами")
                print_array(array)
                break  # выход из цикла
        elif key == '3':
            exit(0)  # выход из программы


if __name__ == '__main__':
    main()
