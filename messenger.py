import datetime
import requests
from PyQt5 import QtWidgets, QtCore
import clientui

class ExamlpeApp(QtWidgets.QMainWindow, clientui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.pressed.connect(self.button_pushed)

        self.after = 0
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_messages)
        self.timer.start(1000)

    def button_pushed(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        text = self.textEdit.toPlainText()

        self.send_message(username, password, text)

        self.textEdit.setText('')
        self.textEdit.repaint()    



    def send_message(self, username, password, text):
            message = {'username': username, 'password': password, 'text': text}
            try:
                response = requests.post('http://127.0.0.1:5000/send', json=message)
                if response.status_code == 401:
                    self.show_text('Bad password')
                elif response.status_code != 200:
                    self.show_text('Connection Error!')
            except:
                self.show_text('Connection Error!')

app = QtWidgets.QApplication([])
window = ExamlpeApp()
window.show()
app.exec_()
