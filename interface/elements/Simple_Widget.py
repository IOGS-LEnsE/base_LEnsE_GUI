# -*- coding: utf-8 -*-
"""
SimpleWidget for LEnsE GUI Application

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


# Graphical interface
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QPushButton, QGridLayout, QComboBox, QSlider, QLineEdit
    )
from PyQt6.QtGui import QPixmap, QImage
from pyqtgraph import PlotWidget, plot, mkPen


from PyQt6.QtWidgets import QMainWindow, QLabel, QComboBox, QWidget, QGroupBox
from PyQt6.QtCore import QTimer, Qt

#-----------------------------------------------------------------------------------------------

class SimpleWidget(QWidget):
    """
    Simple Widget based on QWidget.
    Args:
        QWidget (class): QWidget can be put in another widget and / or window.
    """

    def __init__(self, title=''):
        """
        Initialisation of our camera widget.
        """
        super().__init__(parent=None)
        self.title = title
        
        # Style of the widget - based on CSS
        self.setStyleSheet("background-color: #4472c4; border-radius: 10px;"
                           "border-color: black; border-width: 2px; font: bold 12px; padding: 20px;"
                           "border-style: solid;")

        # Create a self.layout and add widgets
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        # Graphical elements
        self.title_label = QLabel(self.title)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # row = 0
        self.layout.addWidget(self.title_label, 0, 0) 
        

