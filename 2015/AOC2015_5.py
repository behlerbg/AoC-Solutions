#! python3
## AOC2015_5.py
## Advent of Code challenge 5: naughty v nice
## Brett Behler 12.29.2018

import re

def get_file():
    with open('2015ChallengeInput5.txt', 'r') as strings:
        return naughty_nice_pt2(strings)

def naughty_nice_pt1(fname):
    '''(file) -> (int)

    Evaluates fname line by line with three regular expressions. Returns number of lines that match the the specified expressions.
    '''
    # contains at least 3 vowels
    regex_vowels = re.compile(r'(.*[aeiouAEIOU]){3}')
    
    # has any repeating character
    regex_double = re.compile(r'(.)\1')
    
    # includes either ab, cd, pq, and/or xy
    regex_exclude = re.compile(r'ab|cd|pq|xy')
    
    nice_strings = 0

    for line in fname:
        three_vowels = re.search(regex_vowels, line)
        double_letter = re.search(regex_double, line)
        excluded_pair = re.search(regex_exclude, line)
        if three_vowels and double_letter and not excluded_pair:
            nice_strings += 1
    
    return nice_strings

def naughty_nice_pt2(fname):
    
    nice_strings = 0

    # contains two of the same double characters without overlapping
    regex_doubles = re.compile(r'(..).*\1')

    # contains a character that repeats with exactly one character in between
    regex_between = re.compile(r'(.).\1')

    for line in fname:
        doubles = re.search(regex_doubles, line)
        one_between = re.search(regex_between, line)

        if doubles and one_between:
            nice_strings += 1

    return nice_strings

if __name__ == '__main__':
    print(get_file())
