from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
import mysql.connector
import resource_rc
import funções
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = uic.loadUi('sistema_crud.ui', self)
        self.conectar_banco_dados()
        self.pegar_informacao()

    def conectar_banco_dados(self):
        try:
            self.conexao = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='123456'
                )
            
            cursor = self.conexao.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS basedadosM")  # Cria o banco de dados se não existir
            cursor.execute("USE basedadosM")  # Seleciona o banco de dados criado ou já existente

            # Cria a tabela clientes se não existir
            cursor.execute("""CREATE TABLE IF NOT EXISTS clientes (
                                ID_Cliente INT AUTO_INCREMENT PRIMARY KEY,
                                Nome VARCHAR(255),
                                CPF VARCHAR(14),
                                Senha_GOV VARCHAR(255),
                                Telefone VARCHAR(14),
                                Email VARCHAR(255),
                                Servico VARCHAR(255),
                                Sexo ENUM('M', 'F')
                            )""")
            
            cursor.close()
            
            self.ui.label_3.setText("CONECTADO!")
            self.ui.label_3.setStyleSheet('color: green; font: 900 8pt "Arial Black"; border: 2px solid; border-color: rgb(116, 34, 130); border-radius:10px;')
            self.ui.label_3.setAlignment(Qt.AlignCenter)
        except mysql.connector.Error as err:
            self.ui.label_3.setText("DESCONECTADO!")
            self.ui.label_3.setStyleSheet('color: red; font: 900 8pt "Arial Black"; border: 2px solid; border-color: rgb(116, 34, 130); border-radius:10px')
            self.ui.label_3.setAlignment(Qt.AlignCenter)

# CONFERE CAMPOS E REGISTRA NO BANCO DE DADOS
            
    def pegar_informacao(self):
        
        self.ui.lineEdit_2.text()
        print(self)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow() 
    window.show()  
    sys.exit(app.exec_())
