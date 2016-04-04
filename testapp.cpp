/* ==========================================
File: 		main.cpp
Author:		Bonnie Jan
Date:		4/3/2016
Program:	TestApp
========================================== */

#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

int main()
{
	// Stream variable
	ofstream out;

	// Open file
	out.open("data.txt", std::ofstream::out | std::ofstream::app);

	// Prompt for input
	cout << "Please enter text to save to data.txt: \n";

	// Save data to file
	string str;

	getline(cin, str);
	out << str << endl;

	// Close file
	out.close();

	return 0;
}