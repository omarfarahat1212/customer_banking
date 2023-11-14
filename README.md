# Savings and CD Account Interest Calculator

## Description
This Python application allows users to calculate the interest earned on savings and certificate of deposit (CD) accounts. It prompts users to enter account details such as balance, interest rate, and maturity period in months. The application then computes and displays the updated balance and interest earned for both savings and CD accounts.

## Installation
No installation is required. You can run this script in a Python environment.

## Requirements
- Python 3.x

## Usage
To use this application, follow these steps:
1. Run the script in a Python environment.
2. Enter the balance, interest rate, and maturity period for the savings account when prompted.
3. Enter the balance, interest rate, and maturity period for the CD account when prompted.
4. The application will display the updated balance and interest earned for both accounts.

### Account
The `Account` class represents a financial account. It includes methods to set and retrieve the account's balance and interest rate.
- `__init__(self, balance, interest)`: Initializes a new account instance with a given balance and interest rate.
- `set_balance(self, balance)`: Sets the account's balance.
- `set_interest(self, interest)`: Sets the account's interest rate.

## Functions
- `get_user_input(prompt, data_type)`: This function gets and validates user input based on the specified data type, int or float.
- `create_savings_account(savings_balance, savings_interest, savings_maturity)`: Calculates the updated balance and interest for the savings account.
- `create_cd_account(cd_balance, cd_interest, cd_maturity)`: Calculates the updated balance and interest for the CD account.

## Account Class

The `Account` class is a fundamental component of our application, designed to represent a bank account with basic functionalities. This class includes methods to manage the account balance and interest rates.

### Features

- **Initial Balance and Interest Setup**: Upon creating an instance of the `Account` class, you can initialize it with a specific balance and interest rate.
- **Balance Management**: Easily modify the account's balance using the `set_balance` method.
- **Interest Rate Management**: Adjust the interest rate of the account using the `set_interest` method.
### Usage

#### Creating an Account Instance
To create an account, simply provide the initial balance and interest rate:
```python
new_account = Account(balance, interest)
```


## Recommendations for Future Use
- **User Interface:** Consider developing a user-friendly graphical interface to enhance user experience.
- **Extended Financial Features:** Add features such as compound interest calculations, different account types, and financial forecasting tools.
- **Security Enhancements:** Ensure sensitive data protection with encryption and secure data handling practices.
