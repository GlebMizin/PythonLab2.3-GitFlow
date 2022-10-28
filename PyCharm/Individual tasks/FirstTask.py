#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    text = ""
    print("Print your text: ")

    # Multiline Input
    while True:
        x = input()
        if x:
            text += x + " "
        else:
            break

    StrToList = list(text)

    # Counting symbols "+" and "*"
    PlusCounter = StrToList.count("+")
    MultiCounter = StrToList.count("*")

    # Output, with f lines
    print(f'Number of "+" is: {PlusCounter} \n'
          f'Number of "*" is: {MultiCounter}')
