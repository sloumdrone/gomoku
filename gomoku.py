#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gomoku_ai import Opponent

class Gomoku:
    def __init__(self):
        self.game_board = [ [ u' · ' for y in range(15) ] for x in range(15) ]
        self.turn = 0
        self.pieces = [u' ◍ ',u' ○ ']
        self.turn_number = 0
        self.directions = [[1,0],[1,-1],[0,-1],[-1,-1]]
        self.opponent = Opponent(self)
        self.game_loop()

    def game_loop(self):
        while 1:
            self.print_board()

            if self.turn == 1:
                op_move = self.opponent.move()
                row = op_move[0]
                col = op_move[1]
                print 'row? ' + str(row)
                print 'col? ' + str(col)
            else:
                try:
                    row = int(raw_input('Row? ')) - 1
                    col = int(raw_input('Column? ')) - 1
                except ValueError:
                    print '\n\nInvalid input, entry must be a number\n'
                    continue

                if not self.validate_input(row,col):
                    print '\nInvalid move {0} {1}'.format(row+1,col+1)
                    continue

            self.game_board[row][col] = self.pieces[self.turn]

            if self.check_win_state([row,col]):
                self.print_board()
                print u'PLAYER{0}WINS!'.format(self.pieces[self.turn])
                break
            elif self.turn_number > 225:
                print 'There is no winner...'
                break

            self.turn = abs(self.turn - 1)
            self.turn_number += 1

    def validate_input(self,r,c):
        r = r
        c = c
        if r < 0 or r > 14 or c < 0 or c > 14:
            return False

        if self.game_board[r][c] != u' · ':
            return False

        return True

    def print_board(self):
        print '\n\n   1  2  3  4  5  6  7  8  9 10 11 12 13 14 15'
        for i, x in enumerate(self.game_board):
            output_row = str(i + 1) +''.join(x)
            print ' ' + output_row if i + 1 < 10 else output_row
        print u"\n<-- Player{0} -->".format(self.pieces[self.turn])

    def check_win_state(self,point):
        ends = [
            self.walk_to_ends(point,0),
            self.walk_to_ends(point,1),
            self.walk_to_ends(point,2),
            self.walk_to_ends(point,3)
            ]

        game_over = False

        for x in range(4):
            if self.count_to_five(ends[x],x):
                game_over = True
                break

        return game_over



    def count_to_five(self,start,direction,count=1):
        look_toward = [self.directions[direction][0] * -1,self.directions[direction][1] * -1]
        new_point = [start[0] + look_toward[0], start[1] + look_toward[1]]

        if count == 5:
            return True

        if new_point[0] < 0 or new_point[0] > 14 or new_point[1] < 0 or new_point[1] > 14 or self.game_board[new_point[0]][new_point[1]] != self.pieces[self.turn]:
            return False

        return self.count_to_five(new_point,direction, count + 1)



    def walk_to_ends(self,point,direction):
        look_toward = self.directions[direction]
        new_point = [point[0] + look_toward[0], point[1] + look_toward[1]]
        if new_point[0] < 0 or new_point[0] > 14 or new_point[1] < 0 or new_point[1] > 14 or self.game_board[new_point[0]][new_point[1]] != self.pieces[self.turn]:
            return point
        return self.walk_to_ends(new_point,direction)



if __name__ == "__main__":
    game = Gomoku()
