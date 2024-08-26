
package FinalKeyword;
public class University {
   
    final String UNIVERSITY_NAME ="BUBT";
    static final int fees;// static blank final variable
    
    static{
        fees = 67000;  
    }
    
    void display(){
        System.out.println(UNIVERSITY_NAME);
        System.out.println(fees);
        
    }
    
}
