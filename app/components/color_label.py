from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QColor
from app.common.style_sheet import ColorChangeable
from app.common.qfluentwidgets import isDarkTheme


class ColorLabel(QLabel, ColorChangeable):
    '''
    The label color will automatically change as the corresponding `type` color changes
    '''

    def __init__(self, text: str = None, type: str = None, parent=None):
        QLabel.__init__(self, text=text, parent=parent)
        ColorChangeable.__init__(self, type)

    def setColor(self, c1, c2, c3, c4):
        self.setStyleSheet(f"ColorLabel {{color: {c1.name()};}}")


class DeathsLabel(ColorLabel):
    def __init__(self, text: str = None, parent=None):
        super().__init__(text=text, type='deaths', parent=parent)

    def setColor(self, c1: QColor, c2, c3, c4):
        self.setStyleSheet(f"DeathsLabel {{color: {c1.name()};}}")
