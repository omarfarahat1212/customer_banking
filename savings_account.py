"""Imports the SavingsAccount class and attributes from the Account.py file."""
# ADD YOUR CODE HERE
from Accounts import Account

# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    interest = 0
    Account.balance()
    Account.interest()

    # Calculate interest earned
     # ADD YOUR CODE HERE
    
    interest = float(balance * (interest_rate/100 * months/12))
    # Update the savings account balance by adding the interest earned
    # ADD YOUR CODE HERE
    new_balance = float(balance + interest)
    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    Account.set_balance(new_balance)
    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    Account.set_interest(interest)
    # Return the updated balance and interest earned.
    return new_balance and interest # ADD YOUR CODE HERE
