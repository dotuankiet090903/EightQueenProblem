# EightQueenProblem

  The 8 Queens Problem is a classic combinatorial optimization and constraint satisfaction problem in chess. The goal is to place eight queens on an 8×8 chessboard such that no two queens can attack each other. This means:

- No two queens can be in the same row.
- No two queens can be in the same column.
- No two queens can be in the same diagonal.

This project doesn't apply any advance technique but solely using problem solving skill and to understand through the pattern of the problem to achieve the goal. The map with its queens is a given file which:

-  "0": stand for the space of the chessboard
-  "Q": stand for the position of the queen standing on the board

The map is random and the code will rely only logic 
There are others map option or you can create your own map and replace it with "eight_queens02.txt" in the piece of code "thu = EightQueenProblem('eight_queens02.txt')" 
The result will return the complete map that achieve the goal and the number of pairs of queens that are attacking each other after the code done.
