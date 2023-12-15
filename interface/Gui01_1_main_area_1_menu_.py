# -*- coding: utf-8 -*-
"""Basic GUI for LEnsE Application

This GUI is developped in Python 3 and is based on 
PyQt6 for graphical objects.
It divided in :
- 1 main area (QWidget)
- 1 left menu (QWidget)

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

from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QTimer

from elements.Simple_Widget import SimpleWidget


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
        self.setGeometry(50, 50, 1000, 700)

        # Main Layout
        self.main_widget = QWidget()
        self.main_layout = QGridLayout()
        # Left area of size 1 / 5 of the width
        self.main_layout.setColumnStretch(0, 1)
        # Left area of size 4 / 5 of the width  
        self.main_layout.setColumnStretch(1, 4)
        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)
        
        # Main Area
        self.main_area = SimpleWidget(title='Main Area', 
                    background_color='white',
                    text_color='red')

        # Left Main Menu
        self.main_menu = SimpleWidget(title='Left Menu')

        # Include graphical elements in the window application
        self.main_layout.addWidget(self.main_menu, 0, 0)
        self.main_layout.addWidget(self.main_area, 0, 1)


# -------------------------------

# Launching as main for tests
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
