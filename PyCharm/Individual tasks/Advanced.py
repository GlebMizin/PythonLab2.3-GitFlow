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
        Counter += 1

        # Checking if a symbol is a punctuation mark
        for j in range(len(PunctMarks)):
            if StrList[i] == PunctMarks[j]:
                WordLen = Counter - 1

                # Determine the minimum length of a word
                if 0 < WordLen < MinWordLen:
                    MinWordLen = WordLen
                    Counter = 0
                Counter = 0
                break

    # Checking the last word, in case of a forgotten dot at the end
    WordLen = Counter
    if 0 < WordLen < MinWordLen:
        MinWordLen = WordLen

    print(MinWordLen)
