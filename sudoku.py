#!/usr/bin/env python
#coding:utf-8

"""
Each sudoku board is represented as a dictionary with string keys and
int values.
e.g. my_board['A1'] = 8
"""
from CSP_AC3 import*
from BackTrack import*
import sys
import time
import statistics

ROW = "ABCDEFGHI"
COL = "123456789"


def print_board(board):
    """Helper function to print board in a square."""
    print("-----------------")
    for i in ROW:
        row = ''
        for j in COL:
            row += (str(board[i + j]) + " ")
        print(row)


def board_to_string(board):
    """Helper function to convert board dictionary to string for writing."""
    ordered_vals = []
    for r in ROW:
        for c in COL:
            ordered_vals.append(str(board[r + c]))
    return ''.join(ordered_vals)


def backtracking(board):
    """Takes a board and returns solved board."""
    # TODO: implement this
    csp_board = CSP(board)
    check_if_consistent = AC3(csp_board)
    if check_if_consistent:
        board = BackTrack({}, csp_board)
    solved_board = board
    return solved_board


if __name__ == '__main__':
    #  Read boards from source.
    out_filename = 'output.txt'
    stats_filename = 'stats.txt'
    outfile = open(out_filename, "w")
    stats_outfile = open(stats_filename, "w")
    run_times = []
    if len(sys.argv) == 1:
        src_filename = 'sudokus_start.txt'
        try:
            srcfile = open(src_filename, "r")
            sudoku_list = srcfile.read()
        except:
            print("Error reading the sudoku file %s" % src_filename)
            exit()
    # Solve each board using backtracking
        for line in sudoku_list.split("\n"):
            if len(line) < 9:
                continue

        # Parse boards to dict representation, scanning board L to R, Up to Down
            board = { ROW[r] + COL[c]: int(line[9*r+c]) for r in range(9) for c in range(9)}

        # Print starting board. TODO: Comment this out when timing runs.
#             print_board(board)

        # Solve with backtracking
            start_time = time.time()
            solved_board = backtracking(board)
            end_time = time.time()
            run_time = end_time - start_time
            run_times.append(run_time)
            
            outfile.write(board_to_string(solved_board))
            outfile.write('\n')
        # Print solved board. TODO: Comment this out when timing runs.
#             print_board(solved_board)
        min_run_time = min(run_times)
        max_run_time = max(run_times)
        mean_run_time = statistics.mean(run_times)
        std_dev_run_time = statistics.stdev(run_times)

        stats_outfile.write("Minimum run time is: " + str(min_run_time) + "\n")
        stats_outfile.write("Maximum run time is: " + str(max_run_time) + "\n")
        stats_outfile.write("Mean run time is: " + str(mean_run_time) + "\n")
        stats_outfile.write("Standard deviation run time is: " + str(std_dev_run_time) + "\n")
        stats_outfile.close()
        # print("Finishing all boards in file.")
        outfile.close()
            
    elif len(sys.argv) > 1:
        for arg in sys.argv[1:]:
        # Parse boards to dict representation, scanning board L to R, Up to Down
            board = { ROW[r] + COL[c]: int(arg[9*r+c]) for r in range(9) for c in range(9)}

        # Print starting board. TODO: Comment this out when timing runs.
#             print_board(board)

        # Solve with backtracking
            start_time = time.time()
            solved_board = backtracking(board)
            end_time = time.time()
            run_time = end_time - start_time
            run_times.append(run_time)
            
        # Write board to file
            outfile.write(board_to_string(solved_board))
            outfile.write('\n')
        # Print solved board. TODO: Comment this out when timing runs.
#             print_board(solved_board)
