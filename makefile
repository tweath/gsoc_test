testapp: testapp.o
	g++ -o testapp testapp.o
testapp.o: testapp.cpp
	g++ -c testapp.cpp
clean:
	\rm *.o *~ p1