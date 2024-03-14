# Simple Banking API

This is a simple banking API built with Flask. It provides endpoints for creating users, depositing funds, withdrawing funds, checking account balances, and sending funds between users.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/simple-banking-api.git
   ```

2. Navigate to the project directory:

   ```bash
   cd simple-banking-api
   ```

3. Make sure you have system setup for python development recommended version: python3

4. Run a python local environment with this command:

   ```bash
   pipenv shell
   ```

5. Install the required dependencies:

   ```bash
   pip install flask
   ```

## Usage

1. Start the Flask server:

   ```bash
   python main.py
   ```

2. Use the following endpoints to interact with the API using curl, insomia or postman or by simply running test.py file:
   - `POST /create_user`: Create a new user with a username.
      sample curl request:
      ```bash
         curl --request POST \
         --url http://127.0.0.1:5000/create_user \
         --header 'Content-Type: application/json' \
         --data 
         '{"username": "user1" }'
      ```
   - `GET /get_user/<username>`: Get details of a specific user.
      sample curl request:
         ```bash
            curl --request GET \
            --url http://127.0.0.1:5000/get_user/<user1> \
         ```
   - `POST /deposit`: Deposit funds into a user's account.
      sample curl request:
      ```bash
         curl --request POST \
         --url http://127.0.0.1:5000/deposit \
         --header 'Content-Type: application/json' \
         --data '{
	         "username":"user1",
	         "amount": 40}'
      ```
   - `POST /withdraw`: Withdraw funds from a user's account.
      sample curl request:
      ```bash
         curl --request POST \
         --url http://127.0.0.1:5000/withdraw \
         --data '{
	         "username":"user1",
	         "amount": 10}'
      ```
   - `GET /get_balance/<username>`: Get the account balance of a user.
      sample curl request:
      ```bash
         curl --request GET \
         --url 'http://127.0.0.1:5000/get_balance/paul?username=chika' \
         --header 'Content-Type: application/json' \
      ```
   - `POST /send_funds`: Send funds from one user to another. Before sending this request, create a new user
      sample curl request:
      ```bash
         curl --request POST \
         --url http://127.0.0.1:5000/send_funds \
         --header 'Content-Type: application/json' \
         --data '{
	         "sender":"user1",
	         "receiver":"user2",
	         "amount": 10 }'
      ```

## Functional Testing

The project includes functional tests to ensure the correctness of the API endpoints. You can run the tests using the following command:

```bash
python3 -m unittest test.py -v
```

## Non-Functional Testing

The project also does not include non-functional tests in code. The test cases are only documented in the testCases.md file.
