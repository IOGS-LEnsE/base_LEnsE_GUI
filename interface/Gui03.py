# -*- coding: utf-8 -*-
"""Basic GUI for LEnsE Application

This GUI is developped in Python 3 and is based on 
PyQt6 for graphical objects.

This example shows how to use events on buttons to update labels.

---------------------------------------
(c) 2023 - LEnsE - Institut d'Optique
---------------------------------------

Modifications
-------------
    Creation on 2023/12/15


Authors
-------
    Julien VILLEMEJANE
"""

# Libraries to import
import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton
from PyQt6.QtGui import QIcon

from elements.SimpleWidget import SimpleWidget


# -------------------------------

class MainWindow(QMainWindow):
    """
    Our main window.

    Args:
        QMainWindow (class): QMainWindow can contain several widgets.
    """

    def __init__(self):
        """
        Initialisation of the main Window.
        """
        super().__init__()
        
        # Define Window title
        self.setWindowTitle("LEnsE - Window Title")
        self.setWindowIcon(QIcon('images/IOGS-LEnsE-logo.jpg'))
        self.setGeometry(50, 50, 500, 400)
        # Main Widget
        self.main_widget = QWidget()

        # Main Layout
        self.main_layout = QVBoxLayout()
        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)
        
        # Buttons
        self.button1 = QPushButton('Click 1')
        self.button1.clicked.connect(self.button1_action)
        self.button2 = QPushButton('Click 2')
        self.button2.clicked.connect(self.button2_action)
        self.button2.setEnabled(False)
        
        # Labels
        self.label1 = QLabel('Nothing 1')
        self.label2 = QLabel('Nothing 2')
        
        # Integration in the main area
        self.main_layout.addWidget(self.button1)
        self.main_layout.addWidget(self.label1)
        self.main_layout.addWidget(self.button2)
        self.main_layout.addWidget(self.label2)
        

    def button1_action(self):
        """
        Action to process when button1 is clicked.
        """
        self.button2.setEnabled(True)  # Button2 is now enabled
        self.label1.setText('Click on the 2nd button')


    def button2_action(self):
        """
        Action to process when button2 is clicked.
        """
        self.button1.setEnabled(False)  # Button1 is now disabled
        self.label2.setText('Button 2 was clicked')


# -------------------------------

# Launching as main for tests
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
