#!/usr/bin/python

def generateDict():
    # @return a dictionary with words

    dict = set([])
    with open ('dict.txt') as f:
        for word in f:
            dict.add(word.rstrip('\r\n'))
    return dict

def generate_substr(word):
    # @input is a string of word
    # @output is a list which has all the substrings of the input word

    substr = []
    for i in xrange(len(word)):
        for j in xrange(i+1, len(word)+1):
            substr.append(word[i:j])
    return substr

def permutation(substr):
    # @input a string
    # @return all permutations of the input string
    if len(substr) <= 1:
        yield substr
    else:
        for item in permutation(substr[1:]):
            for i in range(len(item)+1):
                yield item[:i]+substr[0:1]+item[i:]

def find_jumble(word):
    # @input a word
    # @return the jumble of this word
    res = []
    dict = generateDict()
    substr = generate_substr(word)
    for sub in substr:
        for item in permutation(sub):
            if item in dict and item != word:
                print item
                res.append(item)
    return res

if __name__ == "__main__":
    print 'input a word'
    word = raw_input()
    print 'word jumble for this word is:'
    print find_jumble(word)
