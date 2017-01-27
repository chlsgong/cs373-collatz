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
INT_CACHE = {1 : 1}      # key: int e, value: int producing the max cycle len from [1, e]
CYC_CACHE = {1 : 1}      # key: int i, value: cycle len of i

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

    maxInt = 0
    maxCycleLength = 0

    # check if max key is > than n
    maxKey = max(INT_CACHE.keys())
    if n in INT_CACHE and maxKey >= n :
        maxInt = INT_CACHE[n]
    else :
        if maxKey in INT_CACHE :
            maxInt = INT_CACHE[maxKey]
            maxCycleLength = CYC_CACHE[maxInt]

        # start iterating through range
        for i in range(maxKey + 1, n + 1) :
            assert i > 0

            curInt = i
            cnt = 1
            
            # collatz calculation starts here
            while i > 1 :
                if i in CYC_CACHE :
                    cnt = cnt + CYC_CACHE[i] - 1
                    break

                if (i % 2) == 0 :
                    i = (i // 2)
                    cnt += 1
                else :
                    i = i + (i >> 1) + 1
                    cnt += 2

            if curInt not in CYC_CACHE :
                CYC_CACHE[curInt] = cnt

            # check if max values need to be changed
            if cnt >= maxCycleLength :
                maxInt = curInt
                maxCycleLength = cnt
                # print("maxInt: ", maxInt, "maxCycleLength: ", maxCycleLength)

            if curInt not in INT_CACHE :
                INT_CACHE[curInt] = maxInt

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
