# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    ##Savings
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    #ask the user to enter the balance and check if it is a digit
    while True:
       savings_balance = input("Please input the balance of you savings account!") 
       if savings_balance.isdigit:
            break
       else: "Error! Please enter a digit"
    #ask the user to enter the interest rate and check if it is a digit   
    while True:
       savings_interest = input("Please input the balance of you savings account!") 
       if savings_interest.isdigit() and int(savings_interest) > 0:
            break
       else: 
           print("Error! Please enter a positive integer.")
    #ask the user to enter the months and check if it is a digit   
    while True:
        savings_maturity = input("Please input the months for the savings account: ")
        if savings_maturity.isdigit() and int(savings_maturity) > 0:
            savings_maturity = int(savings_maturity)
            break
        else:
            print("Error! Please enter a positive integer.")
   
    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity) 
    
    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Your updated savings balance after the maturity of {savings_maturity} months is ${updated_savings_balance:,.2} ")
    print(f"Interest earned on CD: ${interest_earned:,.2f}")
    
    
    
    ##CD --------------------------------------------------------
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    #ask the user to enter the balance and check if it is a digit
    while True:
       cd_balance = input("Please input the balance of you savings account!") 
       if cd_balance.isdigit:
            break
       else: "Error! Please enter a digit"
    #ask the user to enter the interest rate and check if it is a digit   
    while True:
       cd_interest = input("Please input the balance of you savings account!") 
       if cd_interest.isdigit() and int(cd_interest) > 0:
            break
       else: 
           print("Error! Please enter a positive integer.")
    #ask the user to enter the months and check if it is a digit   
    while True:
        cd_maturity = input("Please input the months for the savings account: ")
        if cd_maturity.isdigit() and int(cd_maturity) > 0:
            cd_maturity = int(cd_maturity)
            break
        else:
            print("Error! Please enter a positive integer.")
    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Your updated CD balance after the maturity of {cd_maturity} months is ${updated_cd_balance:,.2} ")
    print(f"Interest earned on CD: ${interest_earned:,.2f}")
if __name__ == "__main__":
    # Call the main function.
    main()
