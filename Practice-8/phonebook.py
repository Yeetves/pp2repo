from connect import get_connection

#Search by pattern, function
conn = get_connection()
cur = conn.cursor()

pattern = input("Enter search pattern: ")

cur.execute("SELECT * FROM get_contacts_by_pattern(%s)", (pattern,))

cur.close()
conn.close()


#Upsert procedure
conn = get_connection()
cur = conn.cursor()

name = input("Enter name: ")
phone = input("Enter phone: ")

cur.execute("CALL upsert_contact(%s, %s)", (name, phone))
conn.commit()

print("Upserted")

cur.close()
conn.close()


#Insert many users procedure
conn = get_connection()
cur = conn.cursor()

n = int(input("How many users? "))

names = []
phones = []

for i in range(n):
    name = input("Name: ")
    names.append(name)
    phone = input("Phone: ")
    phones.append(phone)

cur.execute(
    "CALL insert_many_users(%s, %s)",
    (names, phones)
)

conn.commit()

print("Batch insert completed (check notices for invalid phones)")

cur.close()
conn.close()


#Pagination function (LIMIT OFFSET)
conn = get_connection()
cur = conn.cursor()

limit = int(input("Enter limit: "))
offset = int(input("Enter offset: "))

cur.execute(
    "SELECT * FROM get_contacts_paginated(%s, %s)",
    (limit, offset)
)

rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()


#Delete procedure
conn = get_connection()
cur = conn.cursor()

value = input("Enter name or phone to delete: ")

cur.execute("CALL delete_contact(%s)", (value,))
conn.commit()

print("Deleted")

cur.close()
conn.close()

