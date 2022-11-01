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

    str_to_list = list(text)

    # Counting symbols "+" and "*"
    plus_counter = str_to_list.count("+")
    multi_counter = str_to_list.count("*")

    # Output, with f lines
    print(f'Number of "+" is: {plus_counter} \n'
          f'Number of "*" is: {multi_counter}')
