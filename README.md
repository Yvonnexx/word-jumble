word jumble
===========

word jumble is a program which accept a string as input and then return a list of words that can be created using the submitted letters.
For example, on the input 'dog', the program should return a set of words including 'god', 'do', and 'go'.

# Softwares To Install

## Python 2.7

# How to run

* type in the command line in a terminal

    ``` python

        ./jumble.py
        
        'input a word'

        'dog'

        'word jumble for this word is :'

        ['do', 'god', 'go']

    ``` 

# File description

## dict.txt
This file is generate using the SCOWL (Spell Checker Oriented Word Lists) link http://wordlist.aspell.net/
This file contains a word dictionary.

## jumble.py
This file is the program which accept a string input and return the list of words jumbled from the input string.

* function generateDict()

This function loads all the words from a txt dictionay file and store all the words in a dictionary.

* function generate_substr(word)

This function generate all the substring of the input string and return it as a list

* function permutation(substr)

This function return all the permutation of an input string

* function find_jumble(word)

This fucntion return all the jumble for the input word
