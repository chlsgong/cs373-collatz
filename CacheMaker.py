#!/usr/bin/env python3

import sys

def makeCache():
	r = sys.stdin
	w = sys.stdout

	for _ in range(63):
		i = r.readline().rstrip('\n')
		w.write(i + ", ")


if __name__ == "__main__" :
	makeCache()
