import sqlite3

conn = sqlite3.connect("database.db")

query_creationTable = "CREATE TABLE ALUMNOS(id INTEGER PRIMARY KEY,name TEXT NOT NULL,surname TEXT NOT NULL);"
cursor_Table = conn.cursor()
rows = cursor_Table.execute(query_creationTable)

cont = 0
while cont < 8:
    id = input("Introduzca id del alumno >> ")
    name = input("Introduzca nombre del alumno >> ")
    surname = input("Introduzca apellido del alumno >> ")
    query_Alum = f'INSERT INTO ALUMNOS(id, name, surname) VALUES ({id},"{name}","{surname}")'
    cursor_Alum = conn.cursor()
    row = cursor_Alum.execute(query_Alum)
    conn.commit()
    cont += 1

name = input("Introduce nombre del alumno >> ")
cursor_Find = conn.cursor()
query_Find = f'SELECT * FROM ALUMNOS WHERE name="{name}"'
rows = cursor_Find.execute(query_Find)
data = rows.fetchone()

if data == None:
    print("No hay un alumno con ese nombre")
else:
    query_Alum2 = f'SELECT * FROM ALUMNOS WHERE name="{name}"'
    cursor_Alum2 = conn.cursor()
    rows = cursor_Alum2.execute(query_Alum2)
    for row in rows:
        print(row)

cursor_Table.close()
cursor_Alum.close()
cursor_Find.close()
cursor_Alum2.close()
conn.close()