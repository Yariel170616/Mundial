
Users= open("us.txt","a")
Uuario=input()

Users.writelines(Usuario)
Users.writelines("\n")
T=input()
t=input()
e=0
while True:
    if T ==Users.readline():
        print("Acceso exitoso")
    elif T != Users.readline():
        Users.readline()
    else:
        print("usuario no existe")

