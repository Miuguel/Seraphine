from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget, QHBoxLayout, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy)

from app.components.champion_icon_widget import RoundIcon
from app.components.color_label import ColorLabel
from app.components.animation_frame import ColorAnimationFrame


class TftUnitIcon(QWidget):
    '''云顶之弈棋子图标, 图标下方显示星级'''

    def __init__(self, unit: dict, parent=None):
        super().__init__(parent)

        self.vBoxLayout = QVBoxLayout(self)

        self.icon = RoundIcon(unit['icon'], 32, 2, 2)

        self.starsLabel = QLabel("★" * unit['tier'])
        self.starsLabel.setAlignment(Qt.AlignCenter)
        self.starsLabel.setStyleSheet(
            "QLabel {font: 9px; color: rgb(230, 171, 46);}")

        self.vBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.vBoxLayout.setSpacing(0)
        self.vBoxLayout.addWidget(self.icon, alignment=Qt.AlignCenter)
        self.vBoxLayout.addWidget(self.starsLabel)


class TftGameInfoBar(ColorAnimationFrame):
    '''云顶之弈战绩条, 布局与 `GameInfoBar` 保持一致的观感'''

    def __init__(self, game: dict, parent: QWidget = None):
        type = 'win' if game['win'] else 'lose'

        super().__init__(type=type, parent=parent)

        self.hBoxLayout = QHBoxLayout(self)

        self.placementLabel = ColorLabel(f"#{game['placement']}", type)
        self.placementLabel.setAlignment(Qt.AlignCenter)
        self.placementLabel.setFixedWidth(64)

        self.infoLayout = QVBoxLayout()
        self.modeLabel = QLabel(game['modeName'])

        level = self.tr("Level") + f" {game['level']}"
        setName = f" · {game['setName']}" if game['setName'] else ""
        self.timeLabel = QLabel(
            f"{level}{setName} · {game['duration']} · {game['time']}")

        self.unitsLayout = QHBoxLayout()

        self.__initWidget()
        self.__initLayout(game['units'])

    def __initWidget(self):
        font = self.placementLabel.font()
        font.setPixelSize(26)
        font.setBold(True)
        self.placementLabel.setFont(font)

        self.modeLabel.setStyleSheet("QLabel {font: bold 14px;}")
        self.timeLabel.setStyleSheet("QLabel {font: 12px;}")

    def __initLayout(self, units):
        self.infoLayout.setSpacing(2)
        self.infoLayout.addSpacerItem(
            QSpacerItem(1, 1, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.infoLayout.addWidget(self.modeLabel)
        self.infoLayout.addWidget(self.timeLabel)
        self.infoLayout.addSpacerItem(
            QSpacerItem(1, 1, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.unitsLayout.setSpacing(2)
        for unit in units:
            self.unitsLayout.addWidget(TftUnitIcon(unit))

        self.hBoxLayout.setContentsMargins(11, 8, 11, 8)
        self.hBoxLayout.addWidget(self.placementLabel)
        self.hBoxLayout.addSpacing(4)
        self.hBoxLayout.addLayout(self.infoLayout)
        self.hBoxLayout.addSpacerItem(
            QSpacerItem(1, 1, QSizePolicy.Expanding, QSizePolicy.Minimum))
        self.hBoxLayout.addLayout(self.unitsLayout)
