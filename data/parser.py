import numpy as np

# Categories from command-line:
# cut -f 2 news_tagged_data.txt | sort | uniq
CATEGORIES={
    'B-KEYWORDS':0,
    'B-NEWSTYPE':1,
    'B-PROVIDER':2,
    'B-SECTION':3,
    'I-KEYWORDS':4,
    'I-NEWSTYPE':5,
    'I-PROVIDER':6,
    'I-SECTION':7,
    'O':8
}

class Parser(object):
    def __init__(self, filename):
        self.filename = filename

    def parse(self):
        X = [[]]
        Y = [[]]
        n_sentence = 0
        i = 0
        with open(self.filename, 'r') as f:
            for line in f:
                if line not in ['\n', '\r\n']:
                    x, y = line.split("\t",1)
                    X[n_sentence].append(x)
                    Y[n_sentence].append(CATEGORIES[y[:-1]])
                else:
                    n_sentence += 1
                    X.append([])
                    Y.append([])
        del X[-1]
        del Y[-1]

        print("len(X) = {}".format(len(X)))
        print("len(Y) = {}".format(len(Y)))

        return X, Y
