class ATM:
    def __init__(self, account_data):
        self.account_data = account_data

    def display_balance(self, account_id):
        account = self.account_data.get(account_id)
        if account:
            return f"Current Balance: ${account['balance']:.2f}"
        else:
            return "Account does not exist!"

    def withdraw_cash(self, account_id, amount):
        account = self.account_data.get(account_id)
        
        if not account:
            return "error!"
        
        if amount < 0:
            return "error!"
        
        if amount > account['balance']:
            return "error!"
        
        if amount > account['daily_limit']:
            return f"error{account['daily_limit']:.2f}."
        
        account['balance'] -= amount
        account['daily_limit'] -= amount

        return f"${amount:.2f}\nNew Balance: {account['balance']:.2f}"

accounts = {
    101: {'balance': 500.00, 'daily_limit': 300.00},
}

atm = ATMSystem(accounts)


print(atm.display_balance(101))

amount_to_withdraw = 100  
result = atm.withdraw_cash(101, amount_to_withdraw)
print(result)

print(atm.display_balance(101))