#!/usr/bin/env python3

import sys

# graph / output array
OUT = []

TYPES = ["_", '*', ' ', '#']
# generate something like this:
#{'_': 0, '*': 1, ' ': 2}

TYPEDICT = dict(zip(list(range(len(TYPES))), TYPES))
TYPEDICT_R = dict([(TYPEDICT.get(k),k) for k in TYPEDICT])


def rule1(arr):
	'''
	next type of each is added by index and wrapped around
	'''
	for i in range(len(arr)):
		c = arr[i]
		typeindex = TYPEDICT_R[c]
		nexttypeindex = (typeindex + i) % len(TYPES)
		arr[i] = TYPES[nexttypeindex]
	return arr

def rule2(arr):
	for i in range(len(arr)):
		c = arr[i]
		typeindex = TYPEDICT_R[c]
		# nexttypeindex = (typeindex) % len(TYPES)
		if typeindex < 2:
			nexttypeindex = (typeindex + i) % len(TYPES)
			arr[i] = TYPES[nexttypeindex]
		else:
			nexttypeindex = (typeindex - i) % len(TYPES)
			arr[i] = TYPES[nexttypeindex]
	return arr

def rule3(arr):
	for i in range(len(arr)):
		c = arr[i]
		c_left = arr[(i+1) % len(TYPES)]
		c_right = arr[(i-1) % len(TYPES)]
		typeindex = TYPEDICT_R[c]
		left_typeindex = TYPEDICT_R[c_left]
		right_typeindex = TYPEDICT_R[c_right]

		if typeindex > left_typeindex:
			arr[i] = TYPES[(typeindex * 2) % len(TYPES)]
		else:
			arr[i] = TYPES[(typeindex - 1) % len(TYPES)]
	return arr

def rule4(arr):
	for i in range(len(arr)):
		c = arr[i]
		c_left = arr[(i+1) % len(TYPES)]
		c_right = arr[(i-1) % len(TYPES)]
		typeindex = TYPEDICT_R[c]
		left_typeindex = TYPEDICT_R[c_left]
		right_typeindex = TYPEDICT_R[c_right]

		if typeindex > left_typeindex:
			arr[i] = TYPES[(typeindex * 2) % len(TYPES)]
		if typeindex < right_typeindex:
			arr[i] = TYPES[(typeindex // 2) % len(TYPES)]
		else:
			arr[i] = TYPES[(typeindex - 1) % len(TYPES)]
	return arr

def prettyprint(arr):
	print(''.join(arr))

def run(rulefunc, count):
	init = list("_" * 50)
	prettyprint(init)
	for i in range(count):
		init = rule1(init)
		prettyprint(init)


count = 10


print("----------- rule1 ----------------")
run(rule1, count)

print("----------- rule2 ----------------")
run(rule2, count)

print("----------- rule3 ----------------")
run(rule3, count)

print("----------- rule4 ----------------")
run(rule4, count)