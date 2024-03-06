#include<iostream>
using namespace std;
int main()
{
    float f = 3.4;   
    int g = 1+ (int)f; // this is explicit type conversion
    cout<<"g:"<<g;

    int t = 10;
    char u = 't';
    int sum;
    sum = t+u; // implicit type conversion....
    cout<<"\nthe sum is:"<<sum<<endl;
    return 0 ;

}