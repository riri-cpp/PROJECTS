#include <iostream>

using namespace std;

int main() {

    char op;
    double num1;
    double num2;


    cout << "Enter your desired operation (+, -, *, or /): ";
    cin >> op;

    cout << "Enter the first number: ";
    cin >> num1;

    cout << "Enter the second number: ";
    cin >> num2;

    switch(op){
        
        case '+':
    
            std::cout << "The sum is " << num1 + num2 << '\n';
            break;
        case '-':
        
            std::cout << "The difference is " << num1 - num2 << '\n';
            break;
        case '*':
         
            std::cout << "The product is " << num1 * num2 << '\n';
            break;
        
        case '/':
          
            try{
                
                if(num2 == 0){
                    throw num2;
                }
                std::cout << "The quotient is " << num1 / num2 << '\n';
                
            }catch (double ex){
                cout << "Division by zero is not posssible" << endl;
            }
            break;
            
        default:
            std::cout << "Invalid input, calculator failed." << '\n';
            break;
    }

 
    return 0;
}