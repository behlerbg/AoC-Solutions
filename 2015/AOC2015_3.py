#! python3
## AOC2015_3.py
## Infinite 2d house grid
## Brett Behler 12.28.2018

def get_directions():
    with open('2015ChallengeInput3.txt', 'r') as directions:
        return directions.read()

def eval_directions(directions):
    # Santa's and robot's x, y coordinate values.
    s_x = 0
    s_y = 0
    r_x = 0
    r_y = 0
    
    visited = [(0, 0)]
    santa = False
    
    for char in directions:
        santa = not santa

        # determine if tracking robot or Santa
        if santa:
            x = s_x
            y = s_y
        else:
            x = r_x
            y = r_y

        # update current coordinate
        if char == '^':
            y += 1
        elif char == 'v':
            y -= 1
        elif char == '<':
            x -= 1
        elif char == '>':
            x += 1
        cur_house = (x, y)

        # update Santa or robot position
        if santa:
            s_x, s_y = cur_house
        else:
            r_x, r_y = cur_house
            
        if cur_house not in visited:
            visited.append(cur_house)
            
    return len(visited)

if __name__ == '__main__':
    print(eval_directions(get_directions()))
