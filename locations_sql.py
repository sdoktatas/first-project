from mysql.connector import connect #beimmportaljuk a connectet

conn = connect(
    host="localhost",
    user="locations",
    passwd="locations",
    database="locations"
    #port = "999" ha nem alapertelmezett
)

def print_locations():
    cursor = conn.cursor()
    # cursor.execute("update locations set name = concat(name, 'XXX'), lat = lat + 3")
    cursor.execute("update locations set name = concat(name, 'XXX'), lat = lat + 3 where name like 'Budapest%'")
    conn.commit()

def delete_locations():
    cursor = conn.cursor()
    cursor.execute("delete from location_tags")
    cursor.execute("delete from locations")
    conn.commit()
    cursor.close()


def count_locations():
    cursor = conn.cursor()
    count_found = 0
    cursor.execute("select count(*) from locations")
    for (count,) in cursor:
        count_found = count
    cursor.close()
    return count_found


def insert_location(name, coords):
    coordinates = coords.split(",")
    lat = coordinates[0]
    lon = coordinates[1]
    cursor = conn.cursor()
    cursor.execute("insert into locations (name,lat,lon) values(%s,%s,%s)", (name, lat, lon))
    conn.commit()
    cursor.close()


def find_location_by_name(name):
    location_found = None
    #location_found = []

    cursor = conn.cursor()
    cursor.execute("select name, lat, lon from locations where name = %s", (name,))
    for (name, lat, lon) in cursor:
        location_found = (name, lat, lon)
        #location_found.append(name, lat, lon)
    cursor.close()
    return location_found


def find_location_by_name_dictionary(name):
    location_found = None


    cursor = conn.cursor()
    cursor.execute("select name, lat, lon from locations where name = %s", (name,))
    for (name, lat, lon) in cursor:
        location_found = {"name": name, "lat": lat, "lon": lon}

    cursor.close()
    return location_found


def assert_location_exists(name, coords):
    location_found = find_location_by_name(name)
    print(location_found)
    assert location_found is not None
    parts = coords.split(",")
    lat = float(parts[0])
    lon = float(parts[1])

    assert lat == location_found[1]
    assert lon == location_found[2]




#letter = input("Add meg az első betűt!")
#cursor.execute("select name
# , lat, lon from locations where name like %s", (letter + "%",)) #parameterezos verziot, kell a vesszo hogy egy elemu tupple

#letrehozunk egy adatazis kapcsolatot, megadjuk a szukseges infoka

#cursor = conn.cursor() #letrehozzuk a kurzort, es azon keresztul lefuttatjk a selectet
#letter = input("Add meg az első betűt!")
#cursor.execute("select name, lat, lon from locations where name like %s", (letter + "%",)) #parameterezos verziot, kell a vesszo hogy egy elemu tupple
#for (name, lat, lon) in cursor: #itt kell a zarojel, ha nem hasznalsz akkor a teljes sort visszadja
#    print(f"{name} ({lat}, {lon})") #string interpolation a {} kozotti eretekt kicsereli a valtozo ertekere, tipuskonverzot is automatikusan elvegzi
#cursor.close()

#delete_locations()
#print(count_locations())
#insert_location("fdsfdsa", "12.5,10.6")
#print(find_location_by_name("nincsilyen"))
#print(find_location_by_name("fdsfdsa"))
#print(find_location_by_name("legujabb"))
print(assert_location_exists('legujabb', '10.0,10.0'))

