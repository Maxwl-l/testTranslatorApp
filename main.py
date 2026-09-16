#Modules
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QComboBox, QPushButton, QLabel, QHBoxLayout, QVBoxLayout
from googletrans import Translator
from languages import *
from PyQt5.QtGui import QFont

#Class
class Home(QWidget):
    #Constructor
    def __init__(self):
        super().__init__()
        self.initUI()
        self.settings()
        self.button_click()


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
        self.title.setFont(QFont("Arial", 20, QFont.Bold))

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

        self.setStyleSheet("""
            QWidget { 
                background-color: #42d4f5;
                color: white;
            }

            QPushButton {
                background-color: lightblue;
                color: black;
            }

            QPushButton:hover {
                background-color: lightgreen;
            }
        """)


    def settings(self):
        self.setWindowTitle("PyLate")

        #takes x,y,width,height of the window and sets it to the window
        self.setGeometry(250,250,600,500)


    def button_click(self):
        # Connects the buttons to their respective functions
        self.submit.clicked.connect(self.translate_click)
        self.reverse.clicked.connect(self.reverse_click)
        self.reset.clicked.connect(self.reset_app)


    def translate_click(self):
        value_to_key1 = self.output_option.currentText()
        value_to_key2 = self.input_option.currentText()

        # Gets the key from the value in the dictionary
        key_to_value1 = [key for key, value in LANGUAGES.items() if value == value_to_key1]
        key_to_value2 = [key for key, value in LANGUAGES.items() if value == value_to_key2]

        # Translates the text in the input box to the output box using the translate_text function
        self.script = self.translate_text(self.input_box.toPlainText(), key_to_value1[0], key_to_value2[0])
        self.output_box.setText(self.script)

    def reset_app(self):
        self.input_box.clear()
        self.output_box.clear()


    # Uses googletrans library to translate the text from the input box to the output box
    # Takes in the text, destination language, and source language as parameters
    def translate_text(self, text, dest, src):
        # Translator is the class from the googletrans module that allows us to translate text
        # Speaker is just the object
        speaker = Translator()
        translation = speaker.translate(text, dest=dest, src=src)
        return translation.text


    def reverse_click(self):
        # Reverses the text in the input and output boxes and swaps the selected languages in the combo boxes
        s1,l1 = self.input_box.toPlainText(), self.input_option.currentText()
        s2,l2 = self.output_box.toPlainText(), self.output_option.currentText()

        self.input_box.setText(s2)
        self.output_box.setText(s1)

        self.input_option.setCurrentText(l2)
        self.output_option.setCurrentText(l1)



#Main Run "I think this is standard procedure"
if __name__ == "__main__":
    app = QApplication([])
    main = Home()
    main.button_click()
    main.show()
    app.exec_()