from fastmcp import FastMCP

mcp = FastMCP("Custom Server")

data = {
    'amount': 50000
}

def validate_number(*args):
    return [int(values) for values in args]

@mcp.tool(name='make_payment', description='This is a tool used to make payments or purchase things. MUST take an interger \'amount\' as an argument.')
def make_payment(amount: int | str) -> str:
    amount = validate_number(amount)
    
    """This is a tool used to make payments or purchase things. MUST take an interger 'amount' as an argument."""
    if amount[0] > data['amount']:
        return f"You have only {data['amount']} cash."
    
    data['amount'] -= amount[0]
    return f"{amount[0]} debited from your account. Current amount {data['amount']}."

@mcp.tool(name='add_amount', description="This is a tool used to add amount to back account. Takes three argument - 'amount', 'card_number', 'cvv' all of three MUST be integers.")
def add_amount(amount: int | str, card_number: int|str, cvv: int | str) -> str:
    """This is a tool used to add amount to back account. Takes three argument - 'amount', 'card_number', 'cvv' all of three MUST be integers."""
    amount, card_number, cvv = validate_number(amount, card_number, cvv)

    if card_number and cvv:
        print("validated")

    data['amount'] += amount
    return f"{amount} added to user bank account successfully. Updated amount {data['amount']}"

@mcp.tool(name='add_payment_history', description="This is function used to store all the payments history in data variable. Were 'history' is a meaningfull argument of payments that user have made.")
def add_payment_history(history: str) -> str:
    """This is function used to store all the payments history in data variable. Were 'history' is a meaningfull argument of payments that user have made."""

    data['payment_history'] = history
    return "Payment history updated."

@mcp.tool(name='display_information', description='This is tools used to display information of user.')
def display_account_info():
    """This is tools used to display information of user."""
    return data