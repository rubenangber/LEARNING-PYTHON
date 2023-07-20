import sqlite3
import getpass

def main():
    username = input("Introduce nombre de usuario >> ")
    password = getpass.getpass("Introduce contraseña >> ")
    if verifica_credenciales(username, password):
        print("Login correcto")
    else:
        print("Login incorrecto")
    id = input("Introduce ID de usuario >> ")
    username = input("Introduce nombre de usuario >> ")
    password = input("Introduce contraseña >> ")
    create_user(id, username, password)

def verifica_credenciales(username, password):
    conn = sqlite3.connect("miaplicacion.db")
    cursor = conn.cursor()

    rows = cursor.execute(f'SELECT id from users WHERE username ="{username}" AND password ="{password}"')
    data = rows.fetchone() #Devuelve 1 elemento
    cursor.close()
    conn.close()
    if data == None:
        return False
    else:
        return True

def create_user(id, username, password):
    conn = sqlite3.connect("miaplicacion.db")
    cursor = conn.cursor()

    rows = cursor.execute(f'INSERT INTO users(id, username, password) VALUES ({id},"{username}","{password}")')
    conn.commit() #Enviar trasnaccion

    cursor.close()
    conn.close()

if __name__ == '__main__':
    main()

#conn = sqlite3.connect('miaplicacion.db')
#cursor = conn.cursor()
#
#rows = cursor.execute("SELECT * FROM users")
#for row in rows:
#    print(row)
#
#cursor.close()
#conn.close()