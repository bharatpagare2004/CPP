#include<iostream>
using namespace std;
void swap(int*x ,int*y);
int main()
{
    int a = 10;
    int b = 20;
    swap(&a,&b); // actual parameter.

}
void swap(int*x,int*y) // formal parameter
{
    cout<<"Before"<<endl;
    cout<<"the value of x:"<<*x<<endl;
    cout<<"the value of y:"<<*y<<endl;
    int t;
    t = *x;
    *x = *y;
    *y = t;
     cout<<"Before"<<endl;
    cout<<"the value of x:"<<*x<<endl;
    cout<<"the value of y:"<<*y<<endl;

}