#TEST CASES FOR ENDPOINTS
- [Funtional Test Cases](##Functional Test Cases)
- [Non Functional Test Cases](##Non Functional Test Cases)


##Functional Test Cases
| Endpoint         | Test Case                          | Description                                          | Steps                                                                                           | Expected Result                                           |
|------------------|------------------------------------|------------------------------------------------------|-------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| Create User      | Create User Successfully          | Test creating a new user with a valid username.      | 1. Send a POST request to `/create_user` with a valid username.                                 | User is created successfully.                            |
|                  | Missing Username                   | Test creating a new user without providing a username. | 1. Send a POST request to `/create_user` without providing a username.                          | Error is returned indicating that the username is required. |
| Get User         | Get Existing User                  | Test getting details of an existing user.            | 1. Send a GET request to `/get_user/<username>` with the username of an existing user.         | Details of the existing user are returned successfully.   |
|                  | Get Non-existent User              | Test getting details of a user that does not exist.  | 1. Send a GET request to `/get_user/<username>` with the username of a non-existent user.      | Error is returned indicating that the user was not found. |
| Deposit          | Deposit Successfully               | Test depositing funds into an existing user's account. | 1. Send a POST request to `/deposit` with a valid username and amount.                          | Funds are deposited successfully into the user's account. |
|                  | Missing Username                   | Test depositing funds without providing a username.  | 1. Send a POST request to `/deposit` without providing a username.                               | Error is returned indicating that the username is required. |
| Withdraw         | Withdraw Successfully              | Test withdrawing funds from an existing user's account. | 1. Send a POST request to `/withdraw` with a valid username and amount.                        | Funds are withdrawn successfully from the user's account. |
|                  | Insufficient Funds                 | Test attempting to withdraw more funds than the user has. | 1. Send a POST request to `/withdraw` with a valid username and an amount exceeding the balance. | Error is returned indicating insufficient funds or an invalid username. |
| Get Balance      | Get Balance Successfully          | Test getting the balance of an existing user's account. | 1. Send a GET request to `/get_balance/<username>` with the username of an existing user.      | User's balance is returned successfully.               |
|                  | Get Balance of Non-existent User  | Test getting the balance of a user that does not exist. | 1. Send a GET request to `/get_balance/<username>` with the username of a non-existent user.  | Error is returned indicating that the user was not found. |
| Send Funds       | Send Funds Successfully           | Test sending funds from one user to another.          | 1. Create sender and receiver users.<br>2. Deposit funds into the sender's account.<br>3. Send funds from the sender to the receiver. | Funds are sent successfully from the sender to the receiver. |
|                  | Invalid Amount                    | Test attempting to send funds with an invalid amount. | 1. Create sender and receiver users.<br>2. Deposit funds into the sender's account.<br>3. Send funds from the sender to the receiver with an invalid amount. | Error is returned indicating an invalid amount.        |


##Non Functional Test Cases
### Performance Testing
| Test Case | Description | Steps | Expected Result |
|-----------|-------------|-------|-----------------|
| Load Testing | Test the application's ability to handle a high volume of concurrent users. | 1. Use a load testing tool to simulate a large number of concurrent users.<br>2. Send requests to various endpoints at different load levels.<br>3. Monitor response times, throughput, and server resources. | The application should handle the load gracefully without significant degradation in performance or errors. |
| Stress Testing | Test the application's stability under stress by pushing it beyond its capacity. | 1. Use a stress testing tool to increase the load gradually.<br>2. Monitor the application's behavior and response times.<br>3. Observe how the application recovers from spikes in traffic or resource exhaustion. | The application should gracefully degrade or fail under extreme stress, with proper error handling and recovery mechanisms. |

### Security Testing

| Test Case | Description | Steps | Expected Result |
|-----------|-------------|-------|-----------------|
| Authentication and Authorization | Test the authentication and authorization mechanisms of the application. | 1. Attempt to access protected endpoints without proper credentials.<br>2. Attempt to access protected endpoints with incorrect authorization.<br>3. Verify that unauthorized access is denied and proper error messages are returned. | Unauthorized users should not be able to access protected resources, and proper error messages should be returned. |

### Reliability Testing

| Test Case | Description | Steps | Expected Result |
|-----------|-------------|-------|-----------------|
| Error Handling | Test the application's error handling mechanisms under various scenarios. | 1. Introduce intentional errors in the request payloads or parameters.<br>2. Send requests with missing or invalid data to the endpoints.<br>3. Verify that the application returns meaningful error messages and handles exceptions gracefully. | The application should provide informative error messages and handle exceptions without crashing or exposing sensitive information. |

### Usability Testing

| Test Case | Description | Steps | Expected Result |
|-----------|-------------|-------|-----------------|
| User Interface Testing | Test the usability and intuitiveness of the application's user interface. | 1. Navigate through the application's user interface to perform common tasks.<br>2. Evaluate the layout, design, and responsiveness of the user interface.<br>3. Verify that the user interface provides clear feedback and guidance to users. | The user interface should be user-friendly, intuitive, and easy to navigate. |

### Compatibility Testing

| Test Case | Description | Steps | Expected Result |
|-----------|-------------|-------|-----------------|
| Browser Compatibility | Test the compatibility of the application with different web browsers. | 1. Access the application using popular web browsers (Chrome, Firefox, Safari, Edge, etc.).<br>2. Verify that all features and functionalities work as expected across different browsers. | The application should render correctly and function consistently across different web browsers. |
