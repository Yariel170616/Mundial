<<<<<<< HEAD
#!/usr/bin/env python
# -*- coding: utf-8 -*-
Users= open("us.txt","a")
Usuario=input("Digite su usuario a guardar")
Password=open("Contraseñas.txt","a")
Contra=input("Digite su contraseña:")
Password.writelines(Contra)
Password.writelines("\n")
=======

Users= open("us.txt","a")
Uuario=input()

>>>>>>> master
Users.writelines(Usuario)
Users.writelines("\n")
T=input()
t=input()
e=0
<<<<<<< HEAD
while e>= len(Users.readlines()):

Users.close()
Password.close()
=======
while True:
    if T ==Users.readline():
        print("Acceso exitoso")
    elif T != Users.readline():
        Users.readline()
    else:
        print("usuario no existe")
>>>>>>> master

