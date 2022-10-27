#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    WrongWord = 'роцессорп'

    # Take last 3 symbols
    LastPart = WrongWord[-3:]

    # Revers of received characters
    LastPartR = LastPart[::-1]

    # Printing 3 symbols and right part of the word without last symbol
    print(f'Right word: {LastPartR}{WrongWord[2:-1]}')
