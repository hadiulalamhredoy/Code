#include<bits/stdc++.h> 
using namespace std;    

class cricketer
{
     public:  
     string country;  
     int jersey;
     
    
    cricketer(string country, int jersey)
     {  
        this->country = country;  
        this->jersey = jersey;  

     }
     
          

};

int main()
{
     cricketer* dhoni = new cricketer ("India",7);
     cricketer* kohli = new cricketer ("India",18); 
     cout << dhoni->country << " " << dhoni->jersey << endl;   
    cout << kohli->country << " " << kohli->jersey << endl; 

     return 0;  
}   
