#include <iostream>
using namespace std;

void displayBalance(int balance){
    cout << "\nYour current balance is " << balance << " pesos.\n";
}

void displayColors(string colors[]){
    cout << "The available colors are: ";
    for(int i = 0; i < 6; i++){
        cout << colors[i] << ", ";
    };
}

int getColor(string myColor, string colors[]){
    for(int i = 0; i < 6; i++){
        if(colors[i] == myColor){
            return i;
        }
    }
    return -1;
}

int rollDice(){
    return rand() % 6;
}

void displayDice(int dice[], int diceCount, string colors[]){
    cout << "\nDice rolls: ";
    for(int i = 0; i < diceCount; i++){
        cout << colors[dice[i]] << " ";
    }
    cout << '\n';
}

int getMatches(int colorIndex, int dice[], int diceCount){
    int matches = 0;
    for (int i = 0; i < diceCount; ++i){
        if(dice[i] == colorIndex){
            matches++;
        }
    }
    return matches++;
}

int getWinnings(int betAmount, int matches){
    return betAmount * matches;
}

int main(){
    string colors[6] = {"Red", "Blue", "Yellow", "Green", "White", "Violet"};
    int balance;
    string myColor;
    int betAmount;
    char playAgain;

    cout << "Enter your starting balance: ";
    cin >> balance;
    
    srand(time(0));

    do{

        cout << "WELCOME TO COLOR GAME!\n";
        cout << "**********************\n";

        displayBalance(balance);
        displayColors(colors);

        cout << "\nEnter the color you want to bet on: ";
        cin >> myColor;

        int colorIndex = getColor(myColor, colors);
        if(colorIndex == -1){
            cout << "That is an invalid choice. Please choose among the six colors.\n";
            continue;
        }

        cout << "\nEnter the amount you want to bet on: ";
        cin >> betAmount;

        if(betAmount > balance){
            cout << "You do not have enough money to make that bet.\n";
            continue;
        }

        balance = balance - betAmount;

        int dice[3];
        for(int i = 0; i < 3; i++){
            dice[i] = rollDice();
        }

        displayDice(dice, 3, colors);

        int matches = getMatches(colorIndex, dice, 3);
        int winnings = getWinnings(betAmount, matches);

        if(matches == 0){
            cout << "\nNo color matched! You lost " << betAmount << " pesos\n"; 
        }
        else{
            balance += betAmount + winnings;
            cout << "\nCongratulations! You matched " << matches << " dice(s) and won " << winnings << " pesos\n";
        }

        displayBalance(balance);

        if(balance <= 0){
            cout << "\nYou have no more money left! Game over.\n";
            break;
        }

        cout << "\nPress [Y] to play again: ";
        cin >> playAgain;

        cout << '\n';
    }while(playAgain == 'y' || playAgain == 'Y');

    cout << "Thank you for playing!";
    return 0;
}