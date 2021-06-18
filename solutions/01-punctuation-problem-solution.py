

'''
Problem Description
Write method to remove punctuation symbols from the string

Sample Input
str = 'th!s i$s s$amp~^le s&t#ring'

Expected Output
res = 'this is sample string'

'''

# solution code
import re


def solution(words):
    word_list = []
    symbols = ['_']
    for word in words:
        # remove punctuations from word
        new_word = re.sub(r'[^\w\s]', '', word)
        # check for underscore character
        match = re.search(r'\_', new_word)
        # if found then remove it
        if match:
            for symbol in symbols:
                new_word = new_word.replace(symbol, '')

        # append new word to word list
        word_list.append(new_word)

    # return word list
    return word_list


if __name__ == "__main__":
    words = ["d(on)'t", "k@@\ee*%p", "pa$$/ss^wor#d", "l{ike}", "t-_h-is?"]
    result = solution(words)
    print(result)