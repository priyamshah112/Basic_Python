# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'REGISTER.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sqlite3
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

class Ui_Dialog(object):
    def SIGNUPpushButtonShow(self):
        
        username = self.USERNAMElineEdit.text()
        password = self.PASSEDlineEdit.text()
        confirmPassword = self.CONPASSWDlineEdit.text()
        

        connection  = sqlite3.connect("login.db")
        connection.execute("INSERT INTO USERS VALUES(?,?,?)",(username,password,confirmPassword))
        connection.commit()
        connection.close()
        self.showMessageBox('SUCCESSFULLY REGISTERED')
        
       

    def showMessageBox(self,message):
        msgBox = QtGui.QMessageBox()
        msgBox.setIcon(QtGui.QMessageBox.Warning)
        
        msgBox.setText(message)
        msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
        msgBox.exec_()
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1308, 864)
        Dialog.setStyleSheet(_fromUtf8("background-color: rgb(170, 255, 255);"))
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 1291, 851))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame = QtGui.QFrame(self.verticalLayoutWidget)
        self.frame.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 255);"))
        self.frame.setFrameShape(QtGui.QFrame.Box)
        self.frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame.setLineWidth(2)
        self.frame.setMidLineWidth(2)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(400, 30, 591, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Felix Titling"))
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("color: rgb(170, 0, 0);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.frame_2 = QtGui.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(210, 140, 871, 531))
        self.frame_2.setStyleSheet(_fromUtf8("border-color: rgb(170, 0, 0);"))
        self.frame_2.setFrameShape(QtGui.QFrame.Box)
        self.frame_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame_2.setLineWidth(2)
        self.frame_2.setMidLineWidth(2)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.label_2 = QtGui.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(340, 30, 261, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Felix Titling"))
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(170, 0, 0);"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 261, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Felix Titling"))
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("color: rgb(170, 0, 0);"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(20, 250, 261, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Felix Titling"))
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(_fromUtf8("color: rgb(170, 0, 0);"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(20, 350, 441, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Felix Titling"))
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(_fromUtf8("color: rgb(170, 0, 0);"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(20, 450, 261, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Felix Titling"))
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(_fromUtf8("color: rgb(170, 0, 0);"))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.USERNAMElineEdit = QtGui.QLineEdit(self.frame_2)
        self.USERNAMElineEdit.setGeometry(QtCore.QRect(570, 140, 241, 41))
        self.USERNAMElineEdit.setStyleSheet(_fromUtf8("background-color: rgb(255, 170, 0);"))
        self.USERNAMElineEdit.setObjectName(_fromUtf8("USERNAMElineEdit"))
        self.PASSEDlineEdit = QtGui.QLineEdit(self.frame_2)
        ##############################################
        self.PASSEDlineEdit.setEchoMode(QtGui.QLineEdit.Password)

        self.PASSEDlineEdit.setGeometry(QtCore.QRect(570, 240, 241, 41))
        self.PASSEDlineEdit.setStyleSheet(_fromUtf8("background-color: rgb(255, 170, 0);"))
        self.PASSEDlineEdit.setObjectName(_fromUtf8("PASSEDlineEdit"))
        self.CONPASSWDlineEdit = QtGui.QLineEdit(self.frame_2)
        #####################################################3
        self.CONPASSWDlineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.CONPASSWDlineEdit.setGeometry(QtCore.QRect(570, 350, 241, 41))
        self.CONPASSWDlineEdit.setStyleSheet(_fromUtf8("background-color: rgb(255, 170, 0);"))
        self.CONPASSWDlineEdit.setObjectName(_fromUtf8("CONPASSWDlineEdit"))
        self.CATEGORYcomboBox = QtGui.QComboBox(self.frame_2)
        self.CATEGORYcomboBox.setGeometry(QtCore.QRect(580, 451, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.CATEGORYcomboBox.setFont(font)
        self.CATEGORYcomboBox.setStyleSheet(_fromUtf8("color: rgb(170, 0, 0);\n"
"background-color: rgb(255, 255, 255);"))
        self.CATEGORYcomboBox.setObjectName(_fromUtf8("CATEGORYcomboBox"))
        self.CATEGORYcomboBox.addItem(_fromUtf8(""))
        self.CATEGORYcomboBox.addItem(_fromUtf8(""))
        self.CATEGORYcomboBox.addItem(_fromUtf8(""))
        self.SIGNUPpushButton = QtGui.QPushButton(self.frame)
        self.SIGNUPpushButton.setGeometry(QtCore.QRect(570, 740, 281, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Felix Titling"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.SIGNUPpushButton.setFont(font)
        self.SIGNUPpushButton.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 255, 0);"))
        self.SIGNUPpushButton.setObjectName(_fromUtf8("SIGNUPpushButton"))
        self.SIGNUPpushButton.clicked.connect(self.SIGNUPpushButtonShow)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "WELCOME ! NEW USER", None))
        self.label_2.setText(_translate("Dialog", "REGISTER", None))
        self.label_3.setText(_translate("Dialog", "USERNAME", None))
        self.label_4.setText(_translate("Dialog", "PASSWORD", None))
        self.label_5.setText(_translate("Dialog", "CONFIRM PASSWORD", None))
        self.label_6.setText(_translate("Dialog", "CATEGORY", None))
        self.CATEGORYcomboBox.setItemText(0, _translate("Dialog", "PRINCIPAL", None))
        self.CATEGORYcomboBox.setItemText(1, _translate("Dialog", "TEACHER", None))
        self.CATEGORYcomboBox.setItemText(2, _translate("Dialog", "STUDENT", None))
        self.SIGNUPpushButton.setText(_translate("Dialog", "SIGN UP", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

