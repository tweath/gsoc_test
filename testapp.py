# File: 	testapp.py
# Author:	Bonnie Jan
# Date:		4/6/2016
# Program:	testapp
#
# Retrieve line from user terminated by Enter and save to file data.txt.
# Each entry is appended as a new line at the end of the file.

# Open file for appending and close after
with open('data.txt', 'a') as f:

	# Prompt for input
	str = input('Please enter text to save to data.txt: \n')

	# Save data to file
	f.write(str + "\n")


