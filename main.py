import keyboard
import time
from os import system
class Game:
    def __init__(self):
        self.map = []

    def Map(self, lenght=None):
        self.map = [["."] * 30 for i in range(2)]
        return self.map


if __name__ == '__main__':
    Games = Game()
    line = Games.Map()
    start_p = 0
    line[1][start_p] = '$'
    for iteration in line:
        for elem in iteration:
            print(elem, end='')
        print('')

    while True:
        if keyboard.is_pressed('d'):
            system('cls')

            start_p += 1
            if start_p == 30:
                start_p = 0
                
            line[1][start_p] = '$'
            line[1][start_p-1] = '.'

            for iteration in line:
                for elem in iteration:
                    print(elem, end='')
                print('')

            time.sleep(0.1)

        if keyboard.is_pressed('a'):
            system('cls')
            start_p -= 1
            line[1][start_p] = '$'
            line[1][start_p+1] = '.'

            for iteration in line:
                for elem in iteration:
                    print(elem, end='')
                print('')

            time.sleep(0.1)

        if keyboard.is_pressed('space'):
            system('cls')

            line[0][start_p] = '$'
            line[1][start_p] = '.'
            for iteration in line:
                for elem in iteration:
                    print(elem, end='')
                print('')

            time.sleep(0.5)
            system('cls')
            line[0][start_p] = '.'
            line[1][start_p] = '$'
            for iteration in line:
                for elem in iteration:
                    print(elem, end='')
                print('')

