# -*- coding: utf-8 -*-
"""Basic GUI for LEnsE Application

This GUI is developped in Python 3 and is based on 
PyQt6 for graphical objects.

This example shows how to use events on buttons to update labels between two different widgets.

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

from elements.SignalWidget import SignalWidget


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
        # Main area of size 4 / 5 of the width  
        self.main_layout.setColumnStretch(1, 4)
        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)
        
        # Main Area
        self.main_area = SignalWidget(title='Main Area')

        # Left Main Menu
        self.main_menu = SignalWidget(title='Left Menu')
        self.main_menu.my_signal.connect(self.action_menu)
        self.main_area.my_signal.connect(self.action_main)

        # Include graphical elements in the window application
        self.main_layout.addWidget(self.main_menu, 0, 0)
        self.main_layout.addWidget(self.main_area, 0, 1)


    def action_menu(self, event):
        """
        Processes main menu events.
        """
        self.main_area.update_title('New Area')
        style_css = "background-color: black;"
        style_css += "color: white;"
        self.main_area.title_label.setStyleSheet(style_css)
        print('menu action')


    def action_main(self, event):
        """
        Processes main area events.
        """
        style_css = "background-color: white;"
        style_css += "color: black;"
        self.main_area.title_label.setStyleSheet(style_css)
        print('main action')

# -------------------------------

# Launching as main for tests
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    # CSS Style
    with open("gui04_style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    sys.exit(app.exec())
