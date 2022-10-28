#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    MinWordLen = float('inf')

    # List of punctuation marks
    PunctMarks = [' ', ',', '-', ';', ':', '?', '!', '.']
    Counter = 0

    UserStr = str(input("Enter your sentence: "))
    StrList = list(UserStr)

    # Loop through all characters of the input string
    for i in range(len(StrList)):

        # Checking if a symbol is a punctuation mark
        if StrList[i] in PunctMarks:
            WordLen = Counter
            Counter = 0

            # Determine the minimum length of a word
            if 0 < WordLen < MinWordLen:
                MinWordLen = WordLen
        else:
            Counter += 1

    # Checking the last word, in case of a forgotten dot at the end
    WordLen = Counter
    if 0 < WordLen < MinWordLen:
        MinWordLen = WordLen

    print(MinWordLen)
