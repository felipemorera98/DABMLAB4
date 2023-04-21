from registro import RegistrarUsuario
from Luminocidad import WindowsPaciente
import sys
from PyQt6.QtWidgets import (QApplication,QLabel,QWidget,QLineEdit,QPushButton,QMessageBox,QCheckBox)
from PyQt6.QtGui import QPixmap, QFont                  



class WindowsLogin(QWidget):
        def __init__(self):
                super().__init__()
                self.Inicio()    
        def Inicio(self):
                self.setGeometry(200,200,400,350)
                self.setWindowTitle("Intensidad Luminica")
                self.Items()
                self.show()

        def Items(self):
                self.is_loger=False

                Text_Info=QLabel(self)
                Text_Info.setText("Ingrese las Credenciales Solicitadas")
                Text_Info.setFont(QFont("Arial",10))
                Text_Info.move(20,54)

                user_login=QLabel(self)
                user_login.setText("Usuario: ")
                user_login.setFont(QFont("Arial",10))
                user_login.move(20,104)

                self.user_input=QLineEdit(self)
                self.user_input.resize(250,24)
                self.user_input.move(90,100)

                password_login=QLabel(self)
                password_login.setText("Contraseña: ")
                password_login.setFont(QFont("Arial",10))
                password_login.move(20,154)

                self.password_input=QLineEdit(self)
                self.password_input.resize(250,24)
                self.password_input.move(90,150)
                self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

                self.ver_contraseña=QCheckBox(self)
                self.ver_contraseña.setText("Ver Contraseña")
                self.ver_contraseña.move(90,190)
                self.ver_contraseña.toggled.connect(self.mostrar_password)

                ingresar_boton=QPushButton(self)
                ingresar_boton.setText("Ingresar")
                ingresar_boton.setFont(QFont("Arial",10))
                ingresar_boton.resize(250,30)
                ingresar_boton.move(70,230)
                ingresar_boton.clicked.connect(self.iniciar_mainview)

                registrarse_boton=QPushButton(self)
                registrarse_boton.setText("Registrarse")
                registrarse_boton.setFont(QFont("Arial",10))
                registrarse_boton.resize(250,30)
                registrarse_boton.move(70,270)
                registrarse_boton.clicked.connect(self.registrar_usuario)


        def mostrar_password(self,clicked):
                if clicked:
                        self.password_input.setEchoMode(QLineEdit.EchoMode.Normal)
                else:
                        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
                
        def registrar_usuario(self):
                self.nuevo_usuario=RegistrarUsuario()
                self.nuevo_usuario.show()

        def iniciar_mainview(self):
                users=[]
                user_path="usuarios.txt"
                try:
                        with open(user_path,"r") as file:
                                for linea in file:
                                        users.append(linea.strip("\n"))
                        login_information = f"{self.user_input.text()},{self.password_input.text()}"

                        if login_information in users:
                                QMessageBox.information(self,"inicio Sesion",
                                                        "inicio de Sesion Exitoso",
                                                        QMessageBox.StandardButton.Ok,
                                                        QMessageBox.StandardButton.Ok)
                                self.is_logged=True
                                self.close()
                                self.luminocidad=WindowsPaciente()
                                self.luminocidad.show()
                        else:
                                QMessageBox.warning(self,"Error", 
                                                    "Credenciales incorrectas",
                                                    QMessageBox.StandardButton.Close,
                                                    QMessageBox.StandardButton.Close)

                except FileNotFoundError as e:
                        QMessageBox.warning(self,"Error Message", 
                                                    "Base de datos no encontrada {e}",
                                                    QMessageBox.StandardButton.Close,
                                                    QMessageBox.StandardButton.Close)


if __name__=="__main__":
        app = QApplication(sys.argv)
        ventana = WindowsLogin()
        sys.exit(app.exec())