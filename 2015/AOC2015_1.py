#! python3
## AOC2015_1.py
## Advent of Code 2015 puzzle #1 - "(" == up ")" == down
## Brett Behler 12.28.2018

def get_directions():
    with open('2015ChallengeInput1.txt', 'r') as instruct:
        return instruct.read()

def eval_directions(directions):
    cur_floor = 0
    enter_basement = 0
    i = 0
    for char in directions:
        i += 1
        if char == '(':
            cur_floor += 1
        elif char == ')':
            cur_floor -= 1
        if cur_floor < 0 and not enter_basement:
            enter_basement = i
    return cur_floor, enter_basement


if __name__ == '__main__':
    print(eval_directions(get_directions()))
