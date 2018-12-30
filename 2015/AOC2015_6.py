#! python3
## AOC2015_6.py
## Advent of Code challenge 6. Light show
## Brett Behler 12.30.2018

import re

class LightController(object):
    '''A class for controlling a list of Light objects'''
    def __init__(self, columns, rows):
        self.lights = {}
        self.position_regex = re.compile(r'\d+,\d+')
        self.command_regex = re.compile(r'turn on|turn off|toggle')
        for x in range(columns):
            for y in range(rows):
                self.lights[(x,y)] = Dimmable()
    
    def __str__(self):
        lit = 0
        brightness = 0
        for light in self.lights.values():
            if light.is_on:
                lit += 1
                if isinstance(light, Dimmable):
                    brightness += light.brightness
        return str(lit) + ' lights are on. With a brightness of ' + str(brightness)
    
    def get_command(self, line):
        begin, end = re.findall(self.position_regex, line)
        begin = [int(num) for num in begin.split(',')]
        end = [int(num) for num in end.split(',')]
        command = re.search(self.command_regex, line).group()
        self.send_command(begin, end, command)

    def send_command(self, begin, end, command):
        for x in range(begin[0], end[0] + 1):
            for y in range(begin[1], end[1] + 1):
                self.lights[(x,y)].switch(command)

class Light(object):
    '''A class for simulating a light. Can be turned on, turned off, or toggled.'''
    def __init__(self):
        self.is_on = False

    def switch(self, command):
        if command == 'turn on':
            self.is_on = True
        elif command == 'turn off':
            self.is_on = False
        elif command == 'toggle':
            self.is_on = not self.is_on

class Dimmable(object):
    '''A class for simulating a dimmable light.'''
    def __init__(self):
        self.brightness = 0
        self.is_on = False

    def set_is_on(self):
        if self.brightness == 0:
            self.is_on = False
        else:
            self.is_on = True

    def switch(self, command):
        if command == 'turn on':
            self.brightness += 1
        elif command == 'turn off' and self.brightness != 0:
            self.brightness -= 1
        elif command == 'toggle':
            self.brightness += 2
        self.set_is_on()

def main():
    Controller = LightController(1000, 1000)
    with open('2015ChallengeInput6.txt', 'r') as instructions:
        for line in instructions:
            Controller.get_command(line)
    print(Controller)

if __name__ == '__main__':
    main()
    input('Press enter key to exit.')
