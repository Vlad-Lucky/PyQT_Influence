# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'influence_gaming_starting_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(571, 441)
        MainWindow.setStyleSheet("background-color: black")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tab_widget = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_widget.setGeometry(QtCore.QRect(0, 0, 571, 441))
        self.tab_widget.setObjectName("tab_widget")
        self.game_tab_widget = QtWidgets.QWidget()
        self.game_tab_widget.setObjectName("game_tab_widget")
        self.widget_hexagon_grid = QtWidgets.QWidget(self.game_tab_widget)
        self.widget_hexagon_grid.setGeometry(QtCore.QRect(0, 94, 564, 321))
        self.widget_hexagon_grid.setObjectName("widget_hexagon_grid")
        self.base_game = QtWidgets.QWidget(self.game_tab_widget)
        self.base_game.setGeometry(QtCore.QRect(0, 0, 561, 91))
        self.base_game.setObjectName("base_game")
        self.attack_phase = QtWidgets.QWidget(self.base_game)
        self.attack_phase.setEnabled(True)
        self.attack_phase.setGeometry(QtCore.QRect(0, 0, 71, 71))
        self.attack_phase.setStyleSheet("")
        self.attack_phase.setObjectName("attack_phase")
        self.battle_phase = QtWidgets.QHBoxLayout(self.attack_phase)
        self.battle_phase.setContentsMargins(0, 0, 0, 0)
        self.battle_phase.setSpacing(0)
        self.battle_phase.setObjectName("battle_phase")
        self.next_phase_btn = QtWidgets.QPushButton(self.attack_phase)
        self.next_phase_btn.setMinimumSize(QtCore.QSize(0, 0))
        self.next_phase_btn.setStyleSheet("background-color: gray")
        self.next_phase_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/gaming/images/gaming/next_phase.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.next_phase_btn.setIcon(icon)
        self.next_phase_btn.setIconSize(QtCore.QSize(64, 64))
        self.next_phase_btn.setObjectName("next_phase_btn")
        self.battle_phase.addWidget(self.next_phase_btn)
        self.reinforcement_phase = QtWidgets.QWidget(self.base_game)
        self.reinforcement_phase.setEnabled(False)
        self.reinforcement_phase.setGeometry(QtCore.QRect(72, 0, 211, 71))
        self.reinforcement_phase.setObjectName("reinforcement_phase")
        self.replenishment_phase = QtWidgets.QHBoxLayout(self.reinforcement_phase)
        self.replenishment_phase.setContentsMargins(0, 0, 0, 0)
        self.replenishment_phase.setSpacing(1)
        self.replenishment_phase.setObjectName("replenishment_phase")
        self.plus_one_btn = QtWidgets.QPushButton(self.reinforcement_phase)
        self.plus_one_btn.setStyleSheet("background-color: gray")
        self.plus_one_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/gaming/images/gaming/plus_one.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.plus_one_btn.setIcon(icon1)
        self.plus_one_btn.setIconSize(QtCore.QSize(64, 64))
        self.plus_one_btn.setCheckable(True)
        self.plus_one_btn.setChecked(False)
        self.plus_one_btn.setObjectName("plus_one_btn")
        self.replenishment_phase.addWidget(self.plus_one_btn)
        self.max_btn = QtWidgets.QPushButton(self.reinforcement_phase)
        self.max_btn.setStyleSheet("background-color: gray")
        self.max_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/gaming/images/gaming/to_max.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.max_btn.setIcon(icon2)
        self.max_btn.setIconSize(QtCore.QSize(64, 64))
        self.max_btn.setCheckable(True)
        self.max_btn.setObjectName("max_btn")
        self.replenishment_phase.addWidget(self.max_btn)
        self.skip_btn = QtWidgets.QPushButton(self.reinforcement_phase)
        self.skip_btn.setStyleSheet("background-color: gray")
        self.skip_btn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/gaming/images/gaming/skip.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.skip_btn.setIcon(icon3)
        self.skip_btn.setIconSize(QtCore.QSize(64, 64))
        self.skip_btn.setObjectName("skip_btn")
        self.replenishment_phase.addWidget(self.skip_btn)
        self.status_text = QtWidgets.QLabel(self.base_game)
        self.status_text.setGeometry(QtCore.QRect(290, 20, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.status_text.setFont(font)
        self.status_text.setStyleSheet("color: gray")
        self.status_text.setTextFormat(QtCore.Qt.AutoText)
        self.status_text.setObjectName("status_text")
        self.progress_bar = QtWidgets.QProgressBar(self.base_game)
        self.progress_bar.setGeometry(QtCore.QRect(290, 50, 271, 21))
        self.progress_bar.setStyleSheet("QProgressBar::chunk {\n"
"    background-color: #3add36;\n"
"    width: 1px;\n"
" }\n"
"\n"
" QProgressBar {\n"
"    border: 2px solid grey;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"    color: gray\n"
" }")
        self.progress_bar.setMinimum(0)
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setObjectName("progress_bar")
        self.reinforcement_points_label = QtWidgets.QLabel(self.base_game)
        self.reinforcement_points_label.setGeometry(QtCore.QRect(290, 0, 121, 20))
        self.reinforcement_points_label.setStyleSheet("color: gray")
        self.reinforcement_points_label.setObjectName("reinforcement_points_label")
        self.reinforcement_points = QtWidgets.QLabel(self.base_game)
        self.reinforcement_points.setGeometry(QtCore.QRect(410, 0, 121, 20))
        self.reinforcement_points.setStyleSheet("color: gray")
        self.reinforcement_points.setObjectName("reinforcement_points")
        self.now_phase_lb = QtWidgets.QLabel(self.base_game)
        self.now_phase_lb.setGeometry(QtCore.QRect(0, 70, 561, 20))
        self.now_phase_lb.setStyleSheet("color: white")
        self.now_phase_lb.setAlignment(QtCore.Qt.AlignCenter)
        self.now_phase_lb.setObjectName("now_phase_lb")
        self.tab_widget.addTab(self.game_tab_widget, "")
        self.statistics_tab_widget = QtWidgets.QWidget()
        self.statistics_tab_widget.setObjectName("statistics_tab_widget")
        self.tab_widget.addTab(self.statistics_tab_widget, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.restart_this_map = QtWidgets.QAction(MainWindow)
        self.restart_this_map.setObjectName("restart_this_map")
        self.restart_new_map = QtWidgets.QAction(MainWindow)
        self.restart_new_map.setObjectName("restart_new_map")
        self.exit_to_main_menu = QtWidgets.QAction(MainWindow)
        self.exit_to_main_menu.setObjectName("exit_to_main_menu")

        self.retranslateUi(MainWindow)
        self.tab_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.status_text.setText(_translate("MainWindow", "Игрок Абдулах Игоревич победил!"))
        self.progress_bar.setFormat(_translate("MainWindow", "Поле заполнено на: %p%"))
        self.reinforcement_points_label.setText(_translate("MainWindow", "Очков на заполнение:"))
        self.reinforcement_points.setText(_translate("MainWindow", "100"))
        self.now_phase_lb.setText(_translate("MainWindow", "Фаза атаки"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.game_tab_widget), _translate("MainWindow", "Игра"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.statistics_tab_widget), _translate("MainWindow", "Статистика"))
        self.restart_this_map.setText(_translate("MainWindow", "Перезапустить на этой карте"))
        self.restart_new_map.setText(_translate("MainWindow", "Перезапустить на новой карте"))
        self.exit_to_main_menu.setText(_translate("MainWindow", "Выход в главное меню"))
from .. import ui_resource_rc
