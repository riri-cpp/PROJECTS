#include <iostream>
#include <iomanip>
using namespace std;

void showBalance(double balances[], int accountNum);
double depositMoney(double balances[], int accountNum);
double withdrawMoney(double balances[], int accountNum);
int deleteAccount(double balances[], int activeAccounts, int accountNum);

int main(){
    cout << "\n******** WELCOME TO THE BANK ********\n";

    int totalAccounts;

    cout << "\nEnter total number of accounts: ";
    cin >> totalAccounts;

    double balances[totalAccounts] = {0};
    int activeAccounts = totalAccounts;
    int choice, accountNum;

    do{
        cout << "\nSAMPLE FORMAT - Account Number: [1]\n";
        cout << "\nPlease select an Account Number: ";
        cin >> accountNum;

        if (accountNum > totalAccounts || balances[accountNum-1] == -1){ 
            cout << "\nInvalid account number, please try again.\n";
            continue;
        }

        accountNum --;

        cout << "\nAccounts active: " << activeAccounts << '\n';
        cout << "Account Number: " << accountNum + 1 << '\n';
        cout << "\nWhat would you like to do?\n";
        cout << "Press [1] to View Balance\n";
        cout << "Press [2] to Deposit\n";
        cout << "Press [3] to Withdraw\n";
        cout << "Press [4] to Delete Current Account\n";
        cout << "Press [5] to Exit\n";
        cout << "Enter choice here: ";
        cin >> choice;

        cout << "\n------------------------\n";

        switch(choice){
            case 1:
                showBalance(balances, accountNum); 
                break;
            case 2:
                depositMoney(balances, accountNum);
                showBalance(balances, accountNum);  
                break;
            case 3:
                withdrawMoney(balances, accountNum);
                showBalance(balances, accountNum); 
                break;
            case 4:
                activeAccounts = deleteAccount(balances, activeAccounts, accountNum);
                cout << "\nActive accounts have been reduced to " << activeAccounts << '\n'; 
                break;
            case 5:
                cout << "Thank you for using the bank!\n";
                break;
            default:
                cout << "Invalid choice. Run program again\n";
                break;
        }

    }while(choice != 5 && activeAccounts > 0);

    if(activeAccounts <= 0){
        cout << "\nYou have no more accounts left!";
    }

    return 0;
}

void showBalance(double balances[], int accountNum){
    if(balances[accountNum] == -1){
        cout << "This account has already been deleted!";
    }
    cout << "\nTHE CURRENT BALANCE FOR ACCOUNT NUMBER " << accountNum + 1 << " is PHP " << setprecision(2) << fixed << balances[accountNum] << '\n';
}
double depositMoney(double balances[], int accountNum){
    int amount;
    cout << "\nSAMPLE FORMAT - [100] or [100.00]\n";
    cout << "\nEnter the amount you would like to deposit to this account: ";
    cin >> amount;

    if(balances[accountNum] == -1){
        cout << "This account has already been deleted!";
        return balances[accountNum];
    }
    else if(amount > 0){
        balances[accountNum] = balances[accountNum] + amount;
        cout << "\nYou have deposited PHP " << amount << " to Account Number " << accountNum + 1 << '\n'; 
        return balances[accountNum];
    }
    else{
        cout << "\nYou cannot deposit that amount!\n";
        return balances[accountNum];
    }
}
double withdrawMoney(double balances[], int accountNum){
    int amount;
    cout << "\nSAMPLE FORMAT - [100] or [100.00]\n";
    cout << "\nEnter the amount you would like to withdraw from this account: ";
    cin >> amount;

    if(balances[accountNum] == -1){
        cout << "This account has already been deleted!";
        return balances[accountNum];
    }
    else if(amount <= balances[accountNum]){ 
        balances[accountNum] = balances[accountNum] - amount;
        cout << "\nYou withdrew PHP " << amount << " from Account Number " << accountNum + 1 << '\n'; 
        return balances[accountNum];
    }
    else{
        cout << "\nYou cannot withdraw that amount!\n";
        return balances[accountNum];
    }
}
int deleteAccount(double balances[], int activeAccounts, int accountNum){
    
    if (accountNum < 0 || accountNum >= activeAccounts){
        cout << "\nThis is an invalid account number. Try again!\n";
        return activeAccounts;
    }

    balances[accountNum] = -1;
    cout << "\nAccount " << accountNum + 1 << " has been deleted.\n";

    activeAccounts--;
    return activeAccounts;
}