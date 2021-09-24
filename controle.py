from PyQt5 import uic, QtWidgets
import mysql.connector
import hashlib

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="aps"
)


def enviar():
    usuario = formulario.lineEdit.text()
    senha = formulario.lineEdit_2.text()
    senha = hashlib.md5(senha.encode()).hexdigest()

    cursor = banco.cursor()
    comando_SQL = "SELECT nome FROM tripulantes WHERE usuario = '" + usuario + "' AND senha ='" + senha + "'"
    cursor.execute(comando_SQL)
    dados = cursor.fetchall()

    if dados == []:
        formulario.label_4.setText("Usuário ou senha inválidos")

    else:
        formulario.label_4.setText("")
        navio.label_2.setText(f"Bem Vindo, {dados[0][0]}")
        navio.show()
        formulario.close()
    formulario.lineEdit.setText("")
    formulario.lineEdit_2.setText("")


def sair():
    formulario.show()
    navio.close()
    global usuario
    usuario = ""
    global senha
    senha = ""


app = QtWidgets.QApplication([])
formulario = uic.loadUi("tripulação.ui")
navio = uic.loadUi("navio.ui")
formulario.pushButton.clicked.connect(enviar)
navio.pushButton_2.clicked.connect(sair)
formulario.show()
app.exec()
