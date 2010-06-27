###############################################
#
#Basic Login Dialog..ENter USerName and Password
#
#############################################


import sys
import twitter
import traceback
from PyQt4 import QtGui
from threading import Timer
import thread, threading
from PyQt4 import QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import urllib2, urllib
import os.path
import shutil
from whois import *
from about import *
from direct import *
from reply import *

import config



class Ui_Settings(object):
	def setupUi(self, Dialog):
		Dialog.setObjectName("Dialog")
		Dialog.setWindowIcon(QtGui.QIcon('../icons/web48.png'))
		Dialog.resize(212, 104)
		self.buttonBox = QtGui.QDialogButtonBox(Dialog)
		self.buttonBox.setGeometry(QtCore.QRect(0, 70, 191, 20))
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName("buttonBox")
		self.label_2 = QtGui.QLabel(Dialog)
		self.label_2.setGeometry(QtCore.QRect(0, 40, 71, 16))
		self.label_2.setObjectName("label_2")
		self.label = QtGui.QLabel(Dialog)
		self.label.setGeometry(QtCore.QRect(0, 0, 81, 31))
		self.label.setObjectName("label")
		self.lineEdit = QtGui.QLineEdit(Dialog)
		self.lineEdit.setGeometry(QtCore.QRect(70, 0, 113, 25))
		self.lineEdit.setObjectName("lineEdit")
		self.lineEdit_2 = QtGui.QLineEdit(Dialog)
		self.lineEdit_2.setGeometry(QtCore.QRect(70, 30, 113, 25))
		self.lineEdit_2.setEchoMode(QtGui.QLineEdit.Password)
		self.lineEdit_2.setObjectName("lineEdit_2")
	
		self.retranslateUi(Dialog)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
		QtCore.QObject.connect(self.lineEdit, QtCore.SIGNAL("editingFinished()"), self.showUser)
		QtCore.QObject.connect(self.lineEdit_2, QtCore.SIGNAL("editingFinished()"), self.showPass)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

	def retranslateUi(self, Dialog):
		Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Settings", None, QtGui.QApplication.UnicodeUTF8))
		self.label_2.setText(QtGui.QApplication.translate("Dialog", "Password", None, QtGui.QApplication.UnicodeUTF8))
		self.label.setText(QtGui.QApplication.translate("Dialog", "UserName", None, QtGui.QApplication.UnicodeUTF8))

	def showPass(self):
		
		config.PASSWORD = self.lineEdit_2.text()
	
	def showUser(self):
		
		config.USER = self.lineEdit.text()