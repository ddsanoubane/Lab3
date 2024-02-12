#!/usr/bin/env python3
#Description of Function: A function that will write a text file to your PC with your name.

import os

def text_file():
    name = input('Enter your name: ')
    file = name + '.txt'

    f = open(file, 'w')
    f.close

text_file()

