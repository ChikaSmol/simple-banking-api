from flask import Flask, request, jsonify
from userData import (create_user as create_user_func,
                      get_user,
                      get_balance as get_balance_func,
                      deposit as deposit_func,
                      withdraw as withdraw_func,
                      send_funds)

app = Flask(__name__)

# Endpoint to create a user
@app.route('/create_user', methods=['POST'])
def create_user_route(): 
    data = request.json
    username = data.get('username')
    user = create_user_func(username)
    if user:
        return jsonify({'message': 'User has been created successfully', "user": username}), 201
    else:
        return jsonify({'error': 'Username is required'}), 400

# Endpoint to get user details
@app.route('/get_user/<username>', methods=['GET'])
def get_user_route(username):
    user = get_user(username)
    print(user)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    return jsonify({'user': user}), 200

# Endpoint to deposit funds
@app.route('/deposit', methods=['POST'])
def deposit_route():
    data = request.json
    username = data.get('username')
    amount = data.get('amount')
    if username is None or amount is None:
        return jsonify({'error': 'Username and amount are required'}), 400
    try:
        amount = float(amount)
    except ValueError:
        return jsonify({'error': 'Invalid amount'}), 400
    
    deposit_func(username, amount)
    return jsonify({'message': 'Deposit successful', 'balance': get_balance_func(username)}), 200

# Endpoint to withdraw funds
@app.route('/withdraw', methods=['POST'])
def withdraw_route():
    data = request.json
    username = data.get('username')
    amount = data.get('amount')
    if username is None or amount is None:
        return jsonify({'error': 'Username and amount are required'}), 400
    try:
        amount = float(amount)
    except ValueError:
        return jsonify({'error': 'Invalid amount'}), 400
    
    if withdraw_func(username, amount):
        return jsonify({'message': 'Withdrawal successful', 'balance': get_balance_func(username)}), 200
    else:
        return jsonify({'error': 'Insufficient funds or invalid username'}), 400

# Endpoint to get account balance
@app.route('/get_balance/<username>', methods=['GET'])
def get_balance_route(username):
    if username:
        balance = get_balance_func(username)
        if balance is not None:
            return jsonify({'balance': balance}), 200
        else:
            return jsonify({'error': 'User not found'}), 404
    else:
        return jsonify({'error': 'Username is required'}), 400

# Endpoint to send funds
@app.route('/send_funds', methods=['POST'])
def send_funds_route():
    data = request.json
    sender_username = data.get('sender')
    receiver_username = data.get('receiver')
    amount = data.get('amount')
    if sender_username and receiver_username and amount:
        try:
            amount = float(amount)
        except ValueError:
            return jsonify({'error': 'Invalid amount'}), 400
        
        result, status_code = send_funds(sender_username, receiver_username, amount)
        return jsonify(result), status_code
    else:
        return jsonify({'error': 'Sender, receiver, and amount are required'}), 400

if __name__ == '__main__':
    app.run(debug=True)
