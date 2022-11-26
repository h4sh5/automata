#!/usr/bin/env python3

import sys
import random
import time
# graph / output array
OUT = []

# TYPES = ["_", '*', ' ', '#']
TYPES = [' ', '\\', '/', '*', '#']
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

def rule5(arr, A=2, B=2, C=1):
	# rule 4 with weight vars
	# print(a,b,c)
	for i in range(len(arr)):
		c = arr[i]
		c_left = arr[(i+1) % len(TYPES)]
		c_right = arr[(i-1) % len(TYPES)]
		typeindex = TYPEDICT_R[c]
		left_typeindex = TYPEDICT_R[c_left]
		right_typeindex = TYPEDICT_R[c_right]

		if typeindex > left_typeindex:
			arr[i] = TYPES[(typeindex * A) % len(TYPES)]
		if typeindex < right_typeindex:
			arr[i] = TYPES[(typeindex // B) % len(TYPES)]
		else:
			arr[i] = TYPES[(typeindex - C) % len(TYPES)]
	return arr

def metarule1(vararr):
	return [x + 2 for x in vararr]


def metarule2(vararr):
	for i in range(len(vararr)):
		random.seed(time.time())
		vararr[i] = random.choice(vararr)
	return vararr

def metarule3(vararr):
	# swap the variables around (A and B)
	B = vararr[1]
	vararr[1] = vararr[0]
	vararr[0] = B
	return vararr


def prettyprint(arr, i=None):
	if i:
		print(''.join(arr), end=' '+str(i)+'\n')
	else:
		print(''.join(arr))

def run(rulefunc, count):
	init = list(TYPES[0] * 50)
	prettyprint(init)
	for i in range(count):
		
		init = rulefunc(init)
		prettyprint(init)

def metarun(rulefunc, metafunc, count):
	init = list(TYPES[0] * 100)
	varinit = [2,2,1]
	prettyprint(init)
	for i in range(count):
		init = rulefunc(init, varinit[0] , varinit[1], varinit[2])
		varinit = metafunc(varinit)
		prettyprint(init, i)

count = 10

if len(sys.argv) > 1:
	count = int(sys.argv[1])


# print("----------- rule1 ----------------")
# run(rule1, count)

# print("----------- rule2 ----------------")
# run(rule2, count)

# print("----------- rule3 ----------------")
# run(rule3, count)

# print("----------- rule4 ----------------")
# run(rule4, count)

print("----------- rule5 metarule1 ----------------")
metarun(rule5, metarule1, count)

print("----------- rule5 metarule2 ----------------")
metarun(rule5, metarule2, count)

print("----------- rule5 metarule3 ----------------")
metarun(rule5, metarule3, count)
