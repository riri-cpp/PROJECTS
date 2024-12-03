#include <iostream>

using namespace std;

int main () {

    int num;
    int guess;
    int tries;

    srand(time(NULL));
    num = rand() % 100 + 1;

    cout << "WELCOME TO YOUR NUMBER GUESSING GAME!" << endl;
    
    do{

        cout << "Guess a number from 1 to 100: ";
        cin >> guess;
        tries ++;

        if(guess > num){

            cout << "Too high!" << endl;

        }
        else if(guess < num){

            cout << "Too low!" << endl;

        }
        else{

            cout << "CORRECT! The random number is " << num << endl;
            cout << "Number of tries: " << tries << endl;

        }

    }while(guess != num);

    cout << "THANK YOU FOR PLAYING";

    return 0;
}