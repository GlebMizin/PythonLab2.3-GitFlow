#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    text = ""
    PlusCounter = 0
    MultiCounter = 0
    print("Print your text: ")

    # Multiline Input
    while True:
        x = input()
        if x:
            text += x + " "
        else:
            break

    TextToList = list(text)

    # Counting symbols "+" and "*"
    for i in range(len(text)-1):
        if TextToList[i] == "+":
            PlusCounter += 1
        elif TextToList[i] == "*":
            MultiCounter += 1

    # Output, with f lines
    print(f'Number of "+" is: {PlusCounter} \n'
          f'Number of "*" is: {MultiCounter}')
