#!/usr/bin/python
import os, sys
from data.parser import Parser

sys.path.append(os.path.dirname(__file__))

data_filename='news_tagged_data.txt'

if __name__ == "__main__":
    parser = Parser(data_filename)
    X,Y = parser.parse()
    print X
    print Y

