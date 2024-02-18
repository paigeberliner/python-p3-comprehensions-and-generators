#!/usr/bin/env python3

def return_evens(num_list):
    even_numbers = []
    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)

    return even_numbers

def make_exclamation(sentence_list):
    modified_list = []
    for sentence in sentence_list:
        modified_sentence = sentence + "!"
        modified_list.append(modified_sentence)

    return modified_list