#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    wrong_word = 'роцессорп'

    # Take last 3 symbols
    last_part = wrong_word[-3:]

    # Revers of received characters
    last_part_rev = last_part[::-1]

    # Printing 3 symbols and right part of the word without last symbol
    print(f'Right word: {last_part_rev}{wrong_word[2:-1]}')
