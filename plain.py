# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginpage.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(827, 591)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMouseTracking(False)
        MainWindow.setTabletTracking(False)
        MainWindow.setAcceptDrops(False)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        MainWindow.setAnimated(True)
        self.centralwidget = centralwidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(-1, -1, 30, 30)
        self.gridLayout.setSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.login_widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.login_widget.sizePolicy().hasHeightForWidth())
        self.login_widget.setSizePolicy(sizePolicy)
        self.login_widget.setMinimumSize(QtCore.QSize(280, 350))
        self.login_widget.setMaximumSize(QtCore.QSize(16777215, 400))
        self.login_widget.setStyleSheet("#login_widget { \n"
"border: 1px solid #000000;\n"
"border-radius: 5px; /* Rounded corners */\n"
" }\n"
"#login_button {\n"
"    margin-left: 30px;\n"
"    margin-right: 40px;\n"
"}\n"
"")
        self.login_widget.setObjectName("login_widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.login_widget)
        self.verticalLayout.setContentsMargins(15, -1, 15, 20)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.username_input = QtWidgets.QLineEdit(self.login_widget)
        self.username_input.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.username_input.sizePolicy().hasHeightForWidth())
        self.username_input.setSizePolicy(sizePolicy)
        self.username_input.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.username_input.setFont(font)
        self.username_input.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #CCCCCC;\n"
"    border-radius: 5px;\n"
"    background-color: #f0f2f5;\n"
"    padding: 5px; /* Add some padding for better spacing */\n"
"    color: #333333;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: #999999; /* Placeholder text color */\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid #007ACC; /* Change the border color on focus */\n"
"    box-shadow: 0 0 5px rgba(0, 122, 204, 0.5); /* Add a box shadow on focus */\n"
"}\n"
"\n"
"")
        self.username_input.setFrame(True)
        self.username_input.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.username_input.setCursorPosition(0)
        self.username_input.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.username_input.setReadOnly(False)
        self.username_input.setClearButtonEnabled(False)
        self.username_input.setObjectName("username_input")
        self.verticalLayout.addWidget(self.username_input)
        spacerItem1 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.password_input = QtWidgets.QLineEdit(self.login_widget)
        self.password_input.setMinimumSize(QtCore.QSize(30, 35))
        self.password_input.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #CCCCCC;\n"
"    border-radius: 5px;\n"
"    background-color: #f0f2f5;\n"
"    padding: 5px; /* Add some padding for better spacing */\n"
"    color: #333333;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: #999999; /* Placeholder text color */\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid #007ACC; /* Change the border color on focus */\n"
"    box-shadow: 0 0 5px rgba(0, 122, 204, 0.5); /* Add a box shadow on focus */\n"
"}\n"
"")
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setObjectName("password_input")
        self.verticalLayout.addWidget(self.password_input)
        spacerItem2 = QtWidgets.QSpacerItem(20, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.login_button = QtWidgets.QPushButton(self.login_widget)
        self.login_button.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_button.sizePolicy().hasHeightForWidth())
        self.login_button.setSizePolicy(sizePolicy)
        self.login_button.setMinimumSize(QtCore.QSize(50, 40))
        self.login_button.setMaximumSize(QtCore.QSize(2000, 16777215))
        self.login_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.login_button.setStyleSheet("QPushButton {\n"
"border-radius:10px;\n"
"background-color: rgb(0, 255, 0);\n"
"border-style:outlet;\n"
"padding:5px;\n"
"border-radius:10px;\n"
"border: 2px solid #21ff1d;\n"
"border-style:outset;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:rgb(34, 244, 19)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #6eff6e stop: 1 #6effaa\n"
"        );\n"
"}\n"
"")
        self.login_button.setObjectName("login_button")
        self.verticalLayout.addWidget(self.login_button)
        spacerItem3 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem3)
        self.frame = QtWidgets.QFrame(self.login_widget)
        self.frame.setStyleSheet("background: transparent;\n"
"border: none;\n"
"border-top: 1px dotted black;\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.HLine)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(1)
        self.frame.setObjectName("frame")
        self.verticalLayout.addWidget(self.frame)
        self.pushButton = QtWidgets.QPushButton(self.login_widget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton.setStyleSheet("QPushButton {\n"
"border-radius:10px;\n"
"background-color: rgb(0, 255, 0);\n"
"border-style:outlet;\n"
"padding:5px;\n"
"border-radius:10px;\n"
"border: 2px solid #21ff1d;\n"
"border-style:outset;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:rgb(34, 244, 19)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #6eff6e stop: 1 #6effaa\n"
"        );\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.gridLayout.addWidget(self.login_widget, 2, 1, 1, 1)
        self.Title = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Title.sizePolicy().hasHeightForWidth())
        self.Title.setSizePolicy(sizePolicy)
        self.Title.setMinimumSize(QtCore.QSize(50, 80))
        self.Title.setStyleSheet("border:none;\n"
"")
        self.Title.setObjectName("Title")
        self.gridLayout.addWidget(self.Title, 0, 0, 1, 2)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMaximumSize(QtCore.QSize(500, 16777215))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(-1, 9, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setUnderline(False)
        font.setKerning(True)
        self.textBrowser.setFont(font)
        self.textBrowser.setAutoFillBackground(False)
        self.textBrowser.setStyleSheet("border:none;")
        self.textBrowser.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.textBrowser.setMidLineWidth(3)
        self.textBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.textBrowser.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.gridLayout.addWidget(self.frame_2, 2, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 1, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 3, 1, 1, 1)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 827, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.login_button.clicked.connect(self.login_button.click) # type: ignore
        self.pushButton.clicked.connect(self.pushButton.click) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>tyy</p><p><br/></p></body></html>"))
        self.username_input.setPlaceholderText(_translate("MainWindow", "Username"))
        self.password_input.setPlaceholderText(_translate("MainWindow", "Password"))
        self.login_button.setText(_translate("MainWindow", "Login"))
        self.pushButton.setText(_translate("MainWindow", "Create New Account"))
        self.Title.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Montserrat\'; font-size:28pt;\">Openings Insight</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:18pt;\">Login Page</span></p></body></html>"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:16pt;\">The program that teaches you common chess openings and the ideas behind them.</span></p></body></html>"))
from centralwidget import centralwidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
