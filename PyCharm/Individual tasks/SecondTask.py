#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    Sentence = str(input("Enter your sentence: "))
    Sen_List = list(Sentence)

    for i in range(len(Sentence)-2):

        # Checking 3 symbols one by one
        if Sen_List[i] == "п" and Sen_List[i+1] == "р" and Sen_List[i+2] == "о":
            Sen_List[i] = "н"
            Sen_List[i+1] = "е"
            Sen_List[i+2] = "т"

    # Connecting parts of list to string
    NewSentence = "".join(Sen_List)
    print(NewSentence)
