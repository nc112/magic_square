#!/usr/bin/env python
'''This program is aming to find all possible combination of 1~9
to make a 3 order magic square'''

# initialize the sum of line/column/diagonal
line_1 = 0
line_2 = 0
line_3 = 0
col_1 = 0
col_2 = 0
col_3 = 0
diag_1 = 0
diag_2 = 0


# calculate the sum of every line/column/diagonal
def rule_sum(A):
    line_1 = sum(A[:3])
    line_2 = sum(A[3:6])
    line_3 = sum(A[6:])
    col_1 = sum([A[0], A[3], A[6]])
    col_2 = sum([A[1], A[4], A[7]])
    col_3 = sum([A[2], A[5], A[8]])
    cross_1 = sum([A[0], A[4], A[8]])
    cross_2 = sum([A[2], A[4], A[6]])

    return ([line_1, line_2, line_3, col_1, col_2, col_3, cross_1, cross_2])


# compare the element from item to 15
def rule_equal(item):
    if item == [15] * 8:
        return True
    else:
        return False


 #   use built-in function to get all combination of 1~9

from itertools import permutations
All = list(permutations(range(10),9))
print(len(All))

# print the combination, when it match the rule of the game.
for item in All:
    result = rule_equal(rule_sum(item))
    if result == True:
        print(item[:3])
        print(item[3:6])
        print(item[6:], "\n")
