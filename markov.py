"""
This is a module docstring

This is the Markov module, useful for creating
Markov chains.

>>> m = Markov('ab')  # create an instance
>>> m.predict('a')    # call a method
'b'

      >>> get_table('ab')
      {'a': {'b': 1}}

"""

import argparse
import random
import sys


def adder(x, y):
    """Returns x + y
 >>> adder(4, 5)
 9
    """
    return x + y


def get_table(line, numchars=1, word=False):
    """
    line - string (for character mode default)
    line - list of strings (for word = True)
    >>> get_table('matt')
    {'m': {'a': 1}, 'a': {'t': 1}, 't': {'t': 1}}

    >>> get_table('find a city'.split(), word=True)
    {'find': {'a': 1}, 'a': {'city': 1}}
    """
    results = {} # dictionary literal
    for i, _ in enumerate(line):
        chars = line[i:i+numchars]
        if word: # if isinstance(line, list)
            chars = ' '.join(chars)
        try:
            out = line[i+numchars]
        except IndexError:
            break
        char_dict = results.get(chars, {})
        char_dict.setdefault(out, 0)
        char_dict[out] += 1
        results[chars] = char_dict
    return results

# a class is like a factory
# instances come into the
# constructor, and are
# specialized

class Markov:
    """
    Defines a Markov class
    """
    # language is a class attribute
    language = 'English'
    word = False
    
    # This is a constructor
    def __init__(self, txt, size=1):
        # In a constructor
        # we customize the instance
        # data
        # Instance attributes
        self.tables = []
        for i in range(size):
            self.tables.append(
                get_table(txt, i+1,
                          word=self.word))
        self.size = size

    def _get_table(self, data_in):
        if len(data_in) > self.size:
            data_in = data_in[-self.size:]
        table = self.tables[len(data_in)-1]
        return table
    
    def predict(self, data_in):
        table = self._get_table(data_in)
        options = table.get(data_in, {})
        if not options:
            raise KeyError('{} is missing'.format(data_in))
        possible = []
        for key, count in options.items():
            #possible += key*count
            possible.extend([key]*count)
        result = random.choice(possible)
        return result


class WordMarkov(Markov):
    word = True
    
    def _get_table(self, data_in):
        # try to see if data_in is
        # in the tables in reverse
        for table in reversed(self.tables):
            if data_in in table:
                break
        return table
    
    
def test_predict(m, num_chars, start, size=1):
    res = [start]
    for i in range(num_chars):
        let = m.predict(start)
        res.append(let)
        #start = let
        start = ''.join(res[-size:])
    return ''.join(res)


def fetch_url(url, fname):
    import urllib.request as req
    fin = req.urlopen(url)
    data = fin.read()
    with open(fname, 'wb') as fout:
        fout.write(data)


def repl(m):
    while True:
        try:
            txt = input('>')
        except EOFError:
            print("Goodbye!")
            break
        res = m.predict(txt)
        print(res)
        

def main(args):
    p = argparse.ArgumentParser(
        description='Create a markov repl')
    p.add_argument('-f', '--file', help="Input file")
    p.add_argument('-s', '--size', help='Markov size default(1)',
                   default=1, type=int)
    p.add_argument('-w', '--word-mode', help='Word mode rather'
                   ' than char mode', action='store_true')
    opts = p.parse_args(args)
    if opts.file:
        with open(opts.file) as fin:
            data = fin.read()
        klass = Markov
        if opts.word_mode:
            klass = WordMarkov
            data = data.split()
        m = klass(data, size=opts.size)
        repl(m)
        
    
#m = Markov('ab')
if __name__ == '__main__':
    print(sys.argv)
    main(sys.argv[1:])
    #import doctest
    #doctest.testmod()
    
##    with open('ts.txt', encoding='utf8') as fin:
##        data = fin.read()
##    m = Markov(data, size=4)
##    url = 'https://www.gutenberg.org/files/74/74-0.txt'
    wm = WordMarkov('find a city, find yourself'.split(),
                    size=4)

