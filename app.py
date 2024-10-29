import streamlit as st
import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='Piyush@02',
        database='employee_managment_project'
    )

def add_employee(conn, name, department, promotion_status='Not Promoted'):
    cursor = conn.cursor()
    query = "INSERT INTO emp_data (name, department, promotion_status) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, department, promotion_status))
    conn.commit()  # Use conn.commit() instead of cursor.commit()
    cursor.close()
    st.success(f"Employee {name} added successfully!")

def promote_employee(conn, employee_id):
    cursor = conn.cursor()
    query = "UPDATE emp_data SET promotion_status = 'Promoted' WHERE id = %s"
    cursor.execute(query, (employee_id,))
    conn.commit()  # Use conn.commit() instead of cursor.commit()
    cursor.close()
    st.success(f"Employee with ID {employee_id} promoted successfully!")

def remove_employee(conn, employee_id):
    cursor = conn.cursor()
    query = "DELETE FROM emp_data WHERE id = %s"
    cursor.execute(query, (employee_id,))
    conn.commit()  # Use conn.commit() instead of cursor.commit()
    cursor.close()
    st.success(f"Employee with ID {employee_id} removed successfully!")

def display_employee(conn):
    cursor = conn.cursor()
    query = "SELECT * FROM emp_data"
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    return rows

def main():
    conn = connect_db()
    st.title("Employee Management System")

    menu = ["Home", "Add", "Promote", "Display", "Remove"]
    choice = st.sidebar.selectbox("Menu", [option.lower() for option in menu])

    if choice == "home":
        st.subheader("Home")
        st.write("Welcome to the Employee Management System")

    elif choice == "add":
        st.subheader("Add Employee")
        name = st.text_input("Name")
        department = st.text_input("Department")
        if st.button("Add"):
            add_employee(conn, name, department)

    elif choice == "promote":
        st.subheader("Promote Employee")
        employee_id = st.number_input("Employee ID", min_value=1)
        if st.button("Promote"):
            promote_employee(conn, employee_id)

    elif choice == "display":
        st.subheader("Employee List")
        rows = display_employee(conn)
        st.write(rows)

    elif choice == "remove":
        st.subheader("Remove Employee")
        employee_id = st.number_input("Employee ID to remove", min_value=1)
        if st.button("Remove"):
            remove_employee(conn, employee_id)

    conn.close()

if __name__ == "__main__":
    main()