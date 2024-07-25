import sqlite3

# Create a connection to the database (or create if it doesn't exist)
conn = sqlite3.connect('employee_database.db')
cursor = conn.cursor()

# Create the employee table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        position TEXT NOT NULL,
        salary REAL NOT NULL
    )
''')
conn.commit()

def add_employee(name, position, salary):
    cursor.execute('INSERT INTO employees (name, position, salary) VALUES (?, ?, ?)', (name, position, salary))
    conn.commit()
    print(f'Employee {name} added successfully.')

def view_employees():
    cursor.execute('SELECT * FROM employees')
    employees = cursor.fetchall()
    for employee in employees:
        print(f'ID: {employee[0]}, Name: {employee[1]}, Position: {employee[2]}, Salary: ${employee[3]:.2f}')

def update_employee(id, name, position, salary):
    cursor.execute('UPDATE employees SET name=?, position=?, salary=? WHERE id=?', (name, position, salary, id))
    conn.commit()
    print(f'Employee with ID {id} updated successfully.')

def delete_employee(id):
    cursor.execute('DELETE FROM employees WHERE id=?', (id,))
    conn.commit()
    print(f'Employee with ID {id} deleted successfully.')

if __name__ == '__main__':
    while True:
        print('\nEmployee Management System')
        print('1. Add Employee')
        print('2. View Employees')
        print('3. Update Employee')
        print('4. Delete Employee')
        print('5. Exit')
        
        choice = input('Enter your choice: ')

        if choice == '1':
            name = input('Enter employee name: ')
            position = input('Enter employee position: ')
            salary = float(input('Enter employee salary: '))
            add_employee(name, position, salary)

        elif choice == '2':
            view_employees()

        elif choice == '3':
            id = int(input('Enter employee ID to update: '))
            name = input('Enter updated name: ')
            position = input('Enter updated position: ')
            salary = float(input('Enter updated salary: '))
            update_employee(id, name, position, salary)

        elif choice == '4':
            id = int(input('Enter employee ID to delete: '))
            delete_employee(id)

        elif choice == '5':
            break

    conn.close()
