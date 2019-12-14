from mysql.connector import connect

conn = connect(
    host="localhost",
    user="petclinic",
    passwd="petclinic",
    database="petclinic"
)

def print_owner_names():
    cursor = conn.cursor()
    cursor.execute("SELECT first_name,last_name FROM owners")
    for (first_name, last_name) in cursor:
        print(f"{first_name} {last_name}")
    cursor.close()

def list_owner_names():
    names = []
    cursor = conn.cursor()
    cursor.execute("SELECT first_name,last_name FROM owners")
    for (first_name, last_name) in cursor:
        names.append(f"{first_name} {last_name}")
    cursor.close()
    return names


# print_owner_names()
print(list_owner_names())