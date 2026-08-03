import sqlite3

conn = sqlite3.connect(r"C:\Users\Pranav Wadatkar\Desktop\Python\python-for-ai\practice week4\example.db")

cursor = conn.cursor()

# cursor.execute('''
#     INSERT INTO users (id,name,age)
#     VALUES (1,'Pranav',19)
# ''')

def add_row(id,name,age):
    cursor.execute('''
        INSERT INTO users (id,name,age)
        VALUES (?,?,?)''', (id, name, age))

user_id = int(input("Enter id: "))
user_name = input("Enter name: ")
user_age = int(input("Enter age: "))

add_row(user_id,user_name,user_age)

a = cursor.execute('''
        SELECT * FROM USERS    
    ''')
for i in a:
    print(i)

conn.commit()
conn.close()