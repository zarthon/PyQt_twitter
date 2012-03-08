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
from direct import *
from reply import *
from settings import *
import config
import qr_icon



############################################################################
#Function to execute Functions while GUI thread display Infinite Progress BAR 
############################################################################

class showBusy(QThread):
    def __init__(self,parent=None):
	QtCore.QThread.__init__(self,parent)
    def run(self):
	
	#print 'thread running'
	print config.Thread_Flag
	if config.Thread_Flag == 0:
	    try:
		config.ERROR = None
		config.API = twitter.Api(username=config.USER,password = config.PASSWORD)
		config.FRIENDS = config.API.GetFriends()
	    except twitter.TwitterError as eror:
		config.ERROR = str(eror.message)
		print config.ERROR
	    except urllib2.HTTPError as eror:
		config.ERROR = str(eror)
		print config.ERROR
	    except urllib2.URLError as eror:
		config.ERROR = str(eror)
		print config.ERROR
		
	    config.Thread_Flag = -1
	if config.Thread_Flag == 1:
	  #  print 'falg 1 reached'
	    try:
		config.ERROR = None
		config.STATUS = config.API.GetFriendsTimeline() 
		    #busy.hide()
		i = 0
		temp = len(config.STATUS)
		    
		for i in range(0,temp):
		
		    s = config.STATUS[i]
		    friend = s.GetUser()
		
		    icon_url = friend.GetProfileImageUrl()
		    #print icon_url
		    icon_name = icon_url.rsplit('/',1)
		    filena = "../profile_images/"+icon_name[1]
		    url = urllib.URLopener()
		    if not os.path.isfile("../profile_images/"+icon_name[1]):
			name = icon_name[1].rsplit('.',1)
			#print name[1]
			if name[1] == 'gif':
			    icon_name[1] = name[0]+'.png'
			url.retrieve(icon_url,icon_name[1])
			shutil.move(icon_name[1],"../profile_images/"+icon_name[1])
	    except twitter.TwitterError as eror:
		config.ERROR = str(eror.message)
	    except urllib2.HTTPError as eror:
		config.ERROR = str(eror)
	    except urllib2.URLError as eror:
		config.ERROR = str(eror)
	    config.Thread_Flag = -1
	    
	if config.Thread_Flag == 2:
	    try:
		config.ERROR = None
		config.PUBLIC_MESAGE = config.API.GetPublicTimeline()
		
		for s in config.PUBLIC_MESAGE:
		    friend = s.GetUser()
		    
		    icon_url = friend.GetProfileImageUrl()
		    #print icon_url
		    icon_name = icon_url.rsplit('/',1)
		    filena = "../profile_images/"+icon_name[1]
		    url = urllib.URLopener()
		    if not os.path.isfile("../profile_images/"+icon_name[1]):
			name = icon_name[1].rsplit('.',1)
			#print name[1]
			if name[1] == 'gif':
			    icon_name[1] = name[0]+'.png'
			url.retrieve(icon_url,icon_name[1])
			shutil.move(icon_name[1],"../profile_images/"+icon_name[1])
	    except twitter.TwitterError as eror:
		config.ERROR = str(eror.message)
	    except urllib2.HTTPError as eror:
		config.ERROR = str(eror)
	    except urllib2.URLError as eror:
		config.ERROR = str(eror)
		
	    config.Threa_Flag =-1
	    
	if config.Thread_Flag == 3:
	    try:
		config.ERROR = None
		config.MESSAGES = config.API.GetDirectMessages()
		for m in config.MESSAGES:
		    sender_id = m.GetSenderId()
		    sender_user = config.API.GetUser(sender_id)

		    icon_url = sender_user.GetProfileImageUrl()
		    #print icon_url
		    icon_name = icon_url.rsplit('/',1)
		    print "../profile_images/"+icon_name[1]
		    filena = "../profile_images/"+icon_name[1]
		    url = urllib.URLopener()
		    print os.path.isfile(filena)
		    if os.path.isfile(filena) == False:
			name = icon_name[1].rsplit('.',1)
			#print name[1]
			if name[1] == 'gif':
			    icon_name[1] = name[0]+'.png'
			url.retrieve(icon_url,icon_name[1])
			shutil.move(icon_name[1],"../profile_images/"+icon_name[1])
	    except twitter.TwitterError as eror:
		config.ERROR = str(eror.message)
	    except urllib2.HTTPError as eror:
		config.ERROR = str(eror)
	    except urllib2.URLError as eror:
		config.ERROR = str(eror)
	    config.Thread_Flag = -1
	    
	if config.Thread_Flag ==4:
	    try:
		config.ERROR = None
		config.REPLIES = config.API.GetReplies()
		for m in config.REPLIES:
		    friend = m.GetUser()
		    
		    icon_url = friend.GetProfileImageUrl()
		    #print icon_url
		    icon_name = icon_url.rsplit('/',1)
		    print "../profile_images/"+icon_name[1]
		    filena = "../profile_images/"+icon_name[1]
		    url = urllib.URLopener()
		    print os.path.isfile(filena)
		    if os.path.isfile(filena) == False:
			name = icon_name[1].rsplit('.',1)
			#print name[1]
			if name[1] == 'gif':
			    icon_name[1] = name[0]+'.png'
			url.retrieve(icon_url,icon_name[1])
			shutil.move(icon_name[1],"../profile_images/"+icon_name[1])
	    except twitter.TwitterError as eror:
		config.ERROR = str(eror.message)
	    except urllib2.HTTPError as eror:
		config.ERROR = str(eror)
	    except urllib2.URLError as eror:
		config.ERROR = str(eror)
	    config.Thread_Flag = -1
	    
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
		self.systemTray = QSystemTrayIcon(QtGui.QIcon(':/icons/web48.png'),None)
		self.systemTray.setVisible(True)
		Dialog.setWindowIcon(QtGui.QIcon(':/icons/web48.png'))
		
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
		icon.addPixmap(QtGui.QPixmap(":/icons/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.toolButton.setIcon(icon)
		self.toolButton.setIconSize(QtCore.QSize(48, 48))
		self.toolButton.setObjectName("toolButton")
		self.horizontalLayout_2.addWidget(self.toolButton)
		self.toolButton_2 = QtGui.QToolButton(Dialog)
		self.toolButton_2.setToolTip("Post New Status")
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap(":/icons/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.toolButton_2.setIcon(icon1)
		self.toolButton_2.setIconSize(QtCore.QSize(48, 48))
		self.toolButton_2.setObjectName("toolButton_2")
		self.horizontalLayout_2.addWidget(self.toolButton_2)
		self.toolButton_5 = QtGui.QToolButton(Dialog)
		self.toolButton_5.setToolTip("Get Friends Latest Updates")
		icon2 = QtGui.QIcon()
		icon2.addPixmap(QtGui.QPixmap(":/icons/get_mesg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.toolButton_5.setIcon(icon2)
		self.toolButton_5.setIconSize(QtCore.QSize(48, 48))
		self.toolButton_5.setObjectName("toolButton_5")
		self.horizontalLayout_2.addWidget(self.toolButton_5)
		spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
		self.horizontalLayout_2.addItem(spacerItem)
		self.toolButton_3 = QtGui.QToolButton(Dialog)
		self.toolButton_3.setToolTip("Quit")
		icon3 = QtGui.QIcon()
		icon3.addPixmap(QtGui.QPixmap(":/icons/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.toolButton_3.setIcon(icon3)
		self.toolButton_3.setIconSize(QtCore.QSize(48, 48))
		self.toolButton_3.setObjectName("toolButton_3")
		self.horizontalLayout_2.addWidget(self.toolButton_3)
		self.toolButton_4 = QtGui.QToolButton(Dialog)
		self.toolButton_4.setToolTip("About")
		icon4 = QtGui.QIcon()
		icon4.addPixmap(QtGui.QPixmap(":/icons/about.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
		
		#Timer for regular updates
		self.timer = QTimer()
		#contextmenu for system tray
		
		self.systemTrayMenu = QMenu()
		self.postnew = self.systemTrayMenu.addAction(QtGui.QIcon(':/icons/new.png'),'New Post')
		self.quitAction = self.systemTrayMenu.addAction(QtGui.QIcon(':/icons/close.png'),"Quit")
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
		QtCore.QObject.connect(self.timer,QtCore.SIGNAL('timeout()'),self.showUpdate)
		
		
		QtCore.QMetaObject.connectSlotsByName(Dialog)
		
		#Setting Shortcut for Quiting application
		self.Dialog = Dialog
		exit=QtGui.QAction(Dialog)
		exit.setShortcut('Ctrl+Q')
		Dialog.addAction(exit)
		Dialog.connect(exit,QtCore.SIGNAL('triggered()'),QtGui.qApp, QtCore.SLOT('quit()'))
		
		
		
		
		#Authenticate when opened first time
		self.showSettings()
		self.timer.start(60000)
		
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
		
###################################
#Update List Widget Every 60 seconds
###################################

	def showUpdate(self):
	    
	    if config.MESSAGE_FLAG == 0 and config.PUBLIC_FLAG==0:
		self.timer.start(60000)
		if config.REPLY_FLAG ==1:
		    self.showReplies()
		else:
		    self.showMessage()
	    if config.MESSAGE_FLAG == 1 and config.PUBLIC_FLAG ==0:
		self.timer.start(60000)
		self.showDirectMessage()
	    if config.MESSAGE_FLAG == 0 and config.PUBLIC_FLAG == 1:
		self.timer.start(60000)
		self.publicStatus()
		
#########################
#Post New Status
#########################

	def New(self):
	    self.postNew(None)

	def postNew(self,toSpecific):
		
	    
	    status = None
	    
	    if toSpecific == None:
		text,ok = QtGui.QInputDialog.getText(None, 'Input Dialog', 'New Status')
		
		if ok:
		    temp = QString(str(text))
		    status = str(text)
		    if temp.size() > 140:
			temp = temp.remove(140,9999999)
			status = str(temp)
			#print temp
			
		    try:
			#print status
			config.API.PostUpdates(status)
			
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
			#print temp
			
		    try:
			status = str(toSpecific) + ' ' + status
			#print status
			config.API.PostUpdates(status)
			
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
		    config.API.PostUpdates(status)
		    
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
		
		try:
		    config.Thread_Flag=0
		    busy = showBusy()
		    busy.start()
		    busyd = QProgressDialog("Please Wait..API downloading your DATA",QString(),0,0)
		    QtCore.QObject.connect(busy,QtCore.SIGNAL("finished()"), busyd,QtCore.SLOT("hide()"))
		    busyd.exec_()
		    
		    if config.ERROR != None:
			error = QMessageBox(3,"Error",str(config.ERROR))
			error.show()
			error.exec_()
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
	    config.MESSAGE_FLAG = 0
	    config.PUBLIC_FLAG = 0
	    config.REPLY_FLAG = 0
	    try:
		#print 'showMessage'
		config.Thread_Flag=1
		busy = showBusy()
		busy.start()
		busyd = QProgressDialog("Please Wait..API downloading your DATA",QString(),0,0)
		QtCore.QObject.connect(busy,QtCore.SIGNAL("finished()"), busyd,QtCore.SLOT("hide()"))
		busyd.exec_()
		
		if config.ERROR != None:
			error = QMessageBox(3,"Error",str(config.ERROR))
			error.show()
			error.exec_()
		else:
		    self.listWidget.clear()
		    i = 0
		    temp = len(config.STATUS)
		    
		    for i in range(0,temp):
			
			s = config.STATUS[i]
			friend = s.GetUser()
			
			icon_url = friend.GetProfileImageUrl()
			#print icon_url
			icon_name = icon_url.rsplit('/',1)
			filena = "../profile_images/"+icon_name[1]
			url = urllib.URLopener()
			if not os.path.isfile("../profile_images/"+icon_name[1]):
			    name = icon_name[1].rsplit('.',1)
			    #print name[1]
			    if name[1] == 'gif':
				icon_name[1] = name[0]+'.png'
			    
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
	    config.PUBLIC_FLAG =1
	    config.MESSAGE_FLAG = 0
	    
	    try:
		
		config.Thread_Flag = 2
		busy = showBusy()
		busy.start()
		busyd = QProgressDialog("Please Wait..API downloading your DATA",QString(),0,0)
		QtCore.QObject.connect(busy,QtCore.SIGNAL("finished()"), busyd,QtCore.SLOT("hide()"))
		busyd.exec_()
		
		if config.ERROR != None:
			error = QMessageBox(3,"Error",str(config.ERROR))
			error.show()
			error.exec_()
		else:
		    self.listWidget.clear()
		    #print type(PUBLIC_MESAGE)
		    for s in config.PUBLIC_MESAGE:
			
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
			    #print name[1]
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
	    config.Thread_Flag = 3
	    busy = showBusy()
	    busy.start()
	    busyd = QProgressDialog("Please Wait..API downloading your DATA",QString(),0,0)
	    QtCore.QObject.connect(busy,QtCore.SIGNAL("finished()"), busyd,QtCore.SLOT("hide()"))
	    busyd.exec_()
	    
	    if config.ERROR != None:
		error = QMessageBox(3,"Error",str(config.ERROR))
		error.show()
		error.exec_()
	    try:
		self.listWidget.clear()
		for m in config.MESSAGES:
		    config.MESSAGE_FLAG = 1
		    config.PUBLIC_FLAG =0
		    sender_id = m.GetSenderId()
		    sender_user = config.API.GetUser(sender_id)
		    
		    a = sender_user.GetScreenName()
		    self.listWidget.addItem(a)

		    icon_url = sender_user.GetProfileImageUrl()
		    #print icon_url
		    icon_name = icon_url.rsplit('/',1)
		    print "../profile_images/"+icon_name[1]
		    filena = "../profile_images/"+icon_name[1]
		    url = urllib.URLopener()
		    print os.path.isfile(filena)
		    if os.path.isfile(filena) == False:
			name = icon_name[1].rsplit('.',1)
			#print name[1]
			if name[1] == 'gif':
			    icon_name[1] = name[0]+'.png'
		    
		    size = QSize(48,48)
		    self.listWidget.setIconSize(size)
			#print friend.GetScreenName()
		    name = QListWidgetItem(QIcon(QString("../profile_images/"+icon_name[1])),m.GetText())
			
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
		
#######################################################
#Show Replies to authenticated user through showMessage
#######################################################

	def showReplies(self):
	    try:
		config.Thread_Flag = 4
		
		busy = showBusy()
		busy.start()
		busyd = QProgressDialog("Please Wait..API downloading your DATA",QString(),0,0)
		QtCore.QObject.connect(busy,QtCore.SIGNAL("finished()"), busyd,QtCore.SLOT("hide()"))
		busyd.exec_()
		if config.ERROR != None:
		    error = QMessageBox(3,"Error",str(config.ERROR))
		    error.show()
		    error.exec_()
		else:
		    config.MESSAGE_FLAG = 0
		    config.PUBLIC_FLAG = 0
		    config.REPLY_FLAG =1
		    self.listWidget.clear()
		    for s in config.REPLIES:
			#print 'reply reached'
			friend = s.GetUser()
			a = QtCore.QString()
			a = friend.GetScreenName()
			self.listWidget.addItem(a)
			
			icon_url = friend.GetProfileImageUrl()
			#print icon_url
			icon_name = icon_url.rsplit('/',1)
			url = urllib.URLopener()
			if not os.path.isfile("../profile_images/"+icon_name[1]):
			    name = icon_name[1].rsplit('.',1)
			    #print name[1]
			    if name[1] == 'gif':
				icon_name[1] = name[0]+'.png'
				
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
	    
	    cursor = QCursor()
	    menu = QtGui.QMenu()
	    flag = self.listWidget.currentRow()
	    print flag
	    print config.PUBLIC_FLAG
	    print config.MESSAGE_FLAG
	    
	    if config.MESSAGE_FLAG == 0 or config.PUBLIC_FLAG ==1:
		if (flag)%3 == 0:
		    retweet = menu.addAction(QtGui.QIcon(":/icons/retweet.png"),"ReTweet")
		    reply = menu.addAction(QtGui.QIcon(":/icons/reply.png"), "Reply")
		    whoIs = menu.addAction(QtGui.QIcon(":/icons/whois.png"), "Who Is?")
		    sep_action = QAction(None)
		    sep_action.setSeparator(True)
		    sep = menu.addAction(sep_action)
		    
		    friend_item = self.listWidget.currentItem()
		    
		    if friend_item.text() == 'zarthon':
			delete = menu.addAction(QtGui.QIcon(":/icons/delete.png"),"Delete")
		    if config.PUBLIC_FLAG == 1:
			friendship = menu.addAction(QtGui.QIcon(":/icons/befriends.png"),"Be Friend")
			
		    if config.MESSAGE_FLAG ==0 and config.PUBLIC_FLAG ==0 and friend_item.text() != 'zarthon':
			des_friendship = menu.addAction(QtGui.QIcon(":/icons/befriends.png"),"Destroy Friendship")
			
		    quitAction = menu.addAction(QtGui.QIcon(':/icons/close.png'),"Quit")    
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
			
		    if config.PUBLIC_FLAG == 1 and action == friendship:
			new_friend = self.listWidget.currentItem()
			try:
			    config.API.CreateFriendship(new_friend.text())
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
			    
		    if config.MESSAGE_FLAG ==0 and config.PUBLIC_FLAG ==0 and friend_item.text() != 'zarthon' and action==des_friendship:
			del_friend = self.listWidget.currentItem()
			try:
			    config.API.DestroyFriendship(del_friend.text())
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
			    
			    print type(config.STATUS)
			    try:
				id_del = config.STATUS[index].GetId()
				print id_del
				config.API.DestroyStatus(id_del)
				self.listWidget.takeItem(row)
				self.listWidget.takeItem(row)
				self.listWidget.takeItem(row)
				#print len(STATUS)
				del config.STATUS[index]
				#print len(STATUS)
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
			if config.PUBLIC_FLAG ==0:
			    item = config.STATUS[index].GetUser()
			else:
			    item = config.PUBLIC_MESAGE[index].GetUser()
			item_id = item.GetId()
			user = config.API.GetUser(item_id)
			#print user.GetStatus()
			self.showWhoIs(user)
			
		if (flag-1)%3 == 0:
		    retweet = menu.addAction(QtGui.QIcon(":/icons/retweet.png"),"ReTweet")
		    reply = menu.addAction(QtGui.QIcon(":/icons/reply.png"),"Reply")
		    
		    fav_index = (flag-1)/3
		    fav_status = config.STATUS[fav_index]
		    #print fav_status.GetText()
		    #print fav_status
		    if fav_status.GetFavorited() == False:
			favorite = menu.addAction(QtGui.QIcon(":/icons/favorite.png"),"Favorite")
		    else:
			favorite = menu.addAction(QtGui.QIcon(":/icons/favorite.png"),"Destroy Favorite")
			
		    sep_action = QAction(None)
		    sep_action.setSeparator(True)
		    sep = menu.addAction(sep_action)
		    quitAction = menu.addAction(QtGui.QIcon(':/icons/close.png'),"Quit")
		    action = menu.exec_(cursor.pos())
		
		    if action == retweet:
			msgIndex = self.listWidget.currentRow()
			self.showRetweet(self.listWidget.item(msgIndex),self.listWidget.currentItem())
		    if action == quitAction:
			qApp.quit()
			
		    if action == favorite:
			if fav_status.GetFavorited() == False:
			    try:
				config.API.CreateFavorite(fav_status)
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
				config.API.DestroyFavorite(fav_status)
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
			
	    elif config.MESSAGE_FLAG ==1 and config.PUBLIC_FLAG ==0:
		cursor = QCursor()
		menu = QtGui.QMenu()
		flag = self.listWidget.currentRow()
		#print flag
		if flag%3==0 or (flag-1)%3 == 0:
		    reply = menu.addAction(QtGui.QIcon(":/icons/reply.png"),"Reply")
		    delete = menu.addAction(QtGui.QIcon(":/icons/delete.png"),"Delete")
		    
		    sep_action = QAction(None)
		    sep_action.setSeparator(True)
		    sep = menu.addAction(sep_action)
		    quitAction = menu.addAction(QtGui.QIcon(':/icons/close.png'),"Quit")
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
			    message = config.MESSAGES[index/3]
			    id_del = message.GetId()
			else:
			    index = self.listWidget.currentRow()
			    message = config.MESSAGES[(index-1)/3]
			    id_del = message.GetId()
			    
			dialog = QtGui.QDialog()
			reply = QtGui.QMessageBox.warning(dialog, 'Message',"Are you sure You want to DELETE? There is no UNDOING", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

			if reply == QtGui.QMessageBox.Yes:
			    try:
				#print id_del
				row = self.listWidget.currentRow()
				config.API.DestroyDirectMessage(id_del)
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
