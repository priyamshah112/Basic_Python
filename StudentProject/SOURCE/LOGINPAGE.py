# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LOGINPAGE.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sqlite3
from BASICDETAILS import Ui_Dialog1
from REGISTER import Ui_Dialog
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

class Ui_contact_lbl(object):
    def EXIT_BTNCheck(self):
        self.showMessageBox1('ARE YOU SURE TO QUIT!')
        sys.exit(app.exec_())
        
    def showMessageBox(self,title,message):
        
            
          
        msgBox = QtGui.QMessageBox()
        msgBox.setText("Successfully Added")
        msgBox.setText(message)
        msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
        msgBox.exec_()
    def showMessageBox1(self,message):
        msgBox = QtGui.QMessageBox()
        msgBox.setIcon(QtGui.QMessageBox.Warning)
        
        msgBox.setText(message)
        msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
        msgBox.exec_()
    def REGISTERpushButtonShow(self):
        self.REGISTERpushButtonWindow = QtGui.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.REGISTERpushButtonWindow)
        self.REGISTERpushButtonWindow.show()
    
        
    def loginCheck(self):
        username = self.USERNAMETXTBX.text()
        password = self.PASSWDTXTBX.text()
        
        connection = sqlite3.connect("login.db")
        result = connection.execute("SELECT * FROM USERS WHERE USERNAME = ? AND PASSWORD = ?",(username,password))
        if(len(result.fetchall()) > 0):
            print("User Found ! ")
            self.loginShowWindow = QtGui.QDialog()
            self.ui = Ui_Dialog1()
            self.ui.setupUi(self.loginShowWindow)
            self.loginShowWindow.show()
            
        else:
            print("User Not Found !")
            self.showMessageBox('Warning','Invalid Username And Password')
        connection.close()
        
    def REGISTERpushButtonCheck(self):
        print(" Sign Up Button Clicked !")
        self.REGISTERpushButtonShow()
    def setupUi(self, contact_lbl):
        contact_lbl.setObjectName(_fromUtf8("contact_lbl"))
        contact_lbl.resize(1118, 731)
        contact_lbl.setStyleSheet(_fromUtf8("background-color: rgb(170, 255, 255);"))
        self.HEADINGLBL = QtGui.QLabel(contact_lbl)
        self.HEADINGLBL.setGeometry(QtCore.QRect(80, 30, 971, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Engravers MT"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.HEADINGLBL.setFont(font)
        self.HEADINGLBL.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.HEADINGLBL.setAutoFillBackground(False)
        self.HEADINGLBL.setStyleSheet(_fromUtf8("color: rgb(170, 0, 0);"))
        self.HEADINGLBL.setObjectName(_fromUtf8("HEADINGLBL"))
        self.NAMELBL = QtGui.QLabel(contact_lbl)
        self.NAMELBL.setGeometry(QtCore.QRect(400, 170, 421, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Felix Titling"))
        font.setPointSize(14)
        self.NAMELBL.setFont(font)
        self.NAMELBL.setAutoFillBackground(False)
        self.NAMELBL.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);"))
        self.NAMELBL.setObjectName(_fromUtf8("NAMELBL"))
        self.frame1 = QtGui.QFrame(contact_lbl)
        self.frame1.setGeometry(QtCore.QRect(300, 250, 711, 261))
        self.frame1.setAutoFillBackground(False)
        self.frame1.setFrameShape(QtGui.QFrame.Box)
        self.frame1.setFrameShadow(QtGui.QFrame.Raised)
        self.frame1.setLineWidth(2)
        self.frame1.setMidLineWidth(1)
        self.frame1.setObjectName(_fromUtf8("frame1"))
        self.USERNAMELBL = QtGui.QLabel(self.frame1)
        self.USERNAMELBL.setGeometry(QtCore.QRect(10, 20, 241, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Felix Titling"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.USERNAMELBL.setFont(font)
        self.USERNAMELBL.setStyleSheet(_fromUtf8("color: rgb(0, 0, 127);"))
        self.USERNAMELBL.setAlignment(QtCore.Qt.AlignCenter)
        self.USERNAMELBL.setObjectName(_fromUtf8("USERNAMELBL"))
        self.PASSWDLBL = QtGui.QLabel(self.frame1)
        self.PASSWDLBL.setGeometry(QtCore.QRect(10, 80, 251, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Felix Titling"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.PASSWDLBL.setFont(font)
        self.PASSWDLBL.setStyleSheet(_fromUtf8("color: rgb(0, 0, 127);"))
        self.PASSWDLBL.setAlignment(QtCore.Qt.AlignCenter)
        self.PASSWDLBL.setObjectName(_fromUtf8("PASSWDLBL"))
        self.CATEGORYcomboBox = QtGui.QComboBox(self.frame1)
        self.CATEGORYcomboBox.setGeometry(QtCore.QRect(302, 150, 231, 31))
        self.CATEGORYcomboBox.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.CATEGORYcomboBox.setObjectName(_fromUtf8("CATEGORYcomboBox"))
        self.CATEGORYcomboBox.addItem(_fromUtf8(""))
        self.CATEGORYcomboBox.addItem(_fromUtf8(""))
        self.CATEGORYcomboBox.addItem(_fromUtf8(""))
        self.CATEGORYLBL = QtGui.QLabel(self.frame1)
        self.CATEGORYLBL.setGeometry(QtCore.QRect(0, 150, 261, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Felix Titling"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.CATEGORYLBL.setFont(font)
        self.CATEGORYLBL.setStyleSheet(_fromUtf8("color: rgb(0, 0, 127);"))
        self.CATEGORYLBL.setAlignment(QtCore.Qt.AlignCenter)
        self.CATEGORYLBL.setObjectName(_fromUtf8("CATEGORYLBL"))
        self.USERNAMETXTBX = QtGui.QLineEdit(self.frame1)
        self.USERNAMETXTBX.setGeometry(QtCore.QRect(300, 10, 251, 31))
        self.USERNAMETXTBX.setAutoFillBackground(False)
        self.USERNAMETXTBX.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.USERNAMETXTBX.setObjectName(_fromUtf8("USERNAMETXTBX"))
        self.PASSWDTXTBX = QtGui.QLineEdit(self.frame1)
        ######################################################3
        self.PASSWDTXTBX.setEchoMode(QtGui.QLineEdit.Password)
        self.PASSWDTXTBX.setGeometry(QtCore.QRect(300, 71, 251, 31))
        self.PASSWDTXTBX.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.PASSWDTXTBX.setObjectName(_fromUtf8("PASSWDTXTBX"))
        self.NEWUSERLBL = QtGui.QLabel(self.frame1)
        self.NEWUSERLBL.setGeometry(QtCore.QRect(192, 220, 221, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Felix Titling"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.NEWUSERLBL.setFont(font)
        self.NEWUSERLBL.setStyleSheet(_fromUtf8("color: rgb(0, 0, 127);"))
        self.NEWUSERLBL.setObjectName(_fromUtf8("NEWUSERLBL"))
        self.REGISTERpushButton = QtGui.QPushButton(self.frame1)
        self.REGISTERpushButton.setGeometry(QtCore.QRect(360, 220, 141, 28))
        ######################### Button Event ##############################3
        self.REGISTERpushButton.clicked.connect(self.REGISTERpushButtonCheck)
        #####################################################################
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Felix Titling"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.REGISTERpushButton.setFont(font)
        self.REGISTERpushButton.setStyleSheet(_fromUtf8("color: rgb(170, 0, 0);background-color: rgb(255, 255, 255);"))
        self.REGISTERpushButton.setObjectName(_fromUtf8("REGISTERpushButton"))
        self.PICLBL = QtGui.QLabel(contact_lbl)
        self.PICLBL.setGeometry(QtCore.QRect(20, 70, 231, 261))
        self.PICLBL.setText(_fromUtf8(""))
        self.PICLBL.setPixmap(QtGui.QPixmap(_fromUtf8("download.png")))
        self.PICLBL.setObjectName(_fromUtf8("PICLBL"))
        self.login_btn = QtGui.QPushButton(contact_lbl)
        self.login_btn.setGeometry(QtCore.QRect(380, 567, 151, 61))
        ######################### Button Event ##############################3
        self.login_btn.clicked.connect(self.loginCheck)
        #####################################################################
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Felix Titling"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.login_btn.setFont(font)
        self.login_btn.setStyleSheet(_fromUtf8("color: rgb(170, 0, 0);background-color: rgb(255, 255, 255);"))
        self.login_btn.setObjectName(_fromUtf8("login_btn"))
        self.EXIT_BTN = QtGui.QPushButton(contact_lbl)
        self.EXIT_BTN.setGeometry(QtCore.QRect(550, 570, 151, 61))
  
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Felix Titling"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.EXIT_BTN.setFont(font)
        self.EXIT_BTN.setStyleSheet(_fromUtf8("color: rgb(170, 0, 0);background-color: rgb(255, 255, 255);"))
        self.EXIT_BTN.setObjectName(_fromUtf8("EXIT_BTN"))
        self.EXIT_BTN.clicked.connect(self.EXIT_BTNCheck)
        self.HELP_LBL = QtGui.QLabel(contact_lbl)
        self.HELP_LBL.setGeometry(QtCore.QRect(30, 610, 131, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Felix Titling"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.HELP_LBL.setFont(font)
        self.HELP_LBL.setStyleSheet(_fromUtf8("color: rgb(170, 0, 0);"))
        self.HELP_LBL.setObjectName(_fromUtf8("HELP_LBL"))
        self.HELP_LBL_2 = QtGui.QLabel(contact_lbl)
        self.HELP_LBL_2.setGeometry(QtCore.QRect(20, 660, 1071, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Felix Titling"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.HELP_LBL_2.setFont(font)
        self.HELP_LBL_2.setStyleSheet(_fromUtf8("color: rgb(170, 0, 0);"))
        self.HELP_LBL_2.setObjectName(_fromUtf8("HELP_LBL_2"))

        self.retranslateUi(contact_lbl)
        QtCore.QMetaObject.connectSlotsByName(contact_lbl)

    def retranslateUi(self, contact_lbl):
        contact_lbl.setWindowTitle(_translate("contact_lbl", "Dialog", None))
        self.HEADINGLBL.setAccessibleName(_translate("contact_lbl", "K J SOMAIYA", None))
        self.HEADINGLBL.setAccessibleDescription(_translate("contact_lbl", "HEADING", None))
        self.HEADINGLBL.setText(_translate("contact_lbl", "WELCOME TO K J SOMAIYA COLLEGE OF ENGINEERING", None))
        self.NAMELBL.setAccessibleName(_translate("contact_lbl", "NAME", None))
        self.NAMELBL.setAccessibleDescription(_translate("contact_lbl", "STUDENT RECORD", None))
        self.NAMELBL.setText(_translate("contact_lbl", "STUDENT RECORD ~(LOGIN)", None))
        self.USERNAMELBL.setText(_translate("contact_lbl", "USERNAME", None))
        self.PASSWDLBL.setText(_translate("contact_lbl", "PASSWORD", None))
        self.CATEGORYcomboBox.setItemText(0, _translate("contact_lbl", "PRINCIPAL", None))
        self.CATEGORYcomboBox.setItemText(1, _translate("contact_lbl", "STUDENT", None))
        self.CATEGORYcomboBox.setItemText(2, _translate("contact_lbl", "PROFESSOR", None))
        self.CATEGORYLBL.setText(_translate("contact_lbl", "CATEGORY", None))
        self.NEWUSERLBL.setText(_translate("contact_lbl", "NEW USER ?", None))
        self.REGISTERpushButton.setText(_translate("contact_lbl", "REGISTER", None))
        self.login_btn.setText(_translate("contact_lbl", "LOGIN", None))
        self.EXIT_BTN.setText(_translate("contact_lbl", "EXIT", None))
        self.HELP_LBL.setText(_translate("contact_lbl", "NEED HELP ?", None))
        self.HELP_LBL_2.setText(_translate("contact_lbl", "CONTACT US : 7738478888                                 WRITE US : priyamshah112@gmail.com                          ", None))



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    contact_lbl = QtGui.QDialog()
    ui = Ui_contact_lbl()
    ui.setupUi(contact_lbl)
    contact_lbl.show()
    
    sys.exit(app.exec_())

