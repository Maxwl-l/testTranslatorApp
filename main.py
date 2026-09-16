#Modules
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QComboBox, QPushButton, QLabel, QHBoxLayout, QVBoxLayout
from googletrans import Translator
from languages import *

#Class
class Home(QWidget):
    #Constructor
    def __init__(self):
        super().__init__()
        self.initUI()
        self.settings()


    # Objects and UI Layout
    def initUI(self):
        self.input_box = QTextEdit()
        self.output_box = QTextEdit()
        self.reverse = QPushButton("Reverse")
        self.reset = QPushButton("Reset")
        self.submit = QPushButton("Translate Now")
        self.input_option = QComboBox()
        self.output_option = QComboBox()

        self.input_option.addItems(values)
        self.output_option.addItems(values)


        self.title = QLabel("PyLate")

        self.master = QHBoxLayout()

        col1 = QVBoxLayout()
        col2 = QVBoxLayout()

        # Declares objects(widgets) to the layout
        col1.addWidget(self.title)
        col1.addWidget(self.input_option)
        col1.addWidget(self.output_option)
        col1.addWidget(self.submit)
        col1.addWidget(self.reset)

        col2.addWidget(self.input_box)
        col2.addWidget(self.reverse)
        col2.addWidget(self.output_box)

        # Actually adds the columns/objects to the main layout
        self.master.addLayout(col1,20)
        self.master.addLayout(col2,80)

        self.setLayout(self.master)


    def settings(self):
        self.setWindowTitle("PyLate")

        #takes x,y,width,height of the window and sets it to the window
        self.setGeometry(250,250,800,400)


    def button_click(self):
        pass


    def translate_click(self):
        value_to_key1 = self.output_option.currentText()
        value_to_key2 = self.input_option.currentText()

        # Gets the key from the value in the dictionary
        key_to_value1 = [key for key, value in LANGUAGES.items() if value == value_to_key1][0]


    def reset_app(self):
        pass


    # Uses googletrans library to translate the text from the input box to the output box
    # Takes in the text, destination language, and source language as parameters
    def translate_text(self, text, dest, src):
        # Translator is the class from the googletrans module that allows us to translate text
        # Speaker is just the object
        speaker = Translator()
        translation = speaker.translate(text, dest=dest, src=src)
        return translation.text


    def reverse(self):
        pass



#Main Run "I think this is standard procedure"
if __name__ == "__main__":
    app = QApplication([])
    main = Home()
    main.show()
    app.exec_()