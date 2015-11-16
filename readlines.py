#!/usr/bin/env python
# coding: utf-8
# input lines from stdin
# return list each line
# don't remove newline character

import sys

str = sys.stdin.readlines()
for l in str:
	l = l.strip()
	print l
