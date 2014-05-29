# Google Code Jam Practice Mode
# Qualification Round Africa 2010 - B. Reverse Words

# Problem

# Given a list of space separated words, reverse the order of the words. Each line of text contains L letters and W words. A line will only consist of letters and space characters. There will be exactly one space character between each pair of consecutive words.

# Input

# The first line of input gives the number of cases, N.
# N test cases follow. For each test case there will a line of letters and space characters indicating a list of space separated words. Spaces will not appear at the start or end of a line.

# Output

# For each test case, output one line containing "Case #x: " followed by the list of words in reverse order.

import os
import sys

def reverse_words(inputstr):
	"""Reverses the order of words in a string."""
	inputstr = inputstr.split(' ').reverse().join(' ')

num = raw_input('How many cases?\n')	# Input number of cases
print 'Number of cases: %s' % num 		# Verify
cases = [num]							# Create array
for i in range(0, (num - 1)):			# Input values into the array
	cases[i] = raw_input()				

for string in range(0, (num - 1)): 		# Iterate 
	reverse_words(string)
	print "Case #%s: %s" % num string 	# Print reversed strings

# To do:
# 	Get build env working
# 	Make sure I'm using lists correctly
#	Test