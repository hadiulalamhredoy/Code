#include<bits/stdc++.h>  
using namespace std;  

class student
{
   public:  
   int roll;
   int cls;  
   double gpa; 

student(int roll, int cls, double gpa)
{
    
     this->roll = roll;  
     this->cls = cls;  
     this->gpa = gpa;  
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