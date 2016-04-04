File:		README
Author: 	Bonnie Jan
Date:		4/3/2016
Program:	testapp

BUILDING THE PROGRAM
   This program was written in C++ in Visual Studio 2015. It's meant to
   be able to be built on a Linux system but doesn't seem to work.  Cygwin
   can make the executible, but I have missing dll errors when trying to
   run the program.  If it were working, to build the program, type 'make' to 
   create the executable called 'testapp'

RUNNING THE PROGRAM
   See above.  If it compiles, type 'testapp' at the command prompt after 
   building the program.

PROGRAM DESCRIPTION
   This program will read from stdin until the user presses the Enter key.
   Everything is read as text and stored as is in the file data.txt
   appended at the end of the file.  The file isn't overwritten, so the   
   user can refer back to what they previously saved to the file.

PROGRAM INPUT
   All input comes from the stdin by the user and is saved once they
   press Enter.

PROGRAM OUTPUT
   All output is written to the file data.txt as it was entered.

PROGRAM DESIGN
   This program prompts for and stores input entered by the user 
   from the command prompt appended to the end of the file data.txt.

FILE INDEX
   file              					description
   --------------     					----------------------
   testapp.cpp          				prompts for and saves inputs
                                        to data.txt

   data.txt                             file input is appended to

   makefile                          	builds executable; currently may not
										work, possibly because of development
										environment or incorrectly written
										from how I don't need to make one 
										when using Visual Studio

   README                            	this file
   
   TestApp.exe							compiled executable of the app from
										Visual Studio
										
   other TestApp files					Visual Studio produced files for
										creating project


