#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main():
    num = 1
    while True:
        message = int(input("Введите число: "))
        num *= message
        if num == 0:
            print('Произведение равно 0')
            break
        else:
            print(f'Произведение равно: {num}')


if __name__ == '__main__':
    main()
