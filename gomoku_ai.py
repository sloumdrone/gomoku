#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

class Opponent:
    def __init__(self,parent):
        self.game = parent
        self.directions = [[1,0],[-1,0],[0,-1],[0,1],[1,1],[-1,-1],[1,-1],[-1,1]]

    def generate_point_grid(self):
        point_grid = [ [ {'p': self.check_directions([x,y]),'r': x, 'c': y} for y in range(15) ] for x in range(15) ]
        return point_grid


    def check_directions(self,location):
        if self.game.game_board[location[0]][location[1]] != u' · ':
            return -1
        points = 0
        for direction in self.directions:
            points += self.score_consecutive_pieces(location,direction)
        return points

    def score_consecutive_pieces(self,point,direction,round=1,piece=None):
        new_point = [point[0] + direction[0], point[1] + direction[1]]
        if new_point[0] < 0 or new_point[0] > 14 or new_point[1] < 0 or new_point[1] > 14 or self.game.game_board[ new_point[0]][ new_point[1]] == u' · ':
            return 0
        if round == 1:
            piece = self.game.game_board[new_point[0]][new_point[1]]
        elif round == 4:
            return 100
        if piece != self.game.game_board[new_point[0]][new_point[1]]:
            return 0
        return round + self.score_consecutive_pieces(new_point,direction,round+1,piece)

    def choose_move(self,grid):
        sub_grid = [ max(x, key=lambda y: y['p']) for x in grid]
        max_value = max(sub_grid, key=lambda y: y['p'])['p']
        output_list = [x for x in sub_grid if x['p'] == max_value]
        final_move_choice = random.choice(output_list)
        return [final_move_choice['r'],final_move_choice['c']]

    def move(self):
        return self.choose_move( self.generate_point_grid() )
