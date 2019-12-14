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


def count_owners_who_lives_in(city):
    cursor = conn.cursor()
    count_found = 0
    cursor.execute("select count(*) from owners where city = %s", (city,))
    for (count,) in cursor:
        count_found = count
    cursor.close()
    return count_found


def create_owner_with(name, address, city, telephone):
    parts = name.split(" ")
    first_name = parts[0]
    last_name = parts[1]
    cursor = conn.cursor()
    cursor.execute("insert into owners (first_name,last_name, address,city, telephone) values(%s,%s,%s,%s,%s)",
                   (first_name, last_name, address, city, telephone))
    conn.commit()
    cursor.close()


def create_owner(owner):
    name = owner["name"]
    parts = name.split(" ")
    first_name = parts[0]
    last_name = parts[1]
    address = owner["address"]
    city = owner["city"]
    telephone = owner["telephone"]
    cursor = conn.cursor()
    cursor.execute("insert into owners (first_name,last_name, address,city, telephone) values(%s,%s,%s,%s,%s)",
                   (first_name, last_name, address, city, telephone))
    conn.commit()
    cursor.close()


# print_owner_names()
# print(list_owner_names())
# print(list_owner_names_who_lives_in('Madison'))
# print(find_owner_by_id("1"))
# print(count_owners_who_lives_in("Madison"))
# create_owner_with("Lajcsi Lagzi", "Trombita utca 24.", "Csalyágaröcsöge", "555")
# print_owner_names()
owner = {"name": "Boborján Kis", "address": "Vastyúk u. 1..", "city": "Budapest", "telephone": "123456"}
create_owner(owner)
print_owner_names()

