# MoMo-Analysis-Assignment-Group-16_-SUMMATIVE-
Summative Assignment - MoMo Data Analysis

Ok Good evening Mr David Neza Tuyishimire, I received your email, and here is how you can run my project.

Step 1: Install the Necessary Software
Before running the program, ensure you have these installed:
- Python 3 (Check using: python --version)
- pip (Check using: pip --version)
- Flask (Install using: pip install flask flask-cors)

- 
Step 2: Download and Open the Project
1. Download the project ZIP file.
2. Extract it to a folder on your computer.
3. Open Terminal or Command Prompt and move into the project folder:


Step 3: Set Up the Database
The system will store data in a database. To create it:
1. Move into the Backend folder:
 (cd Backend)
2. Run the script to set up the database:
 (python database.py)


Step 4: Process and Insert Data
Now, you will extract and store transaction data:
1. Extract data from SMS messages:
 (python process_sms.py)
2. then Insert the extracted data into the database:
 (python data_insertion.py)


Step 5: Start the Backend API
The backend handles data and sends it to the frontend. To start it:
 (python api.py)
If it is successful, the API will run at: http://127.0.0.1:5000/transactions


Step 6: Open the Frontend
1. Go to the Frontend folder.
2. Open index.html in a web browser.
3. The page should display transaction records and a chart.

For troubleshooting Sir,if the Flask API fails to start, ensure Flask is installed and that port 5000 is free. If transactions do not appear, check sms_data.xml for messages and review unprocessed_sms.log for errors. If charts fail to load, inspect the Developer Console and confirm that Chart.js is correctly linked.
