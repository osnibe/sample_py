#!/usr/bin/env python
# coding: utf-8
#
# example
# 123 456
# 5
# ab cd
# ef ghi
# jk lmn
# op qrs
# tu vwx

import sys

s = raw_input().split()
a = int(s[0]) # 123
b = int(s[1]) # 456
print a, b

n = int(raw_input()) # 5
print n

line = sys.stdin.readlines()
for l in line:
	l = l.split()
	i = l[0]
	j = l[1]
	print i, j
