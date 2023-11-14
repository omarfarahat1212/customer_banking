# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from savings_account import create_savings_account
from cd_account import create_cd_account


def get_user_input(prompt, data_type):
        """Get user input and validate it.
        
        Arguments
        prompt = the user input 
        data_type = Is the data type requested to cast the variable "prompt"
        
        """
        while True:
             user_input = input(prompt)
             if data_type == 'float' and user_input.replace('.', '', 1).isdigit():
                  return float(user_input)
             elif data_type == 'int' and user_input.isdigit():
                    return int(user_input)
             else:
                  print("Error! Please enter a valid number.")
        
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

    savings_balance = get_user_input("Please input the balance of your savings account: ", 'float')
    savings_interest = get_user_input("Please input the interest of your savings account: ", 'float')
    savings_maturity = get_user_input("Please input the months for the savings account: ", 'int')
   
    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity) 
    
    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Your updated savings balance after the maturity of {savings_maturity} months is ${updated_savings_balance:,.2f} ")
    print(f"Interest earned on Savings account is: ${interest_earned:,.2f}")
    
    
    
    ##CD --------------------------------------------------------
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    #ask the user to enter the balance and check if it is a digit
    cd_balance = get_user_input("Please input the balance of your CD: ", 'float')
    cd_interest = get_user_input("Please input the interest of your CD account: ", 'float')
    cd_maturity = get_user_input("Please input the months for the CD account: ", 'int')
    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)
    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Your updated CD balance after the maturity of {cd_maturity} months is ${updated_cd_balance:,.2f} ")
    print(f"Interest earned on CD: ${interest_earned:,.2f}")
if __name__ == "__main__":
    # Call the main function.
    main()
