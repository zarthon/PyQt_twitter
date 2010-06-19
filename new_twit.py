#!/usr/bin/python

# inputdialog.py

import sys
import twitter
import traceback
from PyQt4 import QtGui
import time
from settings import *

from PyQt4 import QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import config

class InputDialog(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.hbox = QtGui.QHBoxLayout(self)
        
        self.user = None
        self.password = None
        
        self.settings = QtGui.QAction(QtGui.QIcon('icons/settings.png'),'Settings',self)
        
        self.toolbar = QToolBar('Settings')
        self.toolbar.addAction(self.settings)
        
        self.button = QtGui.QPushButton('Username', self)
	self.button2 = QtGui.QPushButton('Password',self)
	self.button3 = QtGui.QPushButton('Get Message',self)
	
	self.splitter = QtGui.QSplitter(QtCore.Qt.Horizontal)
	self.splitter2 = QtGui.QSplitter(QtCore.Qt.Vertical)
	self.splitter3 = QtGui.QSplitter(QtCore.Qt.Vertical)
        
        self.button.move(20, 20)
	self.button2.move(20,40)        
	self.button3.move(20,60)
	
	self.splitter2.addWidget(self.button)
	self.splitter2.addWidget(self.button2)
	self.splitter2.addWidget(self.button3)
	self.splitter3.addWidget(self.toolbar)
	
	self.listw = QtGui.QListWidget()
	self.listw.setGeometry(QtCore.QRect(160,160,300,300))
	self.listw.setFlow(1)
	self.splitter3.addWidget(self.splitter)
	self.splitter.addWidget(self.splitter2)
	self.splitter.addWidget(self.listw)
	
        self.connect(self.button, QtCore.SIGNAL('clicked()'), self.showDialog)
	self.connect(self.button2,QtCore.SIGNAL('clicked()'), self.showDialog2)
	self.connect(self.button3,QtCore.SIGNAL('clicked()'),self.showMessage)
	
        self.connect(self.settings,QtCore.SIGNAL('triggered()'),self.showDialog11)
	
	self.hbox.addWidget(self.splitter3)
	self.setLayout(self.hbox)
	self.setGeometry(500, 500, 550, 500)
        self.setWindowTitle('My Twitter API')
        self.setWindowIcon(QtGui.QIcon('icons/web48.png'))    
        
    def showDialog11(self):
        Dialog = QDialog(None)
        
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()
        
    def showDialog(self):
        text,ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 'Username')
        
        if ok:
	    config.user = str(text)
	    
    def showDialog2(self):
	#here 2 is for password mode
	text,ok = QtGui.QInputDialog.getText(self,'Input Dialog','Password',2)
	
	if ok:
	    config.password = str(text)

    def showMessage(self):
	print config.user +'main'
	print config.password + 'main'
	try:
	  api = twitter.Api(username=config.user,password = config.password)
	  user = api.GetUser(config.user)
	  screen = user.GetScreenName()
	  status = api.GetFriendsTimeline() 
	except twitter.TwitterError as a:
	  #print m.message
	  eror=QErrorMessage()
	  eror.showMessage(a.message)
	  
	for s in status:
	  friend = s.GetUser()
	  a = QtCore.QString()
	  a = friend.GetScreenName()
	  self.listw.addItem(a)
	  a = s.GetText()+'\n'
	  self.listw.addItem(a)

    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Message',"Are you sure to quit?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
            

app = QtGui.QApplication(sys.argv)
idlg = InputDialog()
idlg.show()
app.exec_()

