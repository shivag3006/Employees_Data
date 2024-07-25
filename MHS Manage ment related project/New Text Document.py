import sqlite3

def create_connection():
    return sqlite3.connect('employee_database.db')

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            position TEXT NOT NULL,
            salary REAL NOT NULL
        )
    ''')
    conn.commit()

def add_employee(conn, name, position, salary):
    cursor = conn.cursor()
    cursor.execute('INSERT INTO employees (name, position, salary) VALUES (?, ?, ?)', (name, position, salary))
    conn.commit()
    print(f'Employee {name} added successfully.')

def view_employees(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM employees')
    employees = cursor.fetchall()
    for employee in employees:
        print(f'ID: {employee[0]}, Name: {employee[1]}, Position: {employee[2]}, Salary: ${employee[3]:.2f}')

def update_employee(conn, id, name, position, salary):
    cursor = conn.cursor()
    cursor.execute('UPDATE employees SET name=?, position=?, salary=? WHERE id=?', (name, position, salary, id))
    conn.commit()
    print(f'Employee with ID {id} updated successfully.')

def delete_employee(conn, id):
    cursor = conn.cursor()
    cursor.execute('DELETE FROM employees WHERE id=?', (id,))
    conn.commit()
    print(f'Employee with ID {id} deleted successfully.')

def main():
    with create_connection() as conn:
        create_table(conn)
        
        while True:
            print('\nEmployee Management System')
            print('1. Add Employee')
            print('2. View Employees')
            print('3. Update Employee')
            print('4. Delete Employee')
            print('5. Exit')

            choice = input('Enter your choice: ')

            try:
                if choice == '1':
                    name = input('Enter employee name: ')
                    position = input('Enter employee position: ')
                    salary = float(input('Enter employee salary: '))
                    add_employee(conn, name, position, salary)

                elif choice == '2':
                    view_employees(conn)

                elif choice == '3':
                    id = int(input('Enter employee ID to update: '))
                    name = input('Enter updated name: ')
                    position = input('Enter updated position: ')
                    salary = float(input('Enter updated salary: '))
                    update_employee(conn, id, name, position, salary)

                elif choice == '4':
                    id = int(input('Enter employee ID to delete: '))
                    delete_employee(conn, id)

                elif choice == '5':
                    break

                else:
                    print('Invalid choice. Please try again.')

            except ValueError:
                print('Invalid input. Please enter the correct data type.')

if __name__ == '__main__':
    main()
