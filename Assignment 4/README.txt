README – Assignment 4

Name: Anish Bandaru
Roll No: SE24UCSE007

--------------------------------------------------

OVERVIEW

This project contains implementations of four important problems based on Constraint Satisfaction Problems (CSP):

1. Australia Map Coloring
2. Telangana District Map Coloring
3. Sudoku Solver
4. Cryptarithmetic Puzzle

The objective of this assignment is to understand how CSP techniques like backtracking and constraint checking are used.

--------------------------------------------------

1. AUSTRALIA MAP COLORING (CSP)

This problem assigns colors to Australian states such that no neighboring states share the same color.

Key Idea:
Uses backtracking to assign colors while satisfying constraints.

--------------------------------------------------

2. TELANGANA MAP COLORING (CSP)

This problem assigns colors to Telangana districts ensuring adjacent districts have different colors.

Key Idea:
A larger CSP solved using backtracking.

--------------------------------------------------

3. SUDOKU SOLVER (CSP)

Solves a 9x9 Sudoku puzzle.

Rules:
• Each row, column, and 3x3 grid must have numbers 1–9 without repetition.

Key Idea:
Backtracking with constraint checking.

--------------------------------------------------

4. CRYPTARITHMETIC PUZZLE (CSP)

Puzzle: TWO + TWO = FOUR

Each letter represents a unique digit.

Key Idea:
Uses permutations to find a valid mapping.

--------------------------------------------------

HOW TO RUN

1. Install Python
2. Install libraries:

pip install networkx matplotlib

3. Run:

python australia_csp.py
python telangana_csp.py
python sudoku.py
python Cryptarithmetic_CSP.py

--------------------------------------------------

CONCLUSION

This project demonstrates how CSP is used in:
• Map Coloring
• Sudoku
• Cryptarithmetic problems

--------------------------------------------------

