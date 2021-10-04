#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def cylinder():
    radius = int(input('Введите радиус цилиндра: '))
    height = int(input('Введите высоту цилиндра: '))

    def circle():
        print('Площадь полной поверхности цилиндра: ',
              2 * 3.14 * radius * height + 2 * 3.14 * radius ** 2)
    print('Какую площадь нужно получить?')
    print('Площадь боковой поверхности? - 1')
    print('Площадь полной поверхности цилиндра? - 2')
    message = input('>>> ')
    if message.lower() == '1':
        print('Площадь боковой повехности: ', 2 * 3.14 * radius * height)
    elif message.lower() == '2':
        circle()
    else:
        print('Неизвестная команда')


if __name__ == '__main__':
    cylinder()
