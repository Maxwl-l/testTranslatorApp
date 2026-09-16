#Modules
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QComboBox, QPushButton, QLabel, QHBoxLayout, QVBoxLayout
from googletrans import Translator
from languages import *

#Class
class Home(QWidget):
    #Constructor
    def __init__(self):
        super().__init__()


    # Objects and UI Layout
    def initUI(self):
        self.input_box = QTextEdit()
        self.output_box = QTextEdit()
        self.reverse = QPushButton("Reverse")
        self.reset = QPushButton("Reset")
        self.submit = QPushButton("Translate Now")
        self.input_option = QComboBox()
        self.output_option = QComboBox()
        self.title = QLabel("PyLate")


    def settings(self):
        pass


    def button_click(self):
        pass


    def translate_click(self):
        pass


    def reset_app(self):
        pass


    def translate_text(self):
        pass


    def reverse(self):
        pass



#Main Run "I think this is standard procedure"
if __name__ == "__main__":
    app = QApplication([])
    main = Home()
    main.show()
    app.exec_()