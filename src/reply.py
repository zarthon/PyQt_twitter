#################################################################################################
#Added Functionality Dialog to send Reply to multiple users
#There are two options to show Either ScreenNames or RealNames
#There is search filter to filter out unwanted names
#
#CONSTRAINT: The edit feature is only singleLine i.e QLineEdit
#################################################################################################

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

from settings import *
import config


class Ui_Reply(object):
    def setupUi(self, Dialog):
	
        Dialog.setObjectName("Dialog")
        Dialog.resize(253, 377)
        Dialog.setSizeIncrement(QtCore.QSize(0, 48))
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 251, 371))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_2 = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(209, 52))
        self.lineEdit_2.setBaseSize(QtCore.QSize(0, 48))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.comboBox = QtGui.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.listWidget = QtGui.QListWidget(self.verticalLayoutWidget)
        self.listWidget.setObjectName("listWidget")
        
        self.verticalLayout.addWidget(self.listWidget)
        
	
        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.comboBox, QtCore.SIGNAL("currentIndexChanged(int)"), self.comboFilter)
        QtCore.QObject.connect(self.lineEdit, QtCore.SIGNAL("textChanged(QString)"), self.searchFilter)
        QtCore.QObject.connect(self.listWidget, QtCore.SIGNAL("itemDoubleClicked(QListWidgetItem*)"), self.addToLine)
        QtCore.QObject.connect(self.lineEdit_2, QtCore.SIGNAL("returnPressed()"), self.postReply)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.comboFilter()

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Reply", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("Dialog", "Screen Names", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("Dialog", "Real Names", None, QtGui.QApplication.UnicodeUTF8))
       
    def addToLine(self):
	
	
	if self.comboBox.currentIndex() == 0:
	    name = self.listWidget.currentItem()
	    name_str = name.text()
	    self.lineEdit_2.home(False)
	    self.lineEdit_2.insert(name_str+' ')
	    self.lineEdit_2.end(False)
	    
	else:
	    friend = config.FRIENDS[self.listWidget.currentRow()]
	    name_str = '@'+friend.screen_name+' '
	    self.lineEdit_2.home(False)
	    self.lineEdit_2.insert(name_str+' ')
	    self.lineEdit_2.end(False)
	    
    def comboFilter(self):
	
	
	index = self.comboBox.currentIndex()
	if index == 0:
	    self.listWidget.clear()
	    for f in config.FRIENDS:
		self.listWidget.addItem('@'+f.screen_name)
	if index == 1:
	    self.listWidget.clear()
	    for f in config.FRIENDS:
		self.listWidget.addItem(f.name)
	
    def searchFilter(self):
	
	
	match_string = self.lineEdit.text()
	match_list = self.listWidget.findItems(match_string,Qt.MatchContains)
	temp = len(match_list)
	ra = self.listWidget.count()
	for i in range(0,ra):
	    if self.listWidget.item(i) not in match_list:
		temp = self.listWidget.item(i)
		temp.setHidden(True)
	    else:
		temp = self.listWidget.item(i)
		temp.setHidden(False)
	

    def postReply(self):
	
	post_string = self.lineEdit_2.displayText()
	#print post_string
	
	if post_string.size() > 140:
	    post_string = post_string[:140]
	try:
	    config.API.PostUpdate(post_string)
	    self.lineEdit_2.clear()
	except twitter.TwitterError as eror:
	    error = QErrorMessage()
	    error.showMessage(eror.message)
	except urllib2.HTTPError as eror:
	    error = QMessageBox(3,"Error",str(eror))
	    error.show()
	    error.exec_()
	except urllib2.URLError as eror:
	    error = QMessageBox(3,"Error",str(eror))
	    error.show()
	    error.exec_()
	else:
	    Successful = QMessageBox(1,'Successful','Reply Successfully Posted')
	    Successful.show()  
	    Successful.exec_()