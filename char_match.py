#!/usr/bin/env python

import sys

flag = False
c = raw_input()
lines = sys.stdin.readlines()

for line in lines:
	line = line.strip()
	if c in line:
		print line
		flag = True

if flag == False:
	print "not match"
