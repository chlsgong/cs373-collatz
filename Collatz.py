#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2017
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

def collatz_read (r) :
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

def collatz_eval (n) :
    """
    n the end of the range [1, n], inclusive
    return the max cycle length of the range [1, n]
    """
    # <your code>
    assert n > 0

    maxInt = 0
    maxCycleLength = 0

    for i in range(1, n + 1) :
        curInt = i
        c = 1
        
        while i > 1 :
            if (i % 2) == 0 :
                i = (i // 2)
            else :
                i = (3 * i) + 1
            c += 1

        # print("curInt", curInt, "c", c)
        if c >= maxCycleLength :
            maxCycleLength = c
            maxInt = curInt

        assert c > 0

    assert maxInt > 0

    return maxInt

# -------------
# collatz_print
# -------------

def collatz_print (w, m) :
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

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    t = int(r.readline())
    for _ in range(t) :
        n = collatz_read(r)
        m = collatz_eval(n)
        collatz_print(w, m)
