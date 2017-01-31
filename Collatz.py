#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = global-statement

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2017
# Glenn P. Downing
# ---------------------------

from bisect import bisect

# Meta-cache containing the int at which the max cycle len increases
INT_CACHE = [2, 3, 6, 7, 9, 18, 19, 25, 27, 54, 55, 73, 97, 129, 171, 231, 235,
             313, 327, 649, 654, 655, 667, 703, 871, 1161, 2223, 2322, 2323, 2463, 2919, 3711,
             6171, 10971, 13255, 17647, 17673, 23529, 26623, 34239, 35497, 35655, 52527,
             77031, 106239, 142587, 156159, 216367, 230631, 410011, 511935, 626331, 837799,
             1117065, 1126015, 1501353, 1564063, 1723519, 2298025, 3064033, 3542887, 3732423]

# ------------
# collatz_read
# ------------


def collatz_read(r):
    """
    read an int from r
    r a reader
    return the int
    """
    n = int(r.readline())
    assert n > 0
    return n

# ------------
# collatz_eval
# ------------


def collatz_eval(n):
    """
    n the end of the range [1, n], inclusive
    return the max cycle length of the range [1, n]
    """
    assert n > 0
    assert n <= 5000000

    maxInt = 1

    if n > 1:
        index = bisect(INT_CACHE, n)
        maxInt = INT_CACHE[index - 1]

    assert maxInt > 0

    return maxInt

# -------------
# collatz_print
# -------------


def collatz_print(w, m):
    """
    print an int to w
    w a writer
    m the max cycle length
    """
    assert m > 0
    w.write(str(m) + "\n")

# -------------
# collatz_solve
# -------------


def collatz_solve(r, w):
    """
    r a reader
    w a writer
    """
    t = int(r.readline())
    for _ in range(t):
        n = collatz_read(r)
        m = collatz_eval(n)
        collatz_print(w, m)
