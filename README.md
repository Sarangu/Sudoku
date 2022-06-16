# Sudoku
Implementing Sudoku using backtracking algorithm


## Introduction
The objective of Sudoku is to fill a 9x9 grid with the numbers 1-9 so that each column, row, and 3x3 sub-grid (or
box) contains one of each digit. 
Sudoku has 81 variables, i.e. 81 tiles. The variables are named by row and column, and are valued from 1 to 9 subject to the constraints that no
two cells in the same row, column, or box may be the same.

The Sudoku board is represented with a Python dictionary, where each key is a variable name based on location, and value of the tile placed there.
Using variable names Al... A9... I1... I9, the board above has:

• sudoku dict["B1"] = 2, and

• sudoku dict["E2"] = 9.

Value zero to a tile that has not yet been filled.


## Executing your program
The program is run as follows:

```$ python3 sudoku.py <input string>```

If no input string is given, the file takes ```sudokus_start.txt``` by default (must be in the same folder)

## Files
This repository contains the following files:

```sudokus_start.txt```: Contains hundreds of sample unsolved Sudoku boards

```sudokus_finish.txt```: Contains the solutions corresponding to boards in ```sudokus_start.txt```

```output.txt```: Output file generated after running ```sudoku.py```

```sudoku.py```: Python file containing core logic of sudoky using backtracking

```CSP_AC3.py, BackTrack.py```: Python files containing helper functions


Each board is represented as a single line of text, starting from the top-left corner of
the board, and listed left-to-right, top-to-bottom.

The first board in sudokus start.txt is represented as the string:

003020600900305001001806400008102900700000008006708200002609500800203009005010300

Which is equivalent to:

0 0 3 0 2 0 6 0 0

9 0 0 3 0 5 0 0 1

0 0 1 8 0 6 4 0 0

0 0 8 1 0 2 9 0 0

7 0 0 0 0 0 0 0 8

0 0 6 7 0 8 2 0 0

0 0 2 6 0 9 5 0 0

8 0 0 2 0 3 0 0 9

0 0 5 0 1 0 3 0 0

## Statistics derived

The running time statistics from the 400 boards are:

Minimum run time is: 0.044412851333618164

Maximum run time is: 1.1967337131500244

Mean run time is: 0.16171199202537537

Standard deviation run time is: 0.13922421097105162
