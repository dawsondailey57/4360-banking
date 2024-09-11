import sys
users = {
    "zeep": {"password": "Lemon4", "checking": 105.42, "savings": 162.32},
    "zorp": {"password": "Lime2", "checking": 150.0, "savings": 43.52},
    "glorp": {"password": "Orange7", "checking": 0.05, "savings": 0.01}
}
def login():
    failedLogins = 0
    while True:
        username = input("Enter your username: ").lower()
        password = input("Enter your password: ")

        # Check if username exists and password matches
        if username in users and users[username]["password"] == password:
            print(f"Welcome {username}.")
            return users[username]["checking"], users[username]["savings"]
        else:
            failedLogins += 1
            if failedLogins >= 3:
                print("You have reached the maximum number of failed logins. Try again later.")
                return None
            else:
                print("Invalid username or password. Please try again.\n")
            
            

def main():
    loginData = login()
    if loginData is None:
        return
    
    checking, savings = loginData
    transferAttempts = 0
    
    while True:
        print("\nOptions: /balance, /transfer, /withdraw, /quit")
        option = input("Enter your option: ").lower()
        if option == "/balance":
            accountChoice = input(f"\nWhich account do you want to check the balance of? (savings/checking)\n")
            if accountChoice == "checking":
                print(f"You have ${checking:.2f} in your checking account.")
            elif accountChoice == "savings":
                print(f"You have ${savings:.2f} in your savings account.")
            else:
                print("That is not a valid account name.")

        elif option == "/transfer":
            if transferAttempts < 3:
                transferAccount = input("Which account would you like to transfer money to (savings/checking)?\n")
            else:
                print("You have exceeded the maximum number of transfer attempts, you have been locked out.")
                break
            
            if transferAccount == "checking":
                transferAmount = float(input("How much money would you like to transfer from your savings account to your checking account?\n"))
                if savings >= transferAmount and transferAmount > 0:
                    savings -= transferAmount
                    checking += transferAmount
                    print(f"Your checking account now has ${checking:.2f}")
                else:
                    print("Invalid transfer amount.")    

            elif transferAccount == "savings":
                transferAmount = float(input("How much money would you like to transfer from your checking account to your savings account?\n"))
                if checking >= transferAmount and transferAmount > 0:
                    checking -= transferAmount
                    savings += transferAmount
                    print(f"Your savings account now has ${savings:.2f}")
                else:
                    print("Invalid transfer amount.")
            else:
                print("Invalid account choice.")
            transferAttempts += 1
            
        elif option == "/withdraw":
            accountChoice = input("\nWhich account do you want to withdraw from (savings/checking)?\n")
            if accountChoice == "checking":
                withdrawAmount = float(input("\nHow much money would you like to withdraw from your checking account?\n"))
                if withdrawAmount <= checking:
                    checking -= withdrawAmount
                    print(f"Enjoy your money.\nYour checking account now has ${checking:.2f}")
                else:
                    print("Invalid withdraw amount.")                    
                
            elif accountChoice == "savings":
                withdrawAmount = float(input("\nHow much money would you like to withdraw from your savings account?\n"))
                if withdrawAmount <= savings:
                    savings -= withdrawAmount
                    print(f"Enjoy your money.\nYour savings account now has ${savings:.2f}")
                else:
                    print("Invalid withdraw amount.")

            else:
                print("That is not a valid account name.")
            
        elif option == "/quit":
            print("\nGoodbye.")
            break

if __name__ == "__main__":
    main()