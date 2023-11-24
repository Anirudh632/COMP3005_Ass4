# COMP3005_Ass4

**Video Description:**
Youtube Link - https://youtu.be/2UIUWEUmXC8

**Setup Instuctions for the Database:**
1. Open Pgadmin on your system
2. Create a Database with a name of your choice
3. Run the ass4q1.sql file to create the 'students' table and populate it with the intial data

**Steps to compile and run the application:**
1. Install the psycopg2 library on your system using the following commands on your terminal:
    pip install psycopg2
    pip install psycopg2-binary
2. Open ass4q1.py in the code editor of your choice (I used VS Code). Ensure your python interpreter is set to the environment where you installed the libraries in       the last step.
3. Update the db_params and populate the required fields with your Database Name, Postgres Username and Password.
4. Run the Code by updating the main() as you would like.(More information in the Video)

**A brief Explaination of each function:**
I have created a python application, with the help of online resources such as google and chatGPT, with the following functions:
1. connect(): This function connects to your Database using the provided db_params.
2. getAllStudents(): Retrieves and displays all records from the students table.
3. addStudent(): Inserts a new student record into the students table with the information passed as the function's arguments
4. updateStudentEmail(): Updates the email address for a student with the student_id passed as the argument of the function.
5. deleteStudent(): Deletes the record of the student with the student_id passed as the argument of the function.
