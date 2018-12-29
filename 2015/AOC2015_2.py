#! python3
## AOC2015_2.py
## Advent of Code 2015 puzzle #2 - total surface area
## Brett Behler 12.28.2018

def paper_order():
    with open('2015ChallengeInput2.txt', 'r') as gifts:
        total_paper = 0
        total_ribbon = 0
        for dimensions in gifts:
            dimensions = [int(side) for side in dimensions.split('x')]
            ribbon = (sum(dimensions) - max(dimensions)) * 2
            sur_area = []
            prod = 1
            for i in range(0, -len(dimensions), -1):
                prod *= dimensions[i]
                sur_area.append(dimensions[i] * dimensions[i - 1])
            total_paper += (sum(sur_area) * 2) + min(sur_area)
            total_ribbon += ribbon + prod
        return total_paper, total_ribbon
        
if __name__ == '__main__':
    print(paper_order())
