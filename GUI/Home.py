# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Home.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HomeWindow(object):
    def setupUi(self, HomeWindow):
        HomeWindow.setObjectName("HomeWindow")
        HomeWindow.resize(1089, 788)
        HomeWindow.setStyleSheet("")
        self.widget = QtWidgets.QWidget(HomeWindow)
        self.widget.setGeometry(QtCore.QRect(0, -50, 1091, 801))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.widget.setFont(font)
        self.widget.setStyleSheet("color:black;\n"
"\n"
"\n"
"\n"
"QDoubleSpinBox\n"
"{\n"
"background-color: rgb(200, 200, 200);\n"
"color:black;\n"
"}\n"
"QDoubleSpinBox:hover {\n"
"  background-color:  rgb(166, 166, 166);\n"
"  color: white;\n"
"}\n"
"QListWidget\n"
"{\n"
"background-color: rgb(200, 200, 200);\n"
"color:black;\n"
"}\n"
"QListWidget:hover {\n"
"  background-color:  rgb(166, 166, 166);\n"
"  color: white;\n"
"}\n"
"QListView{\n"
"background-color:  rgb(255, 255, 255);\n"
"  color: white;\n"
"}\n"
"\n"
"QComboBox{\n"
"background-color:  rgb(200, 200, 200);\n"
"color:black;\n"
"}\n"
"QComboBox:hover {\n"
"  background-color:  rgb(166, 166, 166);\n"
"  color: white;\n"
"}\n"
"\n"
"QTextBrowser\n"
"{\n"
"background-color: black;\n"
"color:white;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 8px;\n"
"color:black;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"  background-color:  rgb(166, 166, 166);\n"
"  color: white;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox\n"
"{\n"
"background-color: rgb(200, 200, 200);\n"
"\n"
"color:balck;\n"
"}\n"
"QSpinBox:hover {\n"
"  background-color:  rgb(166, 166, 166);\n"
"  color: white;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QLabel\n"
"{\n"
"color: white;\n"
"}\n"
"\n"
"\n"
"")
        self.widget.setObjectName("widget")
        self.load_image = QtWidgets.QPushButton(self.widget)
        self.load_image.setGeometry(QtCore.QRect(70, 50, 113, 32))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.load_image.setFont(font)
        self.load_image.setObjectName("load_image")
        self.loaded_image_widget = QtWidgets.QWidget(self.widget)
        self.loaded_image_widget.setGeometry(QtCore.QRect(550, 30, 511, 381))
        self.loaded_image_widget.setStyleSheet("QWidget\n"
"{\n"
"    background-color: white;\n"
"}\n"
"\n"
"\n"
"")
        self.loaded_image_widget.setObjectName("loaded_image_widget")
        self.image_slider = QtWidgets.QSlider(self.widget)
        self.image_slider.setGeometry(QtCore.QRect(540, 440, 511, 22))
        self.image_slider.setAcceptDrops(False)
        self.image_slider.setAutoFillBackground(False)
        self.image_slider.setMaximum(10)
        self.image_slider.setOrientation(QtCore.Qt.Horizontal)
        self.image_slider.setInvertedAppearance(False)
        self.image_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.image_slider.setTickInterval(0)
        self.image_slider.setObjectName("image_slider")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(780, 420, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(HomeWindow)
        QtCore.QMetaObject.connectSlotsByName(HomeWindow)

    def retranslateUi(self, HomeWindow):
        _translate = QtCore.QCoreApplication.translate
        HomeWindow.setWindowTitle(_translate("HomeWindow", "Form"))
        self.load_image.setText(_translate("HomeWindow", "Load Images"))
        self.label.setText(_translate("HomeWindow", "Image Number"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HomeWindow = QtWidgets.QWidget()
    ui = Ui_HomeWindow()
    ui.setupUi(HomeWindow)
    HomeWindow.show()
    sys.exit(app.exec_())
