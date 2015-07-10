#!/usr/bin/python
from data.parser import Parser

data_filename='news_tagged_data.txt'

if __name__ == "__main__":
    parser = Parser(data_filename)
    X,Y = parser.parse()

