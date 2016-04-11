# File: 	testapp.py
# Author:	Bonnie Jan
# Date:		4/6/2016, modified 4/10/16
# Program:	testapp
#
# Retrieve line from user terminated by Enter and save to file data.txt.
# Each entry is appended as a new line at the end of the file.
#
# PRE: Text files for input and output are in ANSI format. Input 
#      is expected to be passed from a file using
#
#      cat FILE | python testapp.py
#
#      at the command line, where FILE is replaced by the name of the
#      input file. File is formatted with each line ended by '\n'.
# POST: data.txt contains input from FILE passed through stdin. Has been 
#       tested to work with 40 MB file.


import sys

# Function to open file for appending and close after
def write_stdin_to_file(filename):
	
	# Open file
	with open(filename, 'a') as f:
	
		# Take input from stdin
		for line in sys.stdin:

			# Save data to file
			f.write(str(line))
			
if __name__ == "__main__":
	write_stdin_to_file('data.txt')





