from PyQt5 import QtWidgets
import clientui

class ExamlpeApp(QtWidgets.QMainWindow, clientui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


app = QtWidgets.QApplication([])
window = ExamlpeApp()
window.show()
app.exec_()
