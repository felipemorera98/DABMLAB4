from PyQt6.QtWidgets import (QDialog,QLabel,QLineEdit,QPushButton,QMessageBox)
from PyQt6.QtGui import QFont   

import serial
import csv
import os
import os.path as path
import struct

cwd = os.getcwd()

class WindowsPaciente(QDialog):
        def __init__(self):
                super().__init__()
                self.Inicio()

        def Inicio(self):
                self.setGeometry(200,200,500,500)
                self.setWindowTitle("Intensidad Luminica")
                self.Items()
                self.show()

        def Items(self):
                self.is_loger=False
                LimS=QLabel(self)
                LimS.setText("El Limite de Luminocidad Superior es: ")
                LimS.setFont(QFont("Arial",10))
                LimS.move(20,40)

                self.LimS=QLineEdit(self)
                self.LimS.setFont(QFont("Arial",10))
                self.LimS.move(270,40)
                
                LimI=QLabel(self)
                LimI.setText("El Limite de Luminocidad Inferior es: ")
                LimI.setFont(QFont("Arial",10))
                LimI.move(20,80)

                self.LimI=QLineEdit(self)
                self.LimI.setFont(QFont("Arial",10))
                self.LimI.move(270,80)

                Lum=QLabel(self)
                Lum.setText("La Luminocidad Actual es: ")
                Lum.setFont(QFont("Arial",10))
                Lum.move(20,120)

                self.Lim=QLineEdit(self)
                self.Lim.setFont(QFont("Arial",10))
                self.Lim.move(270,120)

                LimS_user=QLabel(self)
                LimS_user.setText("Ingrese el nuevo valor del Limite Superior :")
                LimS_user.setFont(QFont("Arial",10))
                LimS_user.move(20,160)

                self.LimS_input=QLineEdit(self)
                self.LimS_input.resize(70,25)
                self.LimS_input.move(270,155)
                
                
                LimI_user=QLabel(self)
                LimI_user.setText("Ingrese el nuevo valor del Limite Inferior :")
                LimI_user.setFont(QFont("Arial",10))
                LimI_user.move(20,220)              

                self.LimI_input=QLineEdit(self)
                self.LimI_input.resize(70,25)
                self.LimI_input.move(270,215)

                actualizar_boton=QPushButton(self)
                actualizar_boton.setText("Actualizar")
                actualizar_boton.setFont(QFont("Arial",10))
                actualizar_boton.resize(80,30)
                actualizar_boton.move(20,260)
                actualizar_boton.clicked.connect(self.datos)

                cerrar_boton=QPushButton(self)
                cerrar_boton.setText("Cerrar sesion")
                cerrar_boton.setFont(QFont("Arial",10))
                cerrar_boton.resize(100,30)
                cerrar_boton.move(20,360)
        
        def datos(self):
                self.dato=valor_serial()
                LimS=int(self.LimS_input.text())
                LimI=int(self.LimI_input.text())
                if self.dato<LimS and self.dato>LimI:
                      arduino_F(LimS,LimI,0,255)
                else:
                      QMessageBox.warning(self,"Error Message","No esta dentro de los Limites {e}",
                                          QMessageBox.StandardButton.Close,
                                          QMessageBox.StandardButton.Close)
                

def valor_serial():
    arduino = serial.Serial("COM4", 9600)
    sensor = arduino.readline()
    dato = int(sensor.decode())
    return dato


def c_archivo(vectorD, tipo):
    name = cwd + "/Datos/datos.csv"
    with open(name, tipo, newline="") as file:
        csv_writer = csv.writer(file, delimiter=",")
        csv_writer.writerow(vectorD)

def F_map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


def arduino_F(LimS,LimI,minIN,maxIN):
    while True:
        arduino = serial.Serial("COM4", 9600)
        sensor = arduino.readline()
        dato = int(sensor.decode())
        vector=[]
        dato_m=255-int(F_map(dato, LimI, LimS, minIN, maxIN))
        arduino.write(struct.pack(">B", dato_m))
        vector.append(dato_m)
        name = cwd + "/Datos/datos.csv"
        if path.exists(name):
            tipe_D = "a+"
            c_archivo(vector, tipe_D)
        else:
            tipe_D = "w"
            c_archivo(vector, tipe_D)



