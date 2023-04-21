from PyQt6.QtWidgets import QDialog, QLabel, QPushButton, QLineEdit, QMessageBox
from PyQt6.QtGui import QFont

class RegistrarUsuario(QDialog):
    def __init__(self):
        super().__init__()
        self.formulario()

    def formulario(self):
        self.setGeometry(100,100,350,250)
        self.setWindowTitle("Registro de Usuario")
        
        user_login=QLabel(self)
        user_login.setText("Usuario: ")
        user_login.setFont(QFont("Arial",10))
        user_login.move(20,44)

        self.user_input=QLineEdit(self)
        self.user_input.resize(200,24)
        self.user_input.move(90,44)

        password1_login=QLabel(self)
        password1_login.setText("Contraseña: ")
        password1_login.setFont(QFont("Arial",10))
        password1_login.move(20,84)

        self.password1_input=QLineEdit(self)
        self.password1_input.resize(200,24)
        self.password1_input.move(90,84)
        self.password1_input.setEchoMode(QLineEdit.EchoMode.Password)

        password2_login=QLabel(self)
        password2_login.setText("Contraseña: ")
        password2_login.setFont(QFont("Arial",10))
        password2_login.move(20,124)

        self.password2_input=QLineEdit(self)
        self.password2_input.resize(200,24)
        self.password2_input.move(90,124)
        self.password2_input.setEchoMode(QLineEdit.EchoMode.Password)

        guardar_boton=QPushButton(self)
        guardar_boton.setText("Guardar")
        guardar_boton.resize(100,32)
        guardar_boton.move(30,170)
        guardar_boton.clicked.connect(self.crear_usuario)

        cancelar_boton=QPushButton(self)
        cancelar_boton.setText("Cancelar")
        cancelar_boton.resize(100,32)
        cancelar_boton.move(180,170)
        cancelar_boton.clicked.connect(self.cancelar_creacion)

    def cancelar_creacion(self):
        self.close()
    def crear_usuario(self):
        user_path="usuarios.txt"
        usuario=self.user_input.text()
        password1=self.password1_input.text()
        password2=self.password2_input.text()

        if password1 == "" or password2== "" or usuario == "":
            QMessageBox.warning(self,"Error","Por favor verifique que los datos sean validos",
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)
        elif password1 != password2:
            QMessageBox.warning(self,"Error","Por favor verifique las contraseñas",
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)
        else:
            try:
                with open(user_path,'a+') as f:
                    f.write(f"{usuario},{password1}\n")
                    QMessageBox.information(self,"Creacion Exitosa",
                                            "Usuario Creado Correctamente",
                                            QMessageBox.StandardButton.Ok,
                                            QMessageBox.StandardButton.Ok)
            except FileNotFoundError as e:
                QMessageBox.warning(self,"Error","La base de datos de usuario no existe",
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)
            self.close()