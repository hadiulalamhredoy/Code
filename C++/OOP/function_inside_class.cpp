#include<bits/stdc++.h> 
using namespace std;    

class student
{
     public:  
     string name;  
     int roll;    
     int math;  
     int phy;
    
     student(string name, int roll,int math,int phy)
     {  
        this->name = name;  
        this->roll = roll; 
        this->math = math;
        this->phy = phy; 
        cout<<"Name: "<<this->name<<endl;
          

     }

    //  void hello()
    //  {
    //     cout << "Hello From" << name << endl;
    //  }

     void total_marks()
     {
        int total = math + phy;
        cout << "Total Marks: " << total << endl;
     }

};

int main()
{

     student sakib ("sakib ahmed",22,85,92);
    //  cout << sakib.name << endl;
    //  cout << sakib.roll << endl;
        sakib.total_marks();

     return 0;  
}   
