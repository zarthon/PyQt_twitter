#!/usr/bin/python
#
#Welcome to ZWITTER
#Name has nothing to do with either HERMAPHRODITE nor RAMMSTEIN
#This is a simple GUI for Twitter API developed mainly for my learning of Qt and Python i.e
#PyQt4 using twitter library for python. 
#
#It does not have the OAuth, it will be added afterwards and takes time to start as it 
#obtains data from Net, depending on the speed depends on starting time.
#
#The dialogs are designed using QtDesigner and Converted to python code using pyuic4
#

author = """
NAME: Mohit Kothari(Zarthon)
Profile: http://www.facebook.com/zarthon#!/zarthon?v=info
Blog: http://zarthon.wordpress.wordpress.com
"""
###Importation of Modules

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

###Global Varialbles

USER = None
PASSWORD = None
FRIENDS = None
OWN_STATUS = None
API = None
STATUS = None
MESSAGE_FLAG = 0
PUBLIC_FLAG =0
PUBLIC_MESAGE = 0
Time = None
REPLIES = None
MESSAGES = None

###################################################
#Class to show and send Direct Messages
##################################################

class Ui_Direct(object):
    def setupUi(self, Dialog,screenName):
	global API
	global FRIENDS
	
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
        
        length = len(FRIENDS)
        screen = []
        for i in range(0,length):
	    self.comboBox.addItem(str(FRIENDS[i].GetScreenName()))
	    screen.append(str(FRIENDS[i].GetScreenName()))
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
	    print text
	    print user
	    API.PostDirectMessage(user,text)
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
		
#################################################################################################
#Added Functionality Dialog to send Reply to multiple users
#There are two options to show Either ScreenNames or RealNames
#There is search filter to filter out unwanted names
#
#CONSTRAINT: The edit feature is only singleLine i.e QLineEdit
#################################################################################################

class Ui_Reply(object):
    def setupUi(self, Dialog):
	global FRIENDS
	
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
	global FRIENDS
	
	if self.comboBox.currentIndex() == 0:
	    name = self.listWidget.currentItem()
	    name_str = name.text()
	    self.lineEdit_2.home(False)
	    self.lineEdit_2.insert(name_str+' ')
	    self.lineEdit_2.end(False)
	    
	else:
	    friend = FRIENDS[self.listWidget.currentRow()]
	    name_str = '@'+friend.screen_name+' '
	    self.lineEdit_2.home(False)
	    self.lineEdit_2.insert(name_str+' ')
	    self.lineEdit_2.end(False)
	    
    def comboFilter(self):
	global FRIENDS
	
	index = self.comboBox.currentIndex()
	if index == 0:
	    self.listWidget.clear()
	    for f in FRIENDS:
		self.listWidget.addItem('@'+f.screen_name)
	if index == 1:
	    self.listWidget.clear()
	    for f in FRIENDS:
		self.listWidget.addItem(f.name)
	
    def searchFilter(self):
	global FRIENDS
	
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
	global API
	
	post_string = self.lineEdit_2.displayText()
	print post_string
	
	if post_string.size() > 140:
	    post_string = post_string[:140]
	try:
	    API.PostUpdate(post_string)
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


###############################################
#
#Basic Login Dialog..ENter USerName and Password
#
#############################################
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
		global PASSWORD
		PASSWORD = self.lineEdit_2.text()
	
	def showUser(self):
		global USER
		USER = self.lineEdit.text()
		

################################################
#
#Main Dialog of the Application
#CONSTRAINT: When twitter status are small then the profile image is showed after the name 
#To Quit the app press 'Ctrl+Q'
################################################

class Ui_Zwit(object):
    
	def setupUi(self, Dialog):
		Dialog.setObjectName("Dialog")
		Dialog.resize(430, 584)
		self.systemTray = QSystemTrayIcon(QtGui.QIcon('../icons/web48.png'),None)
		self.systemTray.setVisible(True)
		Dialog.setWindowIcon(QtGui.QIcon('../icons/web48.png'))
		
		self.verticalLayout_3 = QtGui.QVBoxLayout(Dialog)
		self.verticalLayout_3.setObjectName("verticalLayout_3")
		
		self.verticalLayout_2 = QtGui.QVBoxLayout()
	        self.verticalLayout_2.setSpacing(-1)
		self.verticalLayout_2.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
		self.verticalLayout_2.setObjectName("verticalLayout_2")
		
		self.horizontalLayout_2 = QtGui.QHBoxLayout()
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")
		self.toolButton = QtGui.QToolButton(Dialog)
		self.toolButton.setToolTip("Set UserName and Password")
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap("../icons/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.toolButton.setIcon(icon)
		self.toolButton.setIconSize(QtCore.QSize(48, 48))
		self.toolButton.setObjectName("toolButton")
		self.horizontalLayout_2.addWidget(self.toolButton)
		self.toolButton_2 = QtGui.QToolButton(Dialog)
		self.toolButton_2.setToolTip("Post New Status")
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap("../icons/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.toolButton_2.setIcon(icon1)
		self.toolButton_2.setIconSize(QtCore.QSize(48, 48))
		self.toolButton_2.setObjectName("toolButton_2")
		self.horizontalLayout_2.addWidget(self.toolButton_2)
		self.toolButton_5 = QtGui.QToolButton(Dialog)
		self.toolButton_5.setToolTip("Get Friends Latest Updates")
		icon2 = QtGui.QIcon()
		icon2.addPixmap(QtGui.QPixmap("../icons/get_mesg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.toolButton_5.setIcon(icon2)
		self.toolButton_5.setIconSize(QtCore.QSize(48, 48))
		self.toolButton_5.setObjectName("toolButton_5")
		self.horizontalLayout_2.addWidget(self.toolButton_5)
		spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
		self.horizontalLayout_2.addItem(spacerItem)
		self.toolButton_3 = QtGui.QToolButton(Dialog)
		self.toolButton_3.setToolTip("Quit")
		icon3 = QtGui.QIcon()
		icon3.addPixmap(QtGui.QPixmap("../icons/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.toolButton_3.setIcon(icon3)
		self.toolButton_3.setIconSize(QtCore.QSize(48, 48))
		self.toolButton_3.setObjectName("toolButton_3")
		self.horizontalLayout_2.addWidget(self.toolButton_3)
		self.toolButton_4 = QtGui.QToolButton(Dialog)
		self.toolButton_4.setToolTip("About")
		icon4 = QtGui.QIcon()
		icon4.addPixmap(QtGui.QPixmap("../icons/about.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.toolButton_4.setIcon(icon4)
		self.toolButton_4.setIconSize(QtCore.QSize(48, 48))
		self.toolButton_4.setObjectName("toolButton_4")
		self.horizontalLayout_2.addWidget(self.toolButton_4)
		self.verticalLayout_2.addLayout(self.horizontalLayout_2)
		self.horizontalLayout = QtGui.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.verticalLayout = QtGui.QVBoxLayout()
		self.verticalLayout.setObjectName("verticalLayout")
		self.pushButton_5 = QtGui.QPushButton(Dialog)
		self.pushButton_5.setObjectName("pushButton_5")
		self.verticalLayout.addWidget(self.pushButton_5)
		self.pushButton_3 = QtGui.QPushButton(Dialog)
		self.pushButton_3.setObjectName("pushButton_3")
		self.verticalLayout.addWidget(self.pushButton_3)
		self.pushButton_2 = QtGui.QPushButton(Dialog)
		self.pushButton_2.setIconSize(QtCore.QSize(12, 12))
		self.pushButton_2.setObjectName("pushButton_2")
		self.verticalLayout.addWidget(self.pushButton_2)
		self.pushButton_4 = QtGui.QPushButton(Dialog)
		self.pushButton_4.setObjectName("pushButton_4")
		self.verticalLayout.addWidget(self.pushButton_4)
		spacerItem1 = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
		self.verticalLayout.addItem(spacerItem1)
		self.horizontalLayout.addLayout(self.verticalLayout)
		self.listWidget = QtGui.QListWidget(Dialog)
		
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		
		self.listWidget.setSizePolicy(sizePolicy)
		self.listWidget.setWordWrap(True)
		self.listWidget.setObjectName("listWidget")
		self.listWidget.setContextMenuPolicy(Qt.CustomContextMenu)
		self.listWidget.setWrapping(True)
		self.listWidget.setViewMode(0)
		self.listWidget.setFlow(QtGui.QListView.LeftToRight)
		
		self.horizontalLayout.addWidget(self.listWidget)
		self.verticalLayout_2.addLayout(self.horizontalLayout)
		self.verticalLayout_3.addLayout(self.verticalLayout_2)
		
		self.systemTrayMenu = QMenu()
		self.postnew = self.systemTrayMenu.addAction(QtGui.QIcon('../icons/new.png'),'New Post')
		self.quitAction = self.systemTrayMenu.addAction(QtGui.QIcon('../icons/close.png'),"Quit")
		self.postnew.triggered.connect(self.New)
		self.quitAction.triggered.connect(quit)
		self.systemTray.setContextMenu(self.systemTrayMenu)
		
		self.retranslateUi(Dialog)
		
		self.listWidget.customContextMenuRequested.connect(self.openContextMenu)
		QtCore.QObject.connect(self.toolButton_3, QtCore.SIGNAL("clicked()"), QtGui.qApp, QtCore.SLOT('quit()'))
		QtCore.QObject.connect(self.toolButton_4, QtCore.SIGNAL("clicked()"), self.showAbout)
		QtCore.QObject.connect(self.toolButton_5,QtCore.SIGNAL("clicked()"),self.showMessage)
		QtCore.QObject.connect(self.toolButton_2, QtCore.SIGNAL("clicked()"), self.New)
		QtCore.QObject.connect(self.toolButton, QtCore.SIGNAL("clicked()"), self.showSettings)
		QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL("clicked()"), self.publicStatus)
		QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL("clicked()"), self.Reply)
		QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL("clicked()"), self.showReplies)
		
		QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL("clicked()"), self.showDirectMessage)
		QtCore.QObject.connect(self.systemTray,QtCore.SIGNAL("activated(QSystemTrayIcon::ActivationReason)"),self.icon_triggerd)
		QtCore.QMetaObject.connectSlotsByName(Dialog)
		
		#Setting Shortcut for Quiting application
		self.Dialog = Dialog
		exit=QtGui.QAction(Dialog)
		exit.setShortcut('Ctrl+Q')
		Dialog.addAction(exit)
		Dialog.connect(exit,QtCore.SIGNAL('triggered()'),QtGui.qApp, QtCore.SLOT('quit()'))
		
		#Authenticate when opened first time
		self.showSettings()
		
	def icon_triggerd(self,reason):
	    #print 'dasdasdas'
	    #print reason
	    if reason == 3:
		self.Dialog.setVisible(not self.Dialog.isVisible())           

	def retranslateUi(self, Dialog):
		Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Zwitter", None, QtGui.QApplication.UnicodeUTF8))
		self.toolButton.setText(QtGui.QApplication.translate("Dialog", "...", None, QtGui.QApplication.UnicodeUTF8))
		self.toolButton_2.setText(QtGui.QApplication.translate("Dialog", "...", None, QtGui.QApplication.UnicodeUTF8))
		self.toolButton_3.setText(QtGui.QApplication.translate("Dialog", "...", None, QtGui.QApplication.UnicodeUTF8))
		self.toolButton_4.setText(QtGui.QApplication.translate("Dialog", "...", None, QtGui.QApplication.UnicodeUTF8))
		self.pushButton_5.setText(QtGui.QApplication.translate("Dialog", "Get Public Status", None, QtGui.QApplication.UnicodeUTF8))
		self.pushButton_3.setText(QtGui.QApplication.translate("Dialog", "Reply", None, QtGui.QApplication.UnicodeUTF8))
		self.pushButton_2.setText(QtGui.QApplication.translate("Dialog", "Get Replies", None, QtGui.QApplication.UnicodeUTF8))
		self.pushButton_4.setText(QtGui.QApplication.translate("Dialog", "Direct Message", None, QtGui.QApplication.UnicodeUTF8))
		
##########################	
#Show Dialog about the application
##########################

	def showAbout(self):
		dialog = QtGui.QDialog()
		about = Ui_About()
		about.setupUi(dialog)
		dialog.show()
		dialog.exec_()
		
#########################
#Post New Status
#########################

	def New(self):
	    self.postNew(None)

	def postNew(self,toSpecific):
		
	    global API
	    status = None
	    
	    if toSpecific == None:
		text,ok = QtGui.QInputDialog.getText(None, 'Input Dialog', 'New Status')
		
		if ok:
		    temp = QString(str(text))
		    status = str(text)
		    if temp.size() > 140:
			temp = temp.remove(140,9999999)
			status = str(temp)
			print temp
			
		    try:
			print status
			API.PostUpdates(status)
			
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
			Successful = QMessageBox(1,'Successful','New Status Successfully Posted')
			Successful.show()  
			Successful.exec_()
		    
	    elif toSpecific is not None and toSpecific[0] == '@':
		#print toSpecific
		text,ok = QtGui.QInputDialog.getText(None, 'Input Dialog', 'New Status')
		
		if ok:
		    temp = QString(str(text))
		    status = str(text)
		    if temp.size() > 140:
			temp = temp.remove(140,9999999)
			status = str(temp)
			print temp
			
		    try:
			status = str(toSpecific) + ' ' + status
			print status
			API.PostUpdates(status)
			
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
			Successful = QMessageBox(1,'Successful','New Status Successfully Posted')
			Successful.show()
			Successful.exec_()
		    
	    elif toSpecific != None and toSpecific[:2] == 'RT':
		try:
		    status = str(toSpecific)
		    API.PostUpdates(status)
		    
		except twitter.TwitterError as eror:
		    error = QErrorMessage()
		    error.showMessage(eror.message)
		except urllib2.HTTPError as eror:
			error = QErrorMessage()
			error.showMessage(QString(str(eror)))
		except urllib2.URLError as eror:
			error = QErrorMessage()
			error.showMessage(QString(str(eror)))
		else:
		    Successful = QMessageBox(1,'Successful','New Status Successfully Posted')
		    Successful.show()  
		    Successful.exec_()
		    
########################
#Show Settings Dialog
########################

	def showSettings(self):
		Dialog = QDialog(None)
		ui = Ui_Settings()
		ui.setupUi(Dialog)
		Dialog.show()
		Dialog.exec_()
		self.authenticate()
		
############################################################################
#Authenticate User and obtain Friends list and Replies to Authenticated user
############################################################################

	def authenticate(self):
		global FRIENDS
		global OWN_STATUS
		global API
		global REPLIES
		
		try:
		   # busy = QMessageBox(1,"Busy","Please Wait..API downloading your DATA",QMessageBox.NoButton)
		   # busy.show()
		    API = twitter.Api(username=USER,password = PASSWORD)
		    REPLIES = API.GetReplies()
		    FRIENDS = API.GetFriends()
		   # busy.hide()
		except twitter.TwitterError as eror:
		    error = QErrorMessage()
		    error.showMessage(eror.message)
		except urllib2.HTTPError as eror:
		    error = QMessageBox(3,"Error",str(s))
		    error.show()
		    error.exec_()
		except urllib2.URLError as eror:
		    error = QMessageBox(3,"Error",str(s))
		    error.show()
		    error.exec_()
		
#####################################################
#Show Statuses on the Zwitter ListWidget
#####################################################

	def showMessage(self):
	    global API
	    global USER
	    global STATUS
	    global MESSAGE_FLAG
	    global PUBLIC_FLAG
	    
	    MESSAGE_FLAG = 0
	    PUBLIC_FLAG = 0
	    
	    try:
		#print 'showMessage Called'
		self.listWidget.clear()
		#busy = QMessageBox(1,"Busy","Please Wait..API downloading your DATA")
		#busy.show()
		
		STATUS = API.GetFriendsTimeline() 
		#busy.hide()
		i = 0
		temp = len(STATUS)
		
		for i in range(0,temp):
		    
		    s = STATUS[i]
		    friend = s.GetUser()
		    
		    icon_url = friend.GetProfileImageUrl()
		    #print icon_url
		    icon_name = icon_url.rsplit('/',1)
		    filena = "../profile_images/"+icon_name[1]
		    url = urllib.URLopener()
		    if not os.path.isfile("../profile_images/"+icon_name[1]):
			name = icon_name[1].rsplit('.',1)
			print name[1]
			if name[1] == 'gif':
			    icon_name[1] = name[0]+'.png'
			url.retrieve(icon_url,icon_name[1])
			shutil.move(icon_name[1],"../profile_images/"+icon_name[1])
		        
		    #print friend.GetScreenName()
		    name = QListWidgetItem(QIcon(QString("../profile_images/"+icon_name[1])),s.GetText())
		    size = QSize(48,48)
		    self.listWidget.setIconSize(size)
		    
		    a = friend.GetScreenName()
		    self.listWidget.addItem(a)
		    self.listWidget.addItem(name)
		    
		    if s.GetFavorited() == True:
			self.listWidget.addItem('F@\/()r!TeD-------------------------------------------------------------------------------------------------------------------------------------------------------\n')
		    else:
			self.listWidget.addItem('------------------------------------------------------------------------------------------------------------------------------------------------------------------\n')
		    
		    
	    except twitter.TwitterError as a:
		eror=QErrorMessage()
		eror.showMessage(a.message)
		eror.exec_()
	    except urllib2.HTTPError as eror:
		error = QMessageBox(3,"Error",str(eror))
		error.show()
		error.exec_()
	    except urllib2.URLError as eror:
		error = QMessageBox(3,"Error",str(eror))
		error.show()
		error.exec_()

##############################################################
#Get Current Twitter Public Statuses
#WARNING: THIS can hold a good block size on Hard Disk as profile images are loaded and stored on your computer
##############################################################

	def publicStatus(self):
	    global PUBLIC_MESAGE
	    global API
	    global MESSAGE_FLAG
	    global PUBLIC_FLAG
	    
	    PUBLIC_FLAG =1
	    MESSAGE_FLAG = 0
	    
	    try:
		
		PUBLIC_MESAGE = API.GetPublicTimeline()
		self.listWidget.clear()
		for s in PUBLIC_MESAGE:
		    
		    friend = s.GetUser()
		    a = QtCore.QString()
		    a = friend.GetScreenName()
		    self.listWidget.addItem(a)
		   
		    icon_url = friend.GetProfileImageUrl()
		    #print icon_url
		    icon_name = icon_url.rsplit('/',1)
		    filena = "../profile_images/"+icon_name[1]
		    url = urllib.URLopener()
		    if not os.path.isfile("../profile_images/"+icon_name[1]):
			name = icon_name[1].rsplit('.',1)
			print name[1]
			if name[1] == 'gif':
			    icon_name[1] = name[0]+'.png'
			url.retrieve(icon_url,icon_name[1])
			shutil.move(icon_name[1],"../profile_images/"+icon_name[1])
			
		    size = QSize(48,48)
		    self.listWidget.setIconSize(size)
		    #print friend.GetScreenName()
		    name = QListWidgetItem(QIcon(QString("../profile_images/"+icon_name[1])),s.GetText())
		    
		    self.listWidget.addItem(name)
		    self.listWidget.addItem('-------------------------------------------------------------------------------------------------------------------------------------------------------\n')
	    except twitter.TwitterError as a:
		eror=QErrorMessage()
		eror.showMessage(a.message)
		eror.exec_()
	    except urllib2.HTTPError as eror:
		error = QMessageBox(3,"Error",str(eror))
		error.show()
		error.exec_()
	    except urllib2.URLError as eror:
		error = QMessageBox(3,"Error",str(eror))
		error.show()
		error.exec_()
		
#######################################
#Show Reply Dialog for multiple replies
#######################################

	def Reply(self):
	    self.showReply(None)
	    
	def showReply(self,toSpecific):
	    if toSpecific == None:
		Dialog = QDialog()
		ui = Ui_Reply()
		ui.setupUi(Dialog)
		Dialog.show()
		Dialog.exec_()
		time = Timer(30.0,self.showMessage(),self)
		time.start()
	    else:
		self.postNew(toSpecific)
		
####################################
#Retweet the message through PostNew
####################################

	def showRetweet(self,msgItem,nameItem):
	    msg = msgItem.text()
	    name = nameItem.text()
	    new_msg = 'RT @'+name+' '+ msg
	    self.postNew(new_msg)
	    
#########################################
#Show Direct Messages through showMessage
#########################################

	def showDirectMessage(self):
	    global MESSAGES
	    global API
	    global MESSAGE_FLAG
	    global PUBLIC_FLAG
	    
	    MESSAGES = API.GetDirectMessages()
	    self.listWidget.clear()
	    for m in MESSAGES:
		MESSAGE_FLAG = 1
		PUBLIC_FLAG =0
		sender_id = m.GetSenderId()
		sender_user = API.GetUser(sender_id)
		
		a = sender_user.GetScreenName()
		self.listWidget.addItem(a)

		icon_url = sender_user.GetProfileImageUrl()
		print icon_url
		icon_name = icon_url.rsplit('/',1)
		print "../profile_images/"+icon_name[1]
		filena = "../profile_images/"+icon_name[1]
		url = urllib.URLopener()
		print os.path.isfile(filena)
		if os.path.isfile(filena) == False:
		    name = icon_name[1].rsplit('.',1)
		    print name[1]
		    if name[1] == 'gif':
			icon_name[1] = name[0]+'.png'
		    url.retrieve(icon_url,icon_name[1])
		    shutil.move(icon_name[1],"../profile_images/"+icon_name[1])
			
		size = QSize(48,48)
		self.listWidget.setIconSize(size)
		    #print friend.GetScreenName()
		name = QListWidgetItem(QIcon(QString("../profile_images/"+icon_name[1])),m.GetText())
		    
		self.listWidget.addItem(name)
		self.listWidget.addItem('-------------------------------------------------------------------------------------------------------------------------------------------------------\n')
		
#######################################################
#Show Replies to authenticated user through showMessage
#######################################################

	def showReplies(self):
	    global REPLIES
	    global API
	    global MESSAGE_FLAG
	    global PUBLIC_FLAG
	    
	    try:
		MESSAGE_FLAG = 0
		PUBLIC_FLAG = 0
		
		self.listWidget.clear()
		for s in REPLIES:
		    
		    friend = s.GetUser()
		    a = QtCore.QString()
		    a = friend.GetScreenName()
		    self.listWidget.addItem(a)
		    
		    icon_url = friend.GetProfileImageUrl()
		    #print icon_url
		    icon_name = icon_url.rsplit('/',1)
		    url = urllib.URLopener()
		    if not os.path.isfile("../profile_images/"+icon_name[1]):
			url.retrieve(icon_url,icon_name[1])
			shutil.move(icon_name[1],"../profile_images/"+icon_name[1])
			
		    size = QSize(48,48)
		    self.listWidget.setIconSize(size)
		    #print friend.GetScreenName()
		    name = QListWidgetItem(QIcon(QString("../profile_images/"+icon_name[1])),s.GetText())
		    
		    self.listWidget.addItem(name)
		    self.listWidget.addItem('-------------------------------------------------------------------------------------------------------------------------------------------------------\n')
		    
	    except twitter.TwitterError as a:
		eror=QErrorMessage()
		eror.showMessage(a.message)
		eror.exec_()
	    except urllib2.HTTPError as eror:
		error = QMessageBox(3,"Error",str(eror))
		error.show()
		error.exec_()
	    except urllib2.URLError as eror:
		error = QMessageBox(3,"Error",str(eror))
		error.show()
		error.exec_()

######################################################################
#
#Developing Contextmenu of listwidget depending of the contents showed
#MAJOR function of my application
#
######################################################################

	def openContextMenu(self):
	    global STATUS
	    global API
	    global MESSAGES
	    global MESSAGE_FLAG
	    global PUBLIC_FLAG
	    global PUBLIC_MESAGE
	    
	    cursor = QCursor()
	    menu = QtGui.QMenu()
	    flag = self.listWidget.currentRow()
	    print flag
	    print PUBLIC_FLAG
	    print MESSAGE_FLAG
	    if MESSAGE_FLAG == 0 or PUBLIC_FLAG ==1:
		if (flag)%3 == 0:
		    retweet = menu.addAction(QtGui.QIcon("../icons/retweet.png"),"ReTweet")
		    reply = menu.addAction(QtGui.QIcon("../icons/reply.png"), "Reply")
		    whoIs = menu.addAction(QtGui.QIcon("../icons/whois.png"), "Who Is?")
		    sep_action = QAction(None)
		    sep_action.setSeparator(True)
		    sep = menu.addAction(sep_action)
		    
		    friend_item = self.listWidget.currentItem()
		    
		    if friend_item.text() == 'zarthon':
			delete = menu.addAction(QtGui.QIcon("../icons/delete.png"),"Delete")
		    if PUBLIC_FLAG == 1:
			friendship = menu.addAction(QtGui.QIcon("../icons/befriends.png"),"Be Friend")
			
		    if MESSAGE_FLAG ==0 and PUBLIC_FLAG ==0 and friend_item.text() != 'zarthon':
			des_friendship = menu.addAction(QtGui.QIcon("../icons/befriends.png"),"Destroy Friendship")
			
		    quitAction = menu.addAction(QtGui.QIcon('../icons/close.png'),"Quit")    
		    action = menu.exec_(cursor.pos())
		
		    if action == retweet:
			nameIndex = self.listWidget.currentRow()
			self.showRetweet(self.listWidget.item(nameIndex+1),self.listWidget.currentItem())
			
		    if action == quitAction:
			qApp.quit()
			
		    if action == reply:
			friend_item = self.listWidget.currentItem()
			header = '@'+friend_item.text()
			self.showReply(header)
			
		    if PUBLIC_FLAG == 1 and action == friendship:
			new_friend = self.listWidget.currentItem()
			try:
			    API.CreateFriendship(new_friend.text())
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
			    Successful = QMessageBox(1,'Successful','New Friend Added')
			    Successful.show()  
			    Successful.exec_()
			    
		    if MESSAGE_FLAG ==0 and PUBLIC_FLAG ==0 and friend_item.text() != 'zarthon' and action==des_friendship:
			del_friend = self.listWidget.currentItem()
			try:
			    API.DestroyFriendship(del_friend.text())
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
			    Successful = QMessageBox(1,'Successful','Friend Deleted')
			    Successful.show()  
			    Successful.exec_()
			    
		    if friend_item.text() == 'zarthon' and action == delete :
			
			dialog = QtGui.QDialog()
			reply = QtGui.QMessageBox.warning(dialog, 'Message',"Are you sure You want to DELETE? There is no UNDOING", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
			
			if reply == QtGui.QMessageBox.Yes:
			    row = self.listWidget.currentRow()
			    index = (row)/3
			    
			    print type(STATUS)
			    try:
				id_del = STATUS[index].GetId()
				print id_del
				API.DestroyStatus(id_del)
				self.listWidget.takeItem(row)
				self.listWidget.takeItem(row)
				self.listWidget.takeItem(row)
				print len(STATUS)
				del STATUS[index]
				print len(STATUS)
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
				Successful = QMessageBox(1,'Successful','Status Destroyed')
				Successful.show()  
				Successful.exec_()
			
		    if action == whoIs:
			row = self.listWidget.currentRow()
			index = row/3
			if PUBLIC_FLAG ==0:
			    item = STATUS[index].GetUser()
			else:
			    item = PUBLIC_MESAGE[index].GetUser()
			item_id = item.GetId()
			user = API.GetUser(item_id)
			print user.GetStatus()
			self.showWhoIs(user)
			
		if (flag-1)%3 == 0:
		    retweet = menu.addAction(QtGui.QIcon("../icons/retweet.png"),"ReTweet")
		    reply = menu.addAction(QtGui.QIcon("../icons/reply.png"),"Reply")
		    
		    fav_index = (flag-1)/3
		    fav_status = STATUS[fav_index]
		    print fav_status.GetText()
		    print fav_status
		    if fav_status.GetFavorited() == False:
			favorite = menu.addAction(QtGui.QIcon("../icons/favorite.png"),"Favorite")
		    else:
			favorite = menu.addAction(QtGui.QIcon("../icons/favorite.png"),"Destroy Favorite")
			
		    sep_action = QAction(None)
		    sep_action.setSeparator(True)
		    sep = menu.addAction(sep_action)
		    quitAction = menu.addAction(QtGui.QIcon('../icons/close.png'),"Quit")
		    action = menu.exec_(cursor.pos())
		
		    if action == retweet:
			msgIndex = self.listWidget.currentRow()
			self.showRetweet(self.listWidget.item(msgIndex),self.listWidget.currentItem())
		    if action == quitAction:
			qApp.quit()
			
		    if action == favorite:
			if fav_status.GetFavorited() == False:
			    try:
				API.CreateFavorite(fav_status)
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
				Successful = QMessageBox(1,'Successful','Status Favorited')
				Successful.show()  
				Successful.exec_()
			else:
			    try:
				API.DestroyFavorite(fav_status)
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
				Successful = QMessageBox(1,'Successful','Status Unfavorited')
				Successful.show()  
				Successful.exec_()
			    
			    
		    if action == reply:
			row = self.listWidget.currentRow()
			friend_item = self.listWidget.item(row-1)
			self.showReply('@'+friend_item.text())
			
	    elif MESSAGE_FLAG ==1 and PUBLIC_FLAG ==0:
		cursor = QCursor()
		menu = QtGui.QMenu()
		flag = self.listWidget.currentRow()
		print flag
		if flag%3==0 or (flag-1)%3 == 0:
		    reply = menu.addAction(QtGui.QIcon("../icons/reply.png"),"Reply")
		    delete = menu.addAction(QtGui.QIcon("../icons/delete.png"),"Delete")
		    
		    sep_action = QAction(None)
		    sep_action.setSeparator(True)
		    sep = menu.addAction(sep_action)
		    quitAction = menu.addAction(QtGui.QIcon('../icons/close.png'),"Quit")
		    action = menu.exec_(cursor.pos())
		    
		    if action == quitAction:
			qApp.quit()
		    if action == reply:
			if flag%3 ==0:
			    friend_item = self.listWidget.currentItem()
			else:
			    row = self.listWidget.currentRow()
			    friend_item = self.listWidget.item(row-1)
			Dialog = QDialog()
			direct = Ui_Direct()
			direct.setupUi(Dialog,friend_item.text())
			Dialog.show()
			Dialog.exec_()
		    if action == delete:
			if flag%3 ==0:
			    index = self.listWidget.currentRow() +1
			    message = MESSAGES[index/3]
			    id_del = message.GetId()
			else:
			    index = self.listWidget.currentRow()
			    message = MESSAGES[(index-1)/3]
			    id_del = message.GetId()
			    
			dialog = QtGui.QDialog()
			reply = QtGui.QMessageBox.warning(dialog, 'Message',"Are you sure You want to DELETE? There is no UNDOING", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

			if reply == QtGui.QMessageBox.Yes:
			    try:
				print id_del
				row = self.listWidget.currentRow()
				API.DestroyDirectMessage(id_del)
				self.listWidget.takeItem(row)
				self.listWidget.takeItem(row)
				self.listWidget.takeItem(row)
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
				Successful = QMessageBox(1,'Successful','Message Destroyed')
				Successful.show()  
				Successful.exec_()
			    
			    
######################################
#Showing basic Information of the user
#####################################
	def showWhoIs(self,user):
	    Dialog = QDialog()
	    whois = Ui_whoIs()
	    whois.setupUi(Dialog,user)
	    Dialog.show()
	    Dialog.exec_()

def main():
    
    app = QtGui.QApplication(sys.argv)
    asd = QDialog()
    ui = Ui_Zwit()
    ui.setupUi(asd)
    asd.show()
    app.setQuitOnLastWindowClosed(False)
    sys.exit(app.exec_() )
    
if __name__=='__main__':
    main()