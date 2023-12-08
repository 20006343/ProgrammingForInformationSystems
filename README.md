# ProgrammingForInformationSystems
- A repository for hosting code for a Management Information System
- The chosen Information System is - A Retail Store Management Information System
  
# How to Run
- Install a MySQL database instance. The test server used is the XAMPP server but any MySQL instance will work
- Create a MySQL user and set a password.
- Create a test database
- Clone the repository or Download as a ZIP
- Edit the config.py file and enter the host, user, password, database and port details from your MySQL instance
- Depending on your python version install the requirements using the command pip install -r requirements.txt
- Run the app.py file by using the command python app.py
- This will start the application on the address http://127.0.0.1:105 with two routes described below
    -   a normal (/) route for serving the html files
    -   an (/api) route which is an API for interacting with the backend 
- Navigate to the address on your browser
- A test user for login is created by default with the following details
   -  username: test
   -  password: test123

# Interfaces after Running
- Login Page
  ![login page](https://github.com/20006343/ProgrammingForInformationSystems/blob/main/sampleruns/login.png?raw=true)

- Owner Dashboard
  ![owner page](https://github.com/20006343/ProgrammingForInformationSystems/blob/main/sampleruns/dashboard.png?raw=true)


- Add / View User Information
    ![user page](https://github.com/20006343/ProgrammingForInformationSystems/blob/main/sampleruns/users.png?raw=true)

- Add / View Employee Information
    ![employee page](https://github.com/20006343/ProgrammingForInformationSystems/blob/main/sampleruns/employee.png?raw=true)

- Add / View Supplier Information
    ![supplier page](https://github.com/20006343/ProgrammingForInformationSystems/blob/main/sampleruns/supplier.png?raw=true)
  
- Add / View Product Information
  ![product page](https://github.com/20006343/ProgrammingForInformationSystems/blob/main/sampleruns/product.png?raw=true)

- Add / View Stock Information
    ![stock page](https://github.com/20006343/ProgrammingForInformationSystems/blob/main/sampleruns/stock.png?raw=true)
  
