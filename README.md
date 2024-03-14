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

3. Run a python local environment with this command:

   ```bash
   pipenv shell
   ```

4. Install the required dependencies:

   ```bash
   pip install flask
   ```

## Usage

1. Start the Flask server:

   ```bash
   python main.py
   ```

2. Use the following endpoints to interact with the API:
   - `POST /create_user`: Create a new user with a username.
   - `GET /get_user/<username>`: Get details of a specific user.
   - `POST /deposit`: Deposit funds into a user's account.
   - `POST /withdraw`: Withdraw funds from a user's account.
   - `GET /get_balance/<username>`: Get the account balance of a user.
   - `POST /send_funds`: Send funds from one user to another.

## Functional Testing

The project includes functional tests to ensure the correctness of the API endpoints. You can run the tests using the following command:

```bash
python3 -m unittest test.py -v
```

## Non-Functional Testing

The project also does not include non-functional test cases for performance, security, reliability, usability, and compatibility. These test cases are documented in the testCases.md file.
