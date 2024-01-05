# -*- coding: utf-8 -*-
"""
SignalWidget for LEnsE GUI Application

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
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt6.QtCore import Qt, pyqtSignal


class SignalWidget(QWidget):
    """
    Simple Widget based on QWidget.
    Args:
        QWidget (class): QWidget can be put in another widget and / or window.
    """
    my_signal = pyqtSignal(int)

    def __init__(self, title='', background_color='#FFFFFF', text_color='#0A3250'):
        """
        Initialisation of the widget.
        
        :param title: Title of the widget displays in a label, defaults to ''
        :type title: str, optional
        :param background_color: Color of the widget background, defaults to #FFFFFF
        :type background_color: str, optional
        :param text_color: Color of the widget text, defaults to #0A3250
        :type text_color: str, optional
        """
        super().__init__(parent=None)
        self.title = title
        self.background_color = background_color
        self.text_color = text_color

        # Style of the widget - based on CSS
        style_css = "background-color: " + self.background_color + ";"
        style_css += "color: " + self.text_color + ";"
        self.setStyleSheet(style_css)

        # Create a self.layout and add widgets
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Graphical elements
        ## Title label
        self.title_label = QLabel(self.title)
        style_css = "color: " + self.text_color + ";"
        self.title_label.setStyleSheet(style_css)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        ## Button 1
        self.button_1 = QPushButton('Update Main Area')
        self.button_1.clicked.connect(lambda: self.my_signal.emit(int(1)))

        # Integration of the graphical objects
        self.layout.addWidget(self.title_label)
        self.layout.addWidget(self.button_1)

    def update_title(self, title):
        """
        Updates the title of the widget.
        
        :param title: Title of the widget displays in a label
        :type title: str        
        """
        self.title = title
        self.title_label.setText(self.title)


# --------------
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
            self.main_area = SignalWidget(title='Main Area',
                                          background_color='white',
                                          text_color='red')

            self.main_area.my_signal.connect(self.action_menu)
            self.setCentralWidget(self.main_area)

        def action_menu(self, event):
            print('Emitted signal')
            print(event)


    app = QApplication(sys.argv)
    main = MyWindow()
    main.show()
    sys.exit(app.exec())
