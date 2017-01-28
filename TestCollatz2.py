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

from Collatz import collatz_eval

# -----------
# TestCollatz
# -----------

class TestCollatz (TestCase) :

    # ----
    # eval
    # ----

    # def test_eval_1 (self) :
    #     m = collatz_eval(10)
    #     self.assertEqual(m, 9)

    # def test_eval_2 (self) :
    #     m = collatz_eval(15)
    #     self.assertEqual(m, 9)

    # def test_eval_3 (self) :
    #     m = collatz_eval(20)
    #     self.assertEqual(m, 19)
    
    # def test_eval_4 (self) :
    #     m = collatz_eval(3)
    #     self.assertEqual(m, 3)

    def test_eval_5 (self) :
        m = collatz_eval(5000000)
        self.assertEqual(m, 3732423)

# ----
# main
# ----

if __name__ == "__main__" : #pragma: no cover
    main()