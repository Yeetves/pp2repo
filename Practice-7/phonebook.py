from connect import get_connection
import csv


#Insert from console
print("Insertion from console")
conn = get_connection()
cur = conn.cursor()

name = input("Enter name: ")
phone = input("Enter phone: ")
cur.execute(
    "INSERT INTO contacts (name, phone) VALUES (%s, %s)",
    (name, phone)
)

conn.commit()
cur.close()
conn.close()

print("Contact added")


#Insert from CSV
print("Insertion form CSV")
conn = get_connection()
cur = conn.cursor()

with open("contacts.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        cur.execute(
        "INSERT INTO contacts (name, phone) VALUES (%s, %s)",
        (row["name"], row["phone"])
    )

conn.commit()
cur.close()
conn.close()

print("Inserted from CSV")


#Update contact
print("Update contact")
conn = get_connection()
cur = conn.cursor()

old_name = input("Enter name to update: ")
new_name = input("New name: ")
new_phone = input("New phone: ")

cur.execute(
    "UPDATE contacts SET name=%s, phone=%s WHERE name=%s",
    (new_name, new_phone, old_name)
)

conn.commit()
cur.close()
conn.close()

print("Contact updated")


#Search by name
print("Search by name")
conn = get_connection()
cur = conn.cursor()

name = input("Search name: ")

cur.execute(
    "SELECT * FROM contacts WHERE name ILIKE %s",
    ("%" + name + "%",)
)

rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()


#Search by phone
print("Search by phone")
conn = get_connection()
cur = conn.cursor()

prefix = input("Phone starts with: ")

cur.execute(
    "SELECT * FROM contacts WHERE phone LIKE %s",
    (prefix + "%",)
)

rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()


#Delete contact
print("Delete contact")
conn = get_connection()
cur = conn.cursor()

value = input("Enter name or phone to delete: ")

cur.execute(
    "DELETE FROM contacts WHERE name=%s OR phone=%s",
    (value, value)
)

conn.commit()
cur.close()
conn.close()

print("Contact deleted")


print("Output all contacts table")
conn = get_connection()
cur = conn.cursor()

cur.execute("SELECT * FROM contacts")

rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()
