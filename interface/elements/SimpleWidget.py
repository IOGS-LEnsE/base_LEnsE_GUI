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
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QGridLayout
from PyQt6.QtCore import Qt


class SimpleWidget(QWidget):
    """
    Simple Widget based on QWidget.
    Args:
        QWidget (class): QWidget can be put in another widget and / or window.
    """

    def __init__(self, title='', background_color='#0A3250', text_color='#FFFFFF'):
        """
        Initialisation of the widget.
        """
        super().__init__(parent=None)
        self.title = title
        self.background_color = background_color
        self.text_color = text_color
        
        # Style of the widget - based on CSS
        style_css = "background-color: "+self.background_color+";"
        style_css+= "border-radius: 10px;"
        style_css+= "border-color: black; border-width: 2px; font: bold 12px; padding: 20px;"
        style_css+= "border-style: solid;"
        style_css+= "color: "+self.text_color+";"
        self.setStyleSheet(style_css)

        # Create a self.layout and add widgets
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        # Graphical elements
        self.title_label = QLabel(self.title)
        style_css = "color: "+self.text_color+";"
        self.title_label.setStyleSheet(style_css)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # row = 0
        self.layout.addWidget(self.title_label, 0, 0) 
        
#--------------
# Example to test the Simple_Widget class

if __name__ == '__main__':
    import sys
    from PyQt6.QtGui import QIcon

    class MyWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            # Define Window title
            self.setWindowTitle("LEnsE - Window Title")
            self.setWindowIcon(QIcon('images/IOGS-LEnsE-logo.jpg'))
            self.setGeometry(50, 50, 1000, 700)    
                    
            # Widget to test
            self.main_area = SimpleWidget(title='Main Area', 
                        background_color='white',
                        text_color='red')
            self.setCentralWidget(self.main_area)
    
    app = QApplication(sys.argv)
    main = MyWindow()
    main.show()
    sys.exit(app.exec())
