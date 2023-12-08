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
