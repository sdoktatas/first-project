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


def list_owner_names_who_lives_in(city):
    names = []
    cursor = conn.cursor()
    cursor.execute("SELECT first_name,last_name FROM owners WHERE city = %s", (city, ))
    for (first_name, last_name) in cursor:
        names.append(f"{first_name} {last_name}")
    cursor.close()
    return names


def find_owner_by_id(id):

    cursor = conn.cursor()
    cursor.execute("SELECT first_name,last_name, address, city, telephone FROM owners WHERE id = %s", (id,))
    for (first_name,last_name, address, city, telephone) in cursor:
        owner = {"name": first_name + " " + last_name, "address": address, "city": city, "telephone": telephone}
    return owner


# print_owner_names()
# print(list_owner_names())
# print(list_owner_names_who_lives_in('Madison'))
print(find_owner_by_id("1"))