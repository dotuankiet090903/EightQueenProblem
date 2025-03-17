import copy
import random
class EightQueenProblem:
    def __init__(self,filename) -> None:
        self.board = self.load_from_file(filename)
    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            board = []
            for line in f:
                row = ['0' if c == '0' else 'Q' for c in line.split()]
                board.append(row)
            return board
            
    def print_board(self, board):
        for row in board:
            line = ''
            for cell in row:
                if cell == '0':
                    line += ' 0'
                else:
                    line += ' Q'
            print(line)
    # finding pair of queens which is attacking each other
    def h(self,state):
        n = len(state[0])
        queen_pair = 0 #queen pairs that is attacking each other
        check_queen = [] ###
        for r in range(n):
            for c in range(n):
                if state[r][c] == 'Q': # if state[c][r] is a queen then check
                    for i in range(1,n): # As i increase, the diagnoal and rows, columns will increase in range 
                          
                        # Check diagonals
                        if r-i >= 0 and c-i >= 0 and state[r-i][c-i] == 'Q':
                            check_queen.append(((r,c),(r-i,c-i)))
                            queen_pair += 1
                        if r-i >= 0 and c+i < n and state[r-i][c+i] == 'Q':
                            check_queen.append(((r,c),(r-i,c+i)))
                            queen_pair += 1
                        if r+i < n and c-i >= 0 and state[r+i][c-i] == 'Q':
                            check_queen.append(((r,c),(r+i,c-i)))
                            queen_pair += 1
                        if r+i < n and c+i < n and state[r+i][c+i] == 'Q':
                            check_queen.append(((r,c),(r+i,c+i)))
                            queen_pair += 1
                        
                        # Check rows and columns
                        if r+i < n and state[r+i][c] == 'Q':
                            check_queen.append(((r,c),(r+i,c)))
                            queen_pair += 1
                        if c+i < n and state[r][c+i] == 'Q':
                            check_queen.append(((r,c),(r,c+i)))
                            queen_pair += 1
                        if r-i >= 0 and state[r-i][c] == 'Q':
                            check_queen.append(((r,c),(r-i,c)))
                            queen_pair += 1
                        if c-i >= 0 and state[r][c-i] == 'Q':
                            check_queen.append(((r,c),(r,c-i)))
                            queen_pair += 1
                            
        queen_pair = queen_pair // 2
        return queen_pair # Return number of Q pair which can attack each other
    # to take queen
    def get_queens(self,state):
      queens = set()
      n = len(state)
      for r in range(n):
        for c in range(n):
          if state[r][c] == 'Q':
            queens.add((r,c))
      return sorted(queens)

    def h_whole_board(self,state):
      queens = self.get_queens(state)
      h_board = {}
      n = len(state)
      curr_state = copy.deepcopy(state)
      for i in queens:
        curr_col = i[0]
        x,y = i ###
        curr_state[x][y] = '0'
        for k in range(n):
          curr_state[k][y] = 'Q' 
          h = self.h(curr_state)
          h_board[(k,y)] = h
          curr_state[k][y] = h
        curr_state[x][y] = 'Q'
      for i in queens:
        x,y = i
        curr_state[x][y] = h_board[(x,y)]
      curr_state = h_col = [list(row) for row in zip(*curr_state)]
      return curr_state

    def goal_test(self,state):
      cur_state = copy.deepcopy(state)
      return self.h(cur_state) == 0 
    
    # Finding heuristic value in selected position     
    # idx is a list because many position can have multiple equal heuristic value
    def find_min(self,list_h):
      min_val = min(list_h)
      idx = [i for i, x in enumerate(list_h) if x== min_val]
      return random.choice(idx)

    def hill_climbing_search(self):
      curr_state = copy.deepcopy(self.board)
      for i in range(50):
        curr_h = self.h(curr_state)
        queens = self.get_queens(curr_state)
        h_board = self.h_whole_board(curr_state)
        temp_board = copy.deepcopy(curr_state)
        for q in queens:
          r,c = q
          r_min = self.find_min(h_board[c])
          temp_board[r][c] = '0'
          temp_board[r_min][c] = 'Q'
        temp_h = self.h(temp_board)
        if temp_h > curr_h:
          continue
        else : 
          curr_state = temp_board
      return curr_state

        
thu = EightQueenProblem('eight_queens02.txt')
board = thu.board
temp = thu.hill_climbing_search()
# for r in board:
#   print(''.join(str(r)))
# print('----------------------')
for r in temp:
  print(''.join(str(r)))
print(thu.h(temp))
thu.print_board(temp)