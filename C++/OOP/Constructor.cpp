#include<bits/stdc++.h>  
using namespace std;  

class student
{
   public:  
   int cls;  //4 byte
   int roll;
   double gpa; //8 byte

student(int r, int c, double g)
{
    
     roll = r;  
     cls = c;  
     gpa = g;  

}

};

int main()
{

    student rahim (45,7,5.00);  
    student karim (2,5,4.94);  

    cout << rahim.roll << " " << rahim.cls << " " << rahim.gpa << endl;  
     cout << karim.roll << " " << karim.cls << " " << karim.gpa << endl;  

    
    return 0;
}