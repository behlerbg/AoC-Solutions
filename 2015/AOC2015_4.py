#! python3
## AOC2015_4.py
## Advent of Code challenge 4: md5 hashes
## Brett Behler 12.29.2018

import hashlib

def get_lowest_value_5(key):
    hexi = ''
    count = 0
    while not hexi[:5] == '00000':        
        hash_md5 = hashlib.md5()
        count += 1
        hash_md5.update((key + str(count)).encode('ASCII'))
        hexi = hash_md5.hexdigest()
    return count

def get_lowest_value_6(key):
    hexi = ''
    count = 0
    while not hexi[:6] == '000000':        
        hash_md5 = hashlib.md5()
        count += 1
        hash_md5.update((key + str(count)).encode('ASCII'))
        hexi = hash_md5.hexdigest()
    return count

if __name__ == '__main__':
    key = 'iwrupvqb'
    print(get_lowest_value_5(key))
    print(get_lowest_value_6(key))
