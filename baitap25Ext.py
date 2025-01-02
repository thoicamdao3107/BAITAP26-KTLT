from PyQt6.QtWidgets import QMainWindow, QMessageBox
from baitap25 import Ui_MainWindow


class SymmetricChecker(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.check_symmetric)
        self.ui.pushButton_2.clicked.connect(self.clear_fields)
        self.ui.pushButton_3.clicked.connect(self.close_app)

    def check_symmetric(self):

        input_string = self.ui.lineEdit.text()
        if not input_string:
            self.ui.label_3.setText("Please enter a string!")
            return


        if input_string == input_string[::-1]:
            self.ui.label_3.setText("This string is symmetric!")
        else:
            self.ui.label_3.setText("This string is not symmetric!")

    def clear_fields(self):
        self.ui.lineEdit.clear()
        self.ui.label_3.setText("")

    def close_app(self):
        msg = QMessageBox()
        msg.setWindowTitle("Exit")
        msg.setText("Thank you for using the program!")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)

        if msg.exec() == QMessageBox.StandardButton.Ok:
            self.close()
