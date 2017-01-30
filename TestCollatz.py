#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2017
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz (TestCase) :
    # ----
    # read
    # ----

    def test_read_1 (self) :
        r = StringIO("10\n")
        n = collatz_read(r)
        self.assertEqual(n, 10)

    def test_read_2 (self) :
        r = StringIO("-1\n")
        self.assertRaises(AssertionError, collatz_read, r)

    def test_read_3 (self) :
        r = StringIO("5000000\n")
        n = collatz_read(r)
        self.assertEqual(n, 5000000)

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        m = collatz_eval(10)
        self.assertEqual(m, 9)

    def test_eval_2 (self) :
        m = collatz_eval(15)
        self.assertEqual(m, 9)

    def test_eval_3 (self) :
        m = collatz_eval(20)
        self.assertEqual(m, 19)
    
    def test_eval_4 (self) :
        m = collatz_eval(3)
        self.assertEqual(m, 3)

    def test_eval_5 (self) :
        m = collatz_eval(5000000)
        self.assertEqual(m, 3732423)

    def test_eval_6 (self) :
        self.assertRaises(AssertionError, collatz_eval, 5000001)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO()
        collatz_print(w, 10)
        self.assertEqual(w.getvalue(), "10\n")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO("3\n10\n15\n20\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "9\n9\n19\n")

    def test_solve_2 (self) :
        r = StringIO("10\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1\n2\n3\n3\n3\n6\n7\n7\n9\n9\n")

    def test_solve_3 (self) :
        r = StringIO("2\n1\n5000000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1\n3732423\n")

# ----
# main
# ----

if __name__ == "__main__" : #pragma: no cover
    main()
