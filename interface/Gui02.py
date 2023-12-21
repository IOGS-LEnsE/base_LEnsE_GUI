# -*- coding: utf-8 -*-
"""Basic GUI for LEnsE Application

This GUI is developped in Python 3 and is based on 
PyQt6 for graphical objects.
It divided in :
- 4 main areas (QWidget)
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
        self.main_layout = QGridLayout()
        # Left area of size 1 / 5 of the width
        self.main_layout.setColumnStretch(0, 1)
        # Main areas of size 2 / 5 of the width  
        self.main_layout.setColumnStretch(1, 2)
        self.main_layout.setColumnStretch(2, 2)
        # Row of size 1 / 2 of the height
        self.main_layout.setRowStretch(0, 1) 
        self.main_layout.setRowStretch(1, 1)
        
        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)
        
        # Main Area
        self.main_area1 = SimpleWidget(title='Main Area 1', 
                    background_color='white',
                    text_color='red')
        self.main_area2 = SimpleWidget(title='Main Area 2', 
                    background_color='gray',
                    text_color='white')
        self.main_area3 = SimpleWidget(title='Main Area 3', 
                    background_color='gray',
                    text_color='black')
        self.main_area4 = SimpleWidget(title='Main Area 4', 
                    background_color='lightgray',
                    text_color='black')

        # Left Main Menu
        self.main_menu = SimpleWidget(title='Left Menu')

        # Include graphical elements in the window application
        self.main_layout.addWidget(self.main_menu, 0, 0, 2, 1)
        self.main_layout.addWidget(self.main_area1, 0, 1)
        self.main_layout.addWidget(self.main_area2, 0, 2)
        self.main_layout.addWidget(self.main_area3, 1, 1)
        self.main_layout.addWidget(self.main_area4, 1, 2)


# -------------------------------

# Launching as main for tests
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
