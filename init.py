from _global import *
import random

def generate_phone_number():
    return f"0{random.randint(100, 999)}-{random.randint(1000, 9999)}"

names = ["John Doe", "Jane Smith", "Michael Brown", "Alice Miller", "David Johnson",
         "Sarah Jones", "Robert Williams", "Emily Garcia", "Matthew Davis", "Jennifer Lopez"]
unit_names = ["Alpha Team", "Bravo Company", "Charlie Platoon", "Delta Squad", "Echo Force",
              "Foxtrot Battalion", "Golf Regiment", "Hotel Brigade", "India Division", "Juliet Corps"]

def init():
    db = mysql.connector.connect(
      host=mysql_host,
      user=mysql_user,
      password=mysql_pwd)
    print(f"Connected to database: {mysql_user}")
    cursor = db.cursor()
    create_database = f"""CREATE DATABASE IF NOT EXISTS {mysql_db};"""
    delete_table_query = f"""DROP TABLE IF EXISTS {emp_table};"""
    create_table_query = f"""CREATE TABLE IF NOT EXISTS {emp_table}(id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255) NOT NULL, unit_name VARCHAR(255),phone_no VARCHAR(20));"""
    insert_query = f"INSERT INTO {emp_table} (name, unit_name, phone_no) VALUES (%s, %s, %s);"
    cursor.execute(create_database)
    cursor.execute(f"""USE {mysql_db}""")
    cursor.execute(delete_table_query)
    cursor.execute(create_table_query)
    

    names = ["John Doe", "Jane Smith", "Michael Brown", "Alice Miller", "David Johnson",
         "Sarah Jones", "Robert Williams", "Emily Garcia", "Matthew Davis", "Jennifer Lopez"]
    unit_names = ["Alpha Team", "Bravo Company", "Charlie Platoon", "Delta Squad", "Echo Force",
                "Foxtrot Battalion", "Golf Regiment", "Hotel Brigade", "India Division", "Juliet Corps"]
    

    for i in range(10):
        random_unit_name = random.choice(unit_names)
        random_phone_number = generate_phone_number()
        cursor.execute(insert_query, (names[i], random_unit_name, random_phone_number))
    cursor.execute("COMMIT;")
    cursor.close()
    print("init complete.....")



