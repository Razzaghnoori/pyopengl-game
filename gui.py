# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created: Sun Jul 30 10:10:15 2017
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import main

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_mainDialog(object):
    def setupUi(self, mainDialog):

        # defining window size
        mainDialog.setObjectName(_fromUtf8("mainDialog"))
        mainDialog.resize(800, 600)
        mainDialog.setMinimumSize(QtCore.QSize(800, 600))
        mainDialog.setMaximumSize(QtCore.QSize(800, 600))

        # creating "start game" button
        self.startgame = QtGui.QPushButton(mainDialog)
        self.startgame.setGeometry(QtCore.QRect(560, 420, 98, 27))
        self.startgame.setObjectName(_fromUtf8("startgame"))

        self.groupBox = QtGui.QGroupBox(mainDialog)
        self.groupBox.setGeometry(QtCore.QRect(490, 30, 51, 41))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))

        #creating GroupBox for voice section
        self.voice_gpbox = QtGui.QGroupBox(mainDialog)
        self.voice_gpbox.setGeometry(QtCore.QRect(30, 270, 381, 221))
        self.voice_gpbox.setObjectName(_fromUtf8("voice_gpbox"))
        self.widget = QtGui.QWidget(self.voice_gpbox)
        self.widget.setGeometry(QtCore.QRect(0, 20, 371, 170))
        self.widget.setObjectName(_fromUtf8("widget"))

	#vertical layout for elements in groupbox
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        
        # setting up background voice section , including label , text input and radio buttons
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.background_lbl = QtGui.QLabel(self.widget)
        self.background_lbl.setMinimumSize(QtCore.QSize(54, 50))
        self.background_lbl.setObjectName(_fromUtf8("background_lbl"))
        self.horizontalLayout_7.addWidget(self.background_lbl)
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.backpath = QtGui.QLineEdit(self.widget)
        self.backpath.setObjectName(_fromUtf8("backpath"))
        self.horizontalLayout_7.addWidget(self.backpath)

        #group box for radio buttons
        self.backgroun_gpbox = QtGui.QGroupBox(self.widget)
        self.backgroun_gpbox.setMinimumSize(QtCore.QSize(54, 50))
        self.backgroun_gpbox.setBaseSize(QtCore.QSize(54, 50))
        self.backgroun_gpbox.setTitle(_fromUtf8(""))
        self.backgroun_gpbox.setObjectName(_fromUtf8("backgroun_gpbox"))
        self.widget1 = QtGui.QWidget(self.backgroun_gpbox)
        self.widget1.setGeometry(QtCore.QRect(0, 0, 55, 52))
        self.widget1.setObjectName(_fromUtf8("widget1"))

        # layout for radio buttons
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))

        self.back_on = QtGui.QRadioButton(self.widget1)
        self.back_on.setChecked(True)
        self.back_on.setObjectName(_fromUtf8("back_on"))
        self.verticalLayout_2.addWidget(self.back_on)
        self.back_off = QtGui.QRadioButton(self.widget1)
        self.back_off.setObjectName(_fromUtf8("back_off"))
        self.verticalLayout_2.addWidget(self.back_off)
        self.horizontalLayout_7.addWidget(self.backgroun_gpbox)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
	
	# setting up background voice section , including label , text input and radio buttons
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.speec_lbl = QtGui.QLabel(self.widget)
        self.speec_lbl.setObjectName(_fromUtf8("speec_lbl"))
        self.horizontalLayout_3.addWidget(self.speec_lbl)
        spacerItem1 = QtGui.QSpacerItem(50, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.speechpath = QtGui.QLineEdit(self.widget)
        self.speechpath.setObjectName(_fromUtf8("speechpath"))
        self.horizontalLayout_3.addWidget(self.speechpath)

        #group box for radio buttons
        self.speech_gpbox = QtGui.QGroupBox(self.widget)
        self.speech_gpbox.setEnabled(True)
        self.speech_gpbox.setMinimumSize(QtCore.QSize(54, 50))
        self.speech_gpbox.setBaseSize(QtCore.QSize(54, 50))
        self.speech_gpbox.setTitle(_fromUtf8(""))
        self.speech_gpbox.setObjectName(_fromUtf8("speech_gpbox"))

        # layout for radio buttons
        self.layoutWidget = QtGui.QWidget(self.speech_gpbox)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 55, 52))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))

        self.speech_on = QtGui.QRadioButton(self.layoutWidget)
        self.speech_on.setChecked(True)
        self.speech_on.setObjectName(_fromUtf8("speech_on"))
        self.verticalLayout_4.addWidget(self.speech_on)
        self.speech_off = QtGui.QRadioButton(self.layoutWidget)
        self.speech_off.setObjectName(_fromUtf8("speech_off"))
        self.verticalLayout_4.addWidget(self.speech_off)
        self.horizontalLayout_3.addWidget(self.speech_gpbox)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()

        # setting up speech voice section , including label , text input and radio buttons
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.shooting_lbl = QtGui.QLabel(self.widget)
        self.shooting_lbl.setObjectName(_fromUtf8("shooting_lbl"))
        self.horizontalLayout_8.addWidget(self.shooting_lbl)
        spacerItem2 = QtGui.QSpacerItem(38, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.shootingpath = QtGui.QLineEdit(self.widget)
        self.shootingpath.setObjectName(_fromUtf8("shootingpath"))
        self.horizontalLayout_8.addWidget(self.shootingpath)

        #group box for radio buttons
        self.shooting_gpbox = QtGui.QGroupBox(self.widget)
        self.shooting_gpbox.setEnabled(True)
        self.shooting_gpbox.setMinimumSize(QtCore.QSize(54, 50))
        self.shooting_gpbox.setBaseSize(QtCore.QSize(54, 50))
        self.shooting_gpbox.setTitle(_fromUtf8(""))
        self.shooting_gpbox.setObjectName(_fromUtf8("shooting_gpbox"))
        self.layoutWidget_4 = QtGui.QWidget(self.shooting_gpbox)
        self.layoutWidget_4.setGeometry(QtCore.QRect(0, 0, 55, 52))

        # layout for radio buttons
        self.layoutWidget_4.setObjectName(_fromUtf8("layoutWidget_4"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_9.setMargin(0)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.shooting_on = QtGui.QRadioButton(self.layoutWidget_4)
        self.shooting_on.setChecked(True)
        self.shooting_on.setObjectName(_fromUtf8("shooting_on"))
        self.verticalLayout_9.addWidget(self.shooting_on)
        self.shooting_off = QtGui.QRadioButton(self.layoutWidget_4)
        self.shooting_off.setObjectName(_fromUtf8("shooting_off"))
        self.verticalLayout_9.addWidget(self.shooting_off)
        self.horizontalLayout_8.addWidget(self.shooting_gpbox)
        self.verticalLayout.addLayout(self.horizontalLayout_8)

        # group box for "general" section
        self.general_gpbox = QtGui.QGroupBox(mainDialog)
        self.general_gpbox.setGeometry(QtCore.QRect(30, 100, 381, 111))
        self.general_gpbox.setObjectName(_fromUtf8("general_gpbox"))
        self.widget2 = QtGui.QWidget(self.general_gpbox)
        self.widget2.setGeometry(QtCore.QRect(0, 30, 373, 66))
        self.widget2.setObjectName(_fromUtf8("widget2"))

        #layout elements in group box
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widget2)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.window_lbl = QtGui.QLabel(self.widget2)
        self.window_lbl.setObjectName(_fromUtf8("window_lbl"))
        self.horizontalLayout.addWidget(self.window_lbl)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)

        #setting up size section
        self.width = QtGui.QSpinBox(self.widget2)
        self.width.setMaximum(1920)
        self.width.setProperty("value", 800)
        self.width.setObjectName(_fromUtf8("width"))
        self.horizontalLayout.addWidget(self.width)
        self.x_lbl = QtGui.QLabel(self.widget2)
        self.x_lbl.setObjectName(_fromUtf8("x_lbl"))
        self.horizontalLayout.addWidget(self.x_lbl)
        self.height = QtGui.QSpinBox(self.widget2)
        self.height.setMaximum(1024)
        self.height.setProperty("value", 400)
        self.height.setObjectName(_fromUtf8("height"))
        self.horizontalLayout.addWidget(self.height)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))

        #setting up light section
        self.light_lbl = QtGui.QLabel(self.widget2)
        self.light_lbl.setObjectName(_fromUtf8("light_lbl"))
        self.horizontalLayout_2.addWidget(self.light_lbl)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.r_lbl = QtGui.QLabel(self.widget2)
        self.r_lbl.setObjectName(_fromUtf8("r_lbl"))
        self.horizontalLayout_2.addWidget(self.r_lbl)
        self.red = QtGui.QSpinBox(self.widget2)
        self.red.setMaximum(255)
        self.red.setProperty("value", 1)
        self.red.setObjectName(_fromUtf8("red"))
        self.horizontalLayout_2.addWidget(self.red)
        self.g_lbl = QtGui.QLabel(self.widget2)
        self.g_lbl.setObjectName(_fromUtf8("g_lbl"))
        self.horizontalLayout_2.addWidget(self.g_lbl)
        self.green = QtGui.QSpinBox(self.widget2)
        self.green.setMaximum(255)
        self.green.setProperty("value", 1)
        self.green.setObjectName(_fromUtf8("green"))
        self.horizontalLayout_2.addWidget(self.green)
        self.b_lbl = QtGui.QLabel(self.widget2)
        self.b_lbl.setObjectName(_fromUtf8("b_lbl"))
        self.horizontalLayout_2.addWidget(self.b_lbl)
        self.blue = QtGui.QSpinBox(self.widget2)
        self.blue.setSingleStep(255)
        self.blue.setProperty("value", 1)
        self.blue.setObjectName(_fromUtf8("blue"))
        self.horizontalLayout_2.addWidget(self.blue)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.retranslateUi(mainDialog)
        QtCore.QMetaObject.connectSlotsByName(mainDialog)

	QtCore.QObject.connect(self.startgame,QtCore.SIGNAL("clicked()"),self.start_btn)

    def start_btn(self):
        
        background_path = self.backpath.text()
        speech_path = self.speechpath.text()
        shooting_path = self.shootingpath.text()

        if self.back_on.isChecked() :
            back=1
        elif self.back_off.isChecked():
            back=0

        if self.speech_on.isChecked() :
            speech=1
        elif self.speech_off.isChecked():
            speech=0

        if self.shooting_on.isChecked() :
            shooting=1
        elif self.shooting_off.isChecked():
            shooting=0
        
        red = self.red.value()
        green=self.green.value()
        blue = self.blue.value()

        height = self.height.value()
        width = self.width.value()

        main.start(height, width, red, green, blue, background_path, speech_path, shooting_path,
          back, speech, shooting)

        close()

    def retranslateUi(self, mainDialog):
        mainDialog.setWindowTitle(_translate("mainDialog", "Dialog", None))
        self.startgame.setText(_translate("mainDialog", "Start Game", None))
        self.voice_gpbox.setTitle(_translate("mainDialog", "Voice", None))
        self.background_lbl.setText(_translate("mainDialog", "Background", None))
        self.back_on.setText(_translate("mainDialog", "on", None))
        self.back_off.setText(_translate("mainDialog", "off", None))
        self.speec_lbl.setText(_translate("mainDialog", "Speech", None))
        self.speech_on.setText(_translate("mainDialog", "on", None))
        self.speech_off.setText(_translate("mainDialog", "off", None))
        self.shooting_lbl.setText(_translate("mainDialog", "Shooting", None))
        self.shooting_on.setText(_translate("mainDialog", "on", None))
        self.shooting_off.setText(_translate("mainDialog", "off", None))
        self.general_gpbox.setTitle(_translate("mainDialog", "General", None))
        self.window_lbl.setText(_translate("mainDialog", "Window Size", None))
        self.x_lbl.setText(_translate("mainDialog", "X", None))
        self.light_lbl.setText(_translate("mainDialog", "Light Color", None))
        self.r_lbl.setText(_translate("mainDialog", "R", None))
        self.g_lbl.setText(_translate("mainDialog", "G", None))
        self.b_lbl.setText(_translate("mainDialog", "B", None))

def close():
    mainDialog.close()

def start_window():
    import sys
    app = QtGui.QApplication(sys.argv)
    mainDialog = QtGui.QDialog()
    ui = Ui_mainDialog()
    ui.setupUi(mainDialog)
    mainDialog.show()
    sys.exit(app.exec_())
    

if __name__ == "__main__":
    
    start_window()
   

