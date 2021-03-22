# Interview Prep

## Behavioral

## Technical

### What will be tested

-   Data Structures and Algorithms
    -   np complete problems: traveling salesman and the nap sack
    -   trees
        -   tree construction, traversal and manipulation algorithms
    -   hash tables, stacks, arrays, linked lists
    -   the complexity of an algorithm and how you can improve/change it.

*   Math: counting problems, probability
    -   n choose K problems
*   Recursion
*   Operating systems
    -   processes, threads, concurrency
    -   locks, semaphores, new texas?
    -   resource allocation, i.e. what resources a process or thread might need
    -   context switching. it's initiated in the operating system and underlying hardware
    -   how scheduling works

-   system design
    -   feature sets, interfaces, class hierarchies, distributed systems, design under certain constraints
    -   how the internet actually works, familiar with various pieces, i.e. routers, domains, servers, load balancers, firewalls
    -   basics of how search works
-   OOP, API
-   Testing
    -   unit tests, what test cases can you think of
    -   end-to-end, integration,load, performance, security tests for real-world systems

### How to prepare

-   Review algorithms and data structures, i.e. linked list, heap, hash table, etc
    -   what it is?
    -   how it works?
    -   why you use one over the other?
    -   big O notation
-   Practice writing code
    -   Practice on a white board or paper (no syntax highlighting in interview)
    -   Don't use pseudo code
    -   C++, Java, Python
-   Explain and clarify. Think out loud. Ask questions. How you approach problem-solving.
-   Thought process is more important than the right answer.

Sample Question

1. Clarify the problem

    - example rich enough but not tedious: "fastman" -> "fast man"?
    - disambiguate expected result: more than two words? empty string?

    - State and clarify key assumptions: exepcted result, any memory or performance requirements, etc.

        - Where do the words come from? Use a dictionary, a set of words. Use an API

    - Clarify the function signature, i.e. what comes in and what goes out

2. Start with the first solution that comes to mind

    - If necessary, start with the brute force solution and improve on it — just let the interviewer know that's what you're doing and why.
    - refine later
    - this will usually be a brute force solution
    - run through at least one or two examples to check for correctness
    - check again for edge cases
    - use reasonable variable names or clean up the code after the first pass
    - ask if the interviewer has any questions before refinement
        - What's the run time of this
        - What's the memory usage?

3. Refine the solution
    - clarify assumptions (e.g., improving performance)

# L1 Basics

### preprocessor directive

1. Any line that has a hash sign at the start is a preprocessor directive.
2. Include means add the declarations of the given library. In this case we are adding the declarations of the iostream library.
3. The brackets say “Look for this file in the directory where all the standard libraries are stored”. C++ also allows us to specify the library name using double quotes. The double quotes say “look in the current directory, if the file is not there, then look in the directory where the standard libraries are stored”.

```cpp
#include <iostream>

int main(){
    std::cout<<"Hey,world!"<<"try new line"<<"\n";
    return 0;
}
```

### namespace

When the commands are not explicitly defined, there is a possibility that when your code is added to a large project, your code might reference a command from a different library.

```cpp
#include <iostream>

using namespace std; // This tells the compiler to assume we are using the standard library, so we don’t have to write std::.
int main(){
    cout << "Hey, writing std:: is pain, ";
    return 0;
}
```

###

```cpp
g++ main.cpp -o main.out // to compile
// g++ for the c++ compiler
./main.out // run the output file
```

### Header files

```cpp
// header file, main.hpp
#include <iostream>
#include <string>

using namespace std;

// in the main.cpp
# include "main.hpp"
```

### User Input

In C++ we use `std::cout` for writing to the console.

And we have `std::cin` for reading from the console.

"g++", "-o main.out", "main.cpp"
"./main.out", stdin=open("input.txt", "r")
The first statement compiles the code and names the executable file main.out. Then main.out is executed using an input file called "input.txt".

These are the commands you would run if you were compiling and executing the program in a terminal.

```cpp
int main()
{
    int year = 0;
    int age = 0;
    std::string name = " ";
    //print a message to the user
    std::cout<<"What year is your favorite? ";

    //get the user response and assign it to the variable year
    std::cin >> year;

    //output response to user
    std::cout<<"How interesting, your favorite year is "<<year<<"!\n";
    std::cout<<"Tell me your nickname?: ";
    std::getline(std::cin, userName);
    return 0;
}
```

input.txt

```txt
1991
June Bug
```

std::cin will not retrieve strings that have a space in them. It will see the space as the end of the input.

getline: it will retrieve characters from the std::cin source and stores them in the variable called variableName. It will retrieve all characters until the newline or “\n” is detected. The programmer can also specify a different delimiter if the newline character is not desired.

# L3 Arithmetic Operations

M_PI is in the cmath library, it does not need to reference the
std namespace. On the other hand, pow() needs to reference it.

```cpp
 #include<iostream>
 #include <cmath>

 int main()
 {
     //Dimension of the cube
     float cubeSide = 5.4;
     //Dimension of sphere
     float sphereRadius = 2.33;
     //Dimensions of cone
     float coneRadius = 7.65;
     float coneHeight = 14;

     float volCube, volSphere, volCone = 0;

     //find volume of cube
     volCube = std::pow(cubeSide, 3);
     //find volume of sphere
     volSphere = (4.0/3.0)*M_PI*std::pow(sphereRadius,3);
     //find volume of cone
     volCone = M_PI * std::pow(coneRadius, 2) * (coneHeight/3);

     std::cout <<"\nVolume of Cube: "<<volCube<<"\n";
     std::cout <<"\nVolume of Sphere: "<<volSphere<<"\n";
     std::cout <<"\nVolume of Cone: "<<volCone<<"\n";
     return 0;
 }
```

C++ requires variable types to be known at compile time.

But, C++ does allow some implicit conversions, for example

-   assign an integer to a float
-   assign a char to a float/integer
-   assigning a float to a char doesn't quite work
-   assigning a float to an interger, results in the float being truncated

### PreFix and PostFix

Prefix operators increment the value of the variable, then return the reference to the variable.

Postfix operators create a copy of the variable and increments the value of the variable. Then it returns a copy from BEFORE the increment.

Incrementing

-   prefix: ++a
-   postfix: a++

Decrementing

-   prefix: --a
-   postfix: a--

# L4 Control Flow

### Logic Operators

1. && logical and
2. || logical or
3. ! logical not

# L5 Pointers

### Dereferencing

we have a pointer and want to access the value stored in that address, and it is indicated by adding the operator \* before the variable's name.

```cpp
 int a = 54;
 std::cout<< &a<<"\n"; //This will print the LOCATION of 'a'

// this is an integer variable with value = 54
int a = 54;

// this is a pointer that holds the address of the variable 'a'.
// if 'a' was a float, rather than int, so should be its pointer.
int * pointerToA = &a;

// If we were to print pointerToA, we'd obtain the address of 'a':
std::cout << "pointerToA stores " << pointerToA << '\n';

// If we want to know what is stored in this address, we can dereference pointerToA:
std::cout << "pointerToA points to " << * pointerToA << '\n';
```

```cpp
#include<iostream>
#include<string>

int main()
{
    std::string name;
    int givenInt;
    float givenFloat;
    double givenDouble;
    std::string givenString;
    char givenChar;
    int *pointerGivenInt;
    int **pointerPointerGivenInt;

    pointerGivenInt = &givenInt;
    pointerPointerGivenInt = &pointerGivenInt;

   //Get the values of each variable
    std::cout<<"integer = \n";
    std::cin>>givenInt;
    std::cout<<"float = \n";
    std::cin>>givenFloat;
    std::cout<<"double = \n";
    std::cin>>givenDouble;
    //We need to use cin.ignore so cin will ignore
   //the characters in the buffer leftover
   //from the givenDouble
    std::cin.ignore();
    std::cout<<"character = \n";
    std::cin>>givenChar;

    std::cout<<"string = \n";
    std::cin.ignore();
    std::getline (std::cin,givenString);


    //The value stored in the data
    std::cout<<"integer = "<<givenInt<<"\n";
    std::cout<<"float = "<<givenFloat<<"\n";
    std::cout<<"double = "<<givenDouble<<"\n";
    std::cout<<"string = "<<givenString<<"\n";
    std::cout<<"character = "<<(char)givenChar<<"\n\n";

    //The address of the data - use pointers
    std::cout<<"address integer = "<<&givenInt<<"\n";
    std::cout<<"address float = "<<&givenFloat<<"\n";
    std::cout<<"address double = "<<&givenDouble<<"\n";
    std::cout<<"address string = "<<&givenString<<"\n";
    std::cout<< "address character = " << (void *) &givenChar<<"\n\n";

   //Use indirection to the get the value stored at the address
    std::cout<< "pointer of givenInt = " << *pointerGivenInt<<"\n";
    std::cout<< "pointer of pointer of givenInt = " << **pointerPointerGivenInt<< "\n";

    return 0;
}
```

# L6 Arrays

# L15 C++ Checkpoint

```cpp
#include <iostream>

int main() {
  std::cout << "no more steering wheels" << std::endl;
  // std::endl a new line character, also flushes the buffer
  return 0;
}
```

```cpp
// Car.h
// Take a look at Car.cpp to see how to define the Car class.

// Hint: you'll need to define:
// 1. the class itself
// 2. the class constructor
// 3. one private property
// 4. three public methods

#ifndef CAR_H
#define CAR_H

class Car {
 public:
  Car();
  void wearAndTear();
  bool drive();
  void fix();
 private:
  bool in_working_condition_;
};

#endif  // CAR_H
The Car class is pretty straightforward. The trickiest part, I found, was making sure that the constructor was defined.

Note, the trailing _ on in_working_condition_ is common tactic for designating private properties in C++.

Ok! One more challenge to go.
```
