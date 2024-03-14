users = {}
balances = {}

def create_user(username):
    users[username] = {"user_id": len(users), "username": username}
    balances[username] = 0 #initialize balances to zero
    return users.get(username)

def get_user(username):
    return users.get(username)

def get_balance(username):
    return balances.get(username)

def deposit(username, amount):
    balances[username] +=amount

def withdraw(username, amount):
    if balances[username] >= amount:
        balances[username] -= amount
        return True
    return False

def send_funds(sender_username, receiver_username, amount):
    sender_balance = get_balance(sender_username)
    receiver_balance = get_balance(receiver_username)

    if sender_balance is None:
        return {'error': 'Sender not found'}, 404
    elif receiver_balance is None:
        return {'error': 'Receiver not found'}, 404
    elif sender_balance < amount:
        return {'error': 'Insufficient funds'}, 400
    else:
        withdraw(sender_username, amount)
        deposit(receiver_username, amount)
        return {'message': 'Funds sent successfully',
                'sender_balance': get_balance(sender_username),
                'receiver_balance': get_balance(receiver_username)}, 200
