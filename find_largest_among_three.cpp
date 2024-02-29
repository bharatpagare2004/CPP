// find the largest number among three numbers
#include<iostream>
using namespace std;
int main()
{
    int a,b,c;
    cout<<"\nenter the value of a , b , c:";
    cin>>a>>b>>c;
    // by using add 
    if(a==b && b==c && a==c)
         cout<<"the three number is same:"<<a;
    else if(a>=b && a>=c) 
        cout<<"the largest number is:"<<a;
    else if(b>=a && b>=c)
      cout<<"the largest number is:"<<b;
    else if(c>=a && c>=b)
       cout<<"the largest number is:"<<c;
   
       return 0;  
}