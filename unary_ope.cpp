#include<iostream>
using namespace std;
class Dis
{   public:
    int inch,feet;
    Dis(int x , int y)
    {
        this-> feet = x;
        this ->inch = y;
    }
    void operator -()
    {
        feet--;
        inch--;
        cout<<"\nthe feet is:"<<feet;
        cout<<"\nthe inch is:"<<inch;
    }
    
};
int main(){
    Dis p(12,23);
    -p;
    return 0 ;
}
