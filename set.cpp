#include<iostream>
#include<iomanip> // handle the format...
using namespace std;
int main()
{
    double pi = 3.1423344;
    cout<<"the pi value is:"<<pi<<endl;
    cout<<fixed<<setprecision(4);
    cout<<"the pi value is:"<<pi<<endl;
    cout<<"the value is:"<<"|"<<setw(8)<<pi<<"|"<<endl;
    cout<<"the value is:"<<"|"<<setw(20)<<pi<<"|"<<endl;
    bool done = true;
    cout<<"the status is :"<<done<<endl;
    bool done1 = false;
    cout<<"the status is :"<<done1<<endl;
    cout<<"the result is:"<<-1+6*4<<endl; // without bracket also okkk 
    cout<<"the result is:"<<23*33/3;
    


}