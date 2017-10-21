from tkinter import *

from  tkinter import messagebox

equipos = ["Costa Rica", "Panama", "Brazil", "Alemania", "España", "Mexico", "Ghana", "China", "Holanda", "Italia","Argentina", "Chile", "Inglaterra", "Peru", "Grecia", "Portugal"]
identificadores = ["CRC", "PNA", "BRZ", "GER", "ESP", "MEX", "GHA", "CHN", "HLD", "ITA", "ARG", "CHI", "ING", "PRU","GRC", "PRL"]
grupo = ["A", "B", "C", "D"]
grupo[0] = [equipos[0], equipos[2], equipos[4], equipos[6]]
grupo[1] = [equipos[1], equipos[3], equipos[5], equipos[7]]
grupo[2] = [equipos[8], equipos[10], equipos[12], equipos[14]]
grupo[3] = [equipos[9], equipos[11], equipos[13], equipos[15]]


ventana=Tk()
ventana.geometry("710x444")
ventana.title("Escribe La tabla que deses ver")
fondo= PhotoImage(file="ru.png")
fondolabel= Label(ventana, image=fondo).place(x=0, y=0)



def a():
    q=messagebox.showinfo("TABLA",("Grupo : ",entrada.get()))
def b():

   x= messagebox.askquestion(("Deseas ver la tabla del grupo: ",entrada.get()), "Elige si para continuar no para salir")
   if x=="yes":
       l = input("Digita el grupo a ver entre A y D").upper()
       messagebox.showinfo(("Tabla", entrada.get()))
       equipos = ["Costa Rica", "Panama", "Brazil", "Alemania", "España", "Mexico", "Ghana", "China", "Holanda", "Italia", "Argentina", "Chile", "Inglaterra", "Peru", "Grecia", "Portugal"]
       identificadores = ["CRC", "PNA", "BRZ", "GER", "ESP", "MEX", "GHA", "CHN", "HLD", "ITA", "ARG", "CHI", "ING","PRU", "GRC", "PRL"]
       grupo = ["A", "B", "C", "D"]
       grupo[0] = [identificadores[0], identificadores[2], identificadores[4], identificadores[6]]
       grupo[1] = [identificadores[1], identificadores[3], identificadores[5], identificadores[7]]
       grupo[2] = [identificadores[8], identificadores[10], identificadores[12], identificadores[14]]
       grupo[3] = [identificadores[9], identificadores[11], identificadores[13], identificadores[15]]


       if l == "A":
           l = 0
       elif l == "B":
           l = 1
       elif l == "C":
           l = 2
       elif l == "D":
           l = 3
       else:
           print("ERROR")
       lbltabla= Label(text=("1)"+grupo[l][0]+"\n"+"2)"+grupo[l][1]+"\n"+"3)"+grupo[l][2]+"\n"+"4)"+grupo[l][3]),font=("Agency FB", 11)).place(x=-2,y=160)
       ilesta= Label(text=("Equipo   PJ   PG   PP   PE   GF   GC   GD   PTS\n"),font=("Agency FB", 18)).place(x=-2,y=100)




equipos = ["Costa Rica", "Panama", "Brazil", "Alemania", "España", "Mexico", "Ghana", "China", "Holanda", "Italia", "Argentina", "Chile", "Inglaterra", "Peru", "Grecia", "Portugal"]
identificadores = ["CRC", "PNA", "BRZ", "GER", "ESP", "MEX", "GHA", "CHN", "HLD", "ITA", "ARG", "CHI", "ING", "PRU","GRC", "PRL"]
grupo = ["A", "B", "C", "D"]
grupo[0] = [equipos[0], equipos[2], equipos[4], equipos[6]]
grupo[1] = [equipos[1], equipos[3], equipos[5], equipos[7]]
grupo[2] = [equipos[8], equipos[10], equipos[12], equipos[14]]
grupo[3] = [equipos[9], equipos[11], equipos[13], equipos[15]]



entrada=Entry()
entrada.pack()

boton= Button(text="Login", command=a).place(x=500,y=200)
boton2= Button(text="Ver tablas", command=b).place(x=500,y=100)




ventana.mainloop()