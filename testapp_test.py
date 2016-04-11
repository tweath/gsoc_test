# File: 	testapp_test.py
# Author:	Bonnie Jan
# Date:		4/10/2016
# Program:	testapp
#
# Test that data.txt data is the same as in expected.txt, except for the
# final line from stdin to data.txt.
#
# PRE: Text files for input and output are in ANSI format, unusual
#      characters don't show up in files when displayed on console. Input 
#      to prompt is expected to be the last line of input in expected.txt
#      and rest of data.txt has remainder of the content in expected.txt 
#      already for test to not fail; . Works with version of testapp.py 
#      created before 4/10/2016. testapp.py should be in the same directory 
#      as testapp_test.py.
#
# POST: Indicates whether or not data.txt has same data as expected.txt. 
#       Suitable for smaller file sizes.

from io import StringIO
import unittest
import testapp

class TestTestapp(unittest.TestCase):
	
	# Checks that files are the same using lists with each line stored as
	# a list item
	def test_write_stdin_to_file(self):
		
		with open('data.txt', 'r') as f, open('expected.txt', 'r') as fEx:
			
			# Read data from both files
			read = f.readlines()
			expected_read = fEx.readlines()
			
			# Check that read file contents are the same
			self.assertListEqual(read, expected_read)

if __name__ == '__main__':
	unittest.main()
