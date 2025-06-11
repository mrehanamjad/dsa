#include <iostream>
using namespace std;

int main(){

// pridict the out put:
int a = 5;
int *p = &a;
int **q = &p;

cout << *p << endl;  // 5
cout << **q << endl; // 5
cout << p << endl; // address of a
cout << *q << endl; // address of a

int x = 2;
int* y = &x;
int* z = y;
cout << x << " - "<< y << " - " << z << endl;

}