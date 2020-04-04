import os
import random
import math
import copy
import argparse
import time

class State:
    def __init__(self):
        self.board = [[]] * 7
        for i in range(7):
            self.board[i] = [0] * 7
        self.N = 7
        self.turn = 1

    def __repr__(self):
        return str(self.board)

    def __str__(self):
        return str(self.board)
    
    def print(self):
        print("    0 1 2 3 4 5 6")
        print()
        for i, row in enumerate(self.board):
            print(i, end='   ')
            for col in row:
                if col == 0:
                    print('_', end=' ')
                elif col == 9:
                    print('x', end=' ')
                else:
                    print(col, end=' ')
            print()
        print()

    def get_possible_moves(self, turn):
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        if any(turn in sublist for sublist in self.board):
            idx = [(i, b.index(turn)) for i, b in enumerate(self.board) if turn in b]
            
            pos_moves = []

            for move in directions:
                pos = idx[0]

                while pos[0] + move[0] >= 0 and pos[0] + move[0] < self.N and \
                        pos[1] + move[1] >= 0 and pos[1] + move[1] < self.N and \
                        self.board[pos[0] + move[0]][pos[1] + move[1]] == 0:

                    pos = (pos[0] + move[0], pos[1] + move[1])
                    pos_moves.append(pos)

            return pos_moves
        else:
            return [(i, j) for i in range(self.N) for j in range(self.N) if self.board[i][j] == 0]

    def copy(self):
        new_state = State()
        new_state.board = copy.deepcopy(self.board)
        new_state.turn = self.turn
        return new_state

    def apply_move(self, move):
        new_state = self.copy()
        idx = [(i, b.index(self.turn)) for i, b in enumerate(self.board) if self.turn in b]
        if idx == []:
            new_state.board[move[0]][move[1]] = self.turn
            new_state.turn = 1 if self.turn == 2 else 2
            return new_state
        new_state.board[idx[0][0]][idx[0][1]] = 9
        new_state.board[move[0]][move[1]] = self.turn
        new_state.turn = 1 if self.turn == 2 else 2
        return new_state

def is_terminal(state):
    
    if len(state.get_possible_moves(1)) == 0 or \
        len(state.get_possible_moves(2)) == 0:
        return True
    return False

def heuristic_eval(state):
    return len(state.get_possible_moves(2)) - len(state.get_possible_moves(1))

def alpha_beta_pruning(state, alpha, beta, d):
    if is_terminal(state) or d == 0:
        return heuristic_eval(state)
    if state.turn == 2:
        for move in state.get_possible_moves(2):
            alpha = max(alpha, alpha_beta_pruning(state.apply_move(move), alpha, beta, d - 1))
            if alpha >= beta:
                return alpha
        return alpha
    else:
        for move in state.get_possible_moves(1):
            beta = min(beta, alpha_beta_pruning(state.apply_move(move), alpha, beta, d - 1))
            if alpha >= beta:
                return beta
        return beta
    
def best_step(state, depth=math.inf, secs=math.inf):
    mvs = state.get_possible_moves(2)
    vals = []

    if depth != math.inf:
        for move in mvs:
            vals.append(alpha_beta_pruning(state.apply_move(move), -math.inf, math.inf, depth))
    else:
        
        depth = 1
        time_to_think = time.time() + secs
        while True:
            part_vals = []
            for move in mvs:
                if time.time() >= time_to_think:
                    break
                part_vals.append(alpha_beta_pruning(state.apply_move(move), -math.inf, math.inf, depth))
            if time.time() >= time_to_think:
                if len(part_vals) < len(mvs):
                    if len(vals) == 0:
                        return random.choice(mvs)
                    else:
                        break
                else:
                    break
            else:
                vals = part_vals
                depth += 1


    return mvs[vals.index(max(vals))]

parser = argparse.ArgumentParser("Isolation game", add_help=False)
parser.add_argument("-d", type=int)
parser.add_argument("-t", type=int)

args = parser.parse_args()

depth = math.inf
secs = math.inf

if args.d:
    depth = int(args.d)
elif args.t:
    secs = int(args.t)
else:
    print("No argument given! Exiting...")
    exit()

state = State()

while True:
    os.system("cls")
    state.print()
    pos_m = state.get_possible_moves(1)
    if len(pos_m) == 0:
        print("You lost!")
        break
    print("Your possible moves:")
    for i, move in enumerate(pos_m):
        print(i, move)
    chosen = int(input("Which one do you choose? "))
    while type(chosen) != int or chosen < 0 or chosen > len(pos_m) - 1:
        chosen = int(input("Wrong number! Try again! "))
    state = state.apply_move(pos_m[chosen])
    os.system("cls")
    state.print()
    
    pos_m = state.get_possible_moves(2)
    if len(pos_m) == 0:
        print("You won!")
        break
    print("Computer is thinking...")
    chosen = best_step(state.copy(), depth, secs)
    state = state.apply_move(chosen)