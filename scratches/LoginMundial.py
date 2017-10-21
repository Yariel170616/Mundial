#!/usr/bin/env python
# -*- coding: utf-8 -*-
Users= open("us.txt","a")
Usuario=input("Digite su usuario a guardar")
Password=open("Contraseñas.txt","a")
Contra=input("Digite su contraseña:")
Password.writelines(Contra)
Password.writelines("\n")
Users.writelines(Usuario)
Users.writelines("\n")
T=input()
t=input()
e=0
while e>= len(Users.readlines()):

Users.close()
Password.close()

