CXX = g++
CXXFLAGS = -O2 -std=c++17 -Wall -Wextra -march=native

all: fib

fib: fib.cpp
	$(CXX) $(CXXFLAGS) -o fib fib.cpp

clean:
	rm -f fib
