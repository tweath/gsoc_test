# File: 	testapp_test.py
# Author:	Bonnie Jan
# Date:		4/10/2016
# Program:	testapp
#
# Test that data.txt data is the same as in expected.txt.
#
# PRE: Text files for input and output are in ANSI format. Input 
#      is expected to be passed from a file using
#
#      cat FILE | python testapp_test.py
#
#      at the command line, where FILE is replaced by the name of the
#      input file. File is formatted with each line ended by '\n'. 
#      testapp.py should be in the same directory as testapp_test.py.
#
# POST: Indicates whether or not data.txt has same data as expected.txt
#       and where there are differences. Suitable for smaller file 
#       sizes.

from io import StringIO
import sys
import unittest
import testapp

class TestTestapp(unittest.TestCase):
	
	def write_stdin_to_file(self, filename):
	
		# Open file
		with open(filename, 'a') as f:
	
			# Take input from stdin
			for line in sys.stdin:

				# Save data to file
				f.write(str(line))
	
#	def in_filename(self):
#		inFileName = 'expected.txt'
#		return inFileName
		
#	def out_filename(self):
#		outFileName = 'data.txt'
	
	def test_write_stdin_to_file(self):
		
		self.write_stdin_to_file('data.txt')

		with open('data.txt', 'r') as f, open('expected.txt', 'r') as fEx:
			
			# Read data from both files
			read = f.read()
			expected_read = fEx.read()
			
			# Check that read file contents are the same
			self.assertEqual(read, expected_read)

if __name__ == '__main__':
	unittest.main()
