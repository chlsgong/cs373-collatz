#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2017
# Glenn P. Downing
# ---------------------------

# Cache Declarations
INT_CACHE = {}      # key: int e, value: int producing the max cycle len from [1, e]
CYC_CACHE = {}      # key: int i, value: cycle len of i

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
    assert n > 0

    if n in INT_CACHE :
        return INT_CACHE[n]

    maxInt = 0
    maxCycleLength = 0

    # start iterating through range
    for i in range(1, n + 1) :
        assert i > 0

        curInt = i
        cnt = 1
        
        # collatz calculation starts here
        while i > 1 :
            if i in CYC_CACHE :
                cnt = CYC_CACHE[i]
                break

            if (i % 2) == 0 :
                i = (i // 2)
                cnt += 1
            else :
                i + (i >> 1) + 1
                cnt += 2

        # check if max values need to be changed
        if cnt >= maxCycleLength :
            maxCycleLength = cnt
            maxInt = curInt

        assert cnt > 0

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
