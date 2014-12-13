#! /usr/bin/env python

number = int(raw_input("\nHow many bricks do you want?"))
l = 0
for i in range(1, number+1):
	l += 0.3 / (2 * i)
	
print("The maximum span is " + str(round(l,4)) + "m.\n")