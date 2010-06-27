###################################################
#Class to show and send Direct Messages
##################################################

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

from reply import *
from settings import *
import config



class Ui_Direct(object):
    def setupUi(self, Dialog,screenName):
	
	
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(328, 277)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtGui.QComboBox(Dialog)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.plainTextEdit = QtGui.QPlainTextEdit(Dialog)
        self.plainTextEdit.setMaximumBlockCount(140)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.Dialog = Dialog
        
	###################################################################
        #Adding Friends to ComboBox and setting currentIndex to arg Passed
        ###################################################################
        
        length = len(config.FRIENDS)
        screen = []
        for i in range(0,length):
	    self.comboBox.addItem(str(config.FRIENDS[i].GetScreenName()))
	    screen.append(str(config.FRIENDS[i].GetScreenName()))
	index = screen.index(screenName)
	
	self.comboBox.setCurrentIndex(index)
        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.newDirect)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "To:", None, QtGui.QApplication.UnicodeUTF8))
        
    #######################
    #Posting Direct Message
    #######################
        
    def newDirect(self):
	global API
	
	print 'NewDirect Reached'
	text = self.plainTextEdit.toPlainText()
	
	if text.size()>140:
	    text = text.remove(140,99999999)
	    msg = QMessageBox(1,"Large Text","Only Following Message will be Posted: \n"+text)
	    text = str(text)
	   
	try:
	    user = str(self.comboBox.currentText())
	    #print text
	    #print user
	    config.API.PostDirectMessage(user,text)
	except twitter.TwitterError as eror:
	    error = QErrorMessage()
	    error.showMessage(eror.message)
	except urllib2.HTTPError as eror:
	    error = QMessageBox(3,"Error",str(eror))
	    error.show()
	    error.exec_()
	except urllib2.URLError as eror:
	    error = QMessageBox(3,"Error",str(s))
	    error.show()
	    error.exec_()
	else:
	    Successful = QMessageBox(1,'Successful','New Message Sent')
	    Successful.show()
	    Successful.exec_()
	    self.Dialog.hide()