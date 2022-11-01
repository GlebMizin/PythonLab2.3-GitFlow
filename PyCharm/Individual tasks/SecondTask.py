#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    sentence = str(input("Enter your sentence: "))
    sen_list = list(sentence)

    for i in range(len(sentence)-2):

        # Checking 3 symbols one by one
        if sen_list[i] == "п" and sen_list[i+1] == "р" and sen_list[i+2] == "о":
            sen_list[i] = "н"
            sen_list[i+1] = "е"
            sen_list[i+2] = "т"

    # Connecting parts of list to string
    new_sentence = "".join(sen_list)
    print(new_sentence)
