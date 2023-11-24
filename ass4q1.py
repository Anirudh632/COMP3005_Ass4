import psycopg2
from psycopg2 import sql
from datetime import date

# Database connection parameters
db_params = {
    'dbname': 'Assignment4', # Replace with your Database Name
    'user': 'postgres', #Replace with your Postgres Username
    'password': '#PostgreSQL1008*', #Replace with your Postgres Passsword
    'host': 'localhost',
    'port': '5432'
}

# Function to connect to the database
def connect():
    return psycopg2.connect(**db_params)

# Function to create a new student
def addStudent(first_name, last_name, email, enrollment_date):
    try:
        conn = connect()
        with conn.cursor() as cursor:
            insert_query = sql.SQL("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)")
            cursor.execute(insert_query, (first_name, last_name, email, enrollment_date))
        conn.commit()
        print("Student added successfully.")
    except psycopg2.IntegrityError as e:
        conn.rollback()
        print(f"Error: {e}")
    finally:
        conn.close()

# Function to retrieve all students
def getAllStudents():
    conn = connect()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    conn.close()

# Function to update a student's email
def updateStudentEmail(student_id, new_email):
    try:
        conn = connect()
        with conn.cursor() as cursor:
            update_query = sql.SQL("UPDATE students SET email = %s WHERE student_id = %s")
            cursor.execute(update_query, (new_email, student_id))
        conn.commit()
        print("Email updated successfully.")
    except psycopg2.Error as e:
        conn.rollback()
        print(f"Error: {e}")
    finally:
        conn.close()

# Function to delete a student
def deleteStudent(student_id):
    try:
        conn = connect()
        with conn.cursor() as cursor:
            delete_query = sql.SQL("DELETE FROM students WHERE student_id = %s")
            cursor.execute(delete_query, (student_id,))
        conn.commit()
        print("Student deleted successfully.")
    except psycopg2.Error as e:
        conn.rollback()
        print(f"Error: {e}")
    finally:
        conn.close()

# Example usage
if __name__ == "__main__":
#    addStudent('Anirudh', 'Lagar', 'anirudh.lagar@example.com', date.today())
#    updateStudentEmail(1, 'john.doe123@example.com')
#    deleteStudent(2)
    getAllStudents()
