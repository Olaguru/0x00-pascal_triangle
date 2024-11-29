#!/usr/bin/python3
"""making change"""


def makeChange(coins, total):
    """number of change needed for a total"""
    if total <= 0:
        return 0

    change = 0
    few_number = 0

    coins.sort(reverse=True)

    for i in coins:
        while change < total:
            change += i
            few_number += 1
        if change == total:
            return few_number
        change -= i
        few_number -= 1
    return -1
