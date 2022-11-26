#!/usr/bin/env python3

import sys

# graph / output array
OUT = []

TYPES = ["_", '*', ' ']
# generate something like this:
#{'_': 0, '*': 1, ' ': 2}

TYPEDICT = dict(zip(list(range(len(TYPES))), TYPES))
TYPEDICT_R = dict([(TYPEDICT.get(k),k) for k in TYPEDICT])


def rule1(arr):
	for i in range(len(arr)):
		c = arr[i]
		typeindex = TYPEDICT_R[c]
		nexttypeindex = (typeindex + i) % len(TYPES)
		arr[i] = TYPES[nexttypeindex]
	return arr



def prettyprint(arr):
	print(''.join(arr))

init = list("_" * 50)
count = 5
prettyprint(init)
for i in range(count):
	init = rule1(init)
	prettyprint(init)



