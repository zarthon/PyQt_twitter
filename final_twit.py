import sys
import twitter
import traceback
from PyQt4 import QtGui
from threading import Timer
from PyQt4 import QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import urllib2



USER = None
PASSWORD = None
FRIENDS = None
OWN_STATUS = None
API = None
STATUS = None
TIMER_FLAG = 1
Time = None

def Time_Action(QtWit):
    global Time
    Time = Timer(60.0,QtWit.showMessage)
    Time.start()

class Ui_About(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(461, 290)
        self.horizontalLayoutWidget = QtGui.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 461, 241))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(170, 240, 111, 31))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n" "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
	"p, li { white-space: pre-wrap; }\n"
	"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
	"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"./icons/logo.png\" /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
	"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
	"p, li { white-space: pre-wrap; }\n"
	"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
	"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">QtWitter is simple Api for Twitter developed using twitter library for python by DeWitt Clinton</span></p>\n"
	"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">(</span><a href=\"http://code.google.com/p/python-twitter/\"><span style=\" font-size:8pt; text-decoration: underline; color:#0057ae;\">http://code.google.com/p/python-twitter/</span></a><span style=\" font-size:8pt; font-weight:600;\">) </span></p>\n"
	"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">and Qt bindings for Python</span></p>\n"
	"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p>\n"
	"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p>\n"
	"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Version 1.0</span></p>\n"
	"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">(C) Mohit Kothari</span></p>\n"
	"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"http://www.git-hub.com/zarthon/PyQt_Twitter\"><span style=\" text-decoration: underline; color:#0057ae;\">Source Code</span></a></p>\n"
	"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p>\n"
	"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog", "OK", None, QtGui.QApplication.UnicodeUTF8))

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
	    error = QMessageBox.critical(self.Dialog,"Error",s)
	    error.show()
	except urllib2.URLError as eror:
	    error = QMessageBox.critical(self.Dialog,"Error",s)
	    error.show()
	    
	Successful = QMessageBox(1,'Successful','Reply Successfully Posted')
	Successful.show()  
	Successful.exec_()
	
	
class Ui_Settings(object):
	def setupUi(self, Dialog):
		Dialog.setObjectName("Dialog")
		Dialog.setWindowIcon(QtGui.QIcon('icons/web48.png'))
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
		#print Password+'sell'
	
	def showUser(self):
		global USER
		USER = self.lineEdit.text()
		#print User+'sell'


class Ui_Qtwit(object):
	
	def setupUi(self, Dialog):
		Dialog.setObjectName("Dialog")
		Dialog.resize(398, 584)
		self.systemTray = QSystemTrayIcon(QtGui.QIcon('icons/web48.png'),None)
		self.systemTray.setVisible(True)
		Dialog.setWindowIcon(QtGui.QIcon('icons/web48.png'))

		self.verticalLayoutWidget = QtGui.QWidget(Dialog)
		self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 395, 581))
		self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
		self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
		self.verticalLayout_2.setObjectName("verticalLayout_2")
		self.horizontalLayout_2 = QtGui.QHBoxLayout()
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")
		self.toolButton = QtGui.QToolButton(self.verticalLayoutWidget)
		self.toolButton.setToolTip("Set UserName and Password")
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap("icons/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.toolButton.setIcon(icon)
		self.toolButton.setIconSize(QtCore.QSize(48, 48))
		self.toolButton.setObjectName("toolButton")
		self.horizontalLayout_2.addWidget(self.toolButton)
		self.toolButton_2 = QtGui.QToolButton(self.verticalLayoutWidget)
		self.toolButton_2.setToolTip("Post New Status")
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap("icons/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.toolButton_2.setIcon(icon1)
		self.toolButton_2.setIconSize(QtCore.QSize(48, 48))
		self.toolButton_2.setObjectName("toolButton_2")
		self.horizontalLayout_2.addWidget(self.toolButton_2)
		self.toolButton_5 = QtGui.QToolButton(self.verticalLayoutWidget)
		self.toolButton_5.setToolTip("Get Friends Latest Updates")
		icon2 = QtGui.QIcon()
		icon2.addPixmap(QtGui.QPixmap("icons/get_mesg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.toolButton_5.setIcon(icon2)
		self.toolButton_5.setIconSize(QtCore.QSize(48, 48))
		self.toolButton_5.setObjectName("toolButton_5")
		self.horizontalLayout_2.addWidget(self.toolButton_5)
		spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
		self.horizontalLayout_2.addItem(spacerItem)
		self.toolButton_3 = QtGui.QToolButton(self.verticalLayoutWidget)
		self.toolButton_3.setToolTip("Quit")
		icon3 = QtGui.QIcon()
		icon3.addPixmap(QtGui.QPixmap("icons/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.toolButton_3.setIcon(icon3)
		self.toolButton_3.setIconSize(QtCore.QSize(48, 48))
		self.toolButton_3.setObjectName("toolButton_3")
		self.horizontalLayout_2.addWidget(self.toolButton_3)
		self.toolButton_4 = QtGui.QToolButton(self.verticalLayoutWidget)
		self.toolButton_4.setToolTip("About")
		icon4 = QtGui.QIcon()
		icon4.addPixmap(QtGui.QPixmap("icons/about.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.toolButton_4.setIcon(icon4)
		self.toolButton_4.setIconSize(QtCore.QSize(48, 48))
		self.toolButton_4.setObjectName("toolButton_4")
		self.horizontalLayout_2.addWidget(self.toolButton_4)
		self.verticalLayout_2.addLayout(self.horizontalLayout_2)
		self.horizontalLayout = QtGui.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.verticalLayout = QtGui.QVBoxLayout()
		self.verticalLayout.setObjectName("verticalLayout")
		self.pushButton_5 = QtGui.QPushButton(self.verticalLayoutWidget)
		self.pushButton_5.setObjectName("pushButton_5")
		self.verticalLayout.addWidget(self.pushButton_5)
		self.pushButton_3 = QtGui.QPushButton(self.verticalLayoutWidget)
		self.pushButton_3.setObjectName("pushButton_3")
		self.verticalLayout.addWidget(self.pushButton_3)
		self.pushButton_2 = QtGui.QPushButton(self.verticalLayoutWidget)
		self.pushButton_2.setIconSize(QtCore.QSize(12, 12))
		self.pushButton_2.setObjectName("pushButton_2")
		self.verticalLayout.addWidget(self.pushButton_2)
		self.pushButton_4 = QtGui.QPushButton(self.verticalLayoutWidget)
		self.pushButton_4.setObjectName("pushButton_4")
		self.verticalLayout.addWidget(self.pushButton_4)
		spacerItem1 = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
		self.verticalLayout.addItem(spacerItem1)
		self.horizontalLayout.addLayout(self.verticalLayout)
		self.listWidget = QtGui.QListWidget(self.verticalLayoutWidget)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
		self.listWidget.setSizePolicy(sizePolicy)
		self.listWidget.setWordWrap(True)
		self.listWidget.setObjectName("listWidget")
		self.listWidget.setContextMenuPolicy(Qt.CustomContextMenu)
		
		self.horizontalLayout.addWidget(self.listWidget)
		self.verticalLayout_2.addLayout(self.horizontalLayout)
		
		
		self.systemTrayMenu = QMenu()
		self.postnew = self.systemTrayMenu.addAction(QtGui.QIcon('./icons/new.png'),'New Post')
		self.quitAction = self.systemTrayMenu.addAction(QtGui.QIcon('./icons/close.png'),"Quit")
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
		#QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL("clicked()"), self.destroyStatus)
		QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL("clicked()"), self.Reply)
		QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL("clicked()"), self.showReplies)
		
		#QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL("clicked()"), self.showDirectMessage)
		QtCore.QObject.connect(self.systemTray,QtCore.SIGNAL("activated(QSystemTrayIcon::ActivationReason)"),self.__icon_triggerd)
		QtCore.QMetaObject.connectSlotsByName(Dialog)
		self.Dialog = Dialog
		exit=QtGui.QAction(Dialog)
		exit.setShortcut('Ctrl+Q')
		Dialog.addAction(exit)
		Dialog.connect(exit,QtCore.SIGNAL('triggered()'),QtGui.qApp, QtCore.SLOT('quit()'))#self.CloseEvent)
		
		#Authenticate when opened first time
		self.showSettings()
		
	
	def __icon_triggerd(self,reason):
	    print 'dasdasdas'
	    print reason
	    if reason == 3:
		self.Dialog.setVisible(not self.Dialog.isVisible())
	    
	def CloseEvent(self):
	    print type(self)
	    if self.Dialog.isVisible() == True:
		msg = QMessageBox.question(self.Dialog,"SysTray","The program will keep running in the "
				    "system tray. To terminate the program, "
				    "choose <b>Quit</b> in the context menu "
				    "of the system tray entry.",QtGui.QMessageBox.Ok)
		self.Dialog.hide()

                
	    

	def retranslateUi(self, Dialog):
		Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "QtWitter", None, QtGui.QApplication.UnicodeUTF8))
		self.toolButton.setText(QtGui.QApplication.translate("Dialog", "...", None, QtGui.QApplication.UnicodeUTF8))
		self.toolButton_2.setText(QtGui.QApplication.translate("Dialog", "...", None, QtGui.QApplication.UnicodeUTF8))
		self.toolButton_3.setText(QtGui.QApplication.translate("Dialog", "...", None, QtGui.QApplication.UnicodeUTF8))
		self.toolButton_4.setText(QtGui.QApplication.translate("Dialog", "...", None, QtGui.QApplication.UnicodeUTF8))
		self.pushButton_5.setText(QtGui.QApplication.translate("Dialog", "Destroy Status", None, QtGui.QApplication.UnicodeUTF8))
		self.pushButton_3.setText(QtGui.QApplication.translate("Dialog", "Reply", None, QtGui.QApplication.UnicodeUTF8))
		self.pushButton_2.setText(QtGui.QApplication.translate("Dialog", "GetReplies", None, QtGui.QApplication.UnicodeUTF8))
		self.pushButton_4.setText(QtGui.QApplication.translate("Dialog", "Direct Message", None, QtGui.QApplication.UnicodeUTF8))
	
	def showAbout(self):
		dialog = QtGui.QDialog()
		about = Ui_About()
		about.setupUi(dialog)
		dialog.show()
		dialog.exec_()
		
	
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
			Time_Action(self)
		    except twitter.TwitterError as eror:
			error = QErrorMessage()
			error.showMessage(eror.message)
		    except urllib2.HTTPError as eror:
			error = QMessageBox.critical(self.Dialog,"Error",s)
			error.show()
		    except urllib2.URLError as eror:
			error = QMessageBox.critical(self.Dialog,"Error",s)
			error.show()
			
		    Successful = QMessageBox(1,'Successful','New Status Successfully Posted')
		    Successful.show()  
		    Successful.exec_()
		    
	    elif toSpecific is not None and toSpecific[0] == '@':
		print toSpecific
		
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
			Time_Action(self)
		    except twitter.TwitterError as eror:
			error = QErrorMessage()
			error.showMessage(eror.message)
		    except urllib2.HTTPError as eror:
			error = QMessageBox.critical(self.Dialog,"Error",s)
			error.show()
		    except urllib2.URLError as eror:
			error = QMessageBox.critical(self.Dialog,"Error",s)
			error.show()
			
		    Successful = QMessageBox(1,'Successful','New Status Successfully Posted')
		    Successful.show()
		    Successful.exec_()
		    
	    elif toSpecific != None and toSpecific[:2] == 'RT':
		try:
		    status = str(toSpecific)
		    API.PostUpdates(status)
		    Time_Action(self)
		except twitter.TwitterError as eror:
		    error = QErrorMessage()
		    error.showMessage(eror.message)
		except urllib2.HTTPError as eror:
			error = QErrorMessage()
			error.showMessage(QString(str(eror)))
		except urllib2.URLError as eror:
			error = QErrorMessage()
			error.showMessage(QString(str(eror)))
			
		Successful = QMessageBox(1,'Successful','New Status Successfully Posted')
		Successful.show()  
		Successful.exec_()
		
	def showSettings(self):
		Dialog = QDialog(None)
		ui = Ui_Settings()
		ui.setupUi(Dialog)
		Dialog.show()
		Dialog.exec_()
		self.authenticate()
		
	def authenticate(self):
		global FRIENDS
		global OWN_STATUS
		global API
		
		API = twitter.Api(username=USER,password = PASSWORD)
		
		try:
		    FRIENDS = API.GetFriends()
		except twitter.TwitterError as eror:
		    error = QErrorMessage()
		    error.showMessage(eror.message)
		except urllib2.HTTPError as eror:
		    error = QErrorMessage()
		    error.showMessage(QString(str(eror)))
		    error.exec_()
		except urllib2.URLError as eror:
		    error = QErrorMessage()
		    error.showMessage(QString(str(eror)))
		    error.exec_()
	
	    
	def showMessage(self):
	    global API
	    global USER
	    global STATUS
	    
	    try:
		print 'showMessage Called'
		self.listWidget.clear()
		user = API.GetUser(USER)
		screen = user.GetScreenName()
		STATUS = API.GetFriendsTimeline() 
		for s in STATUS:
		    friend = s.GetUser()
		    a = QtCore.QString()
		    a = friend.GetScreenName()
		    self.listWidget.addItem(a)
		    a = s.GetText()
		    self.listWidget.addItem(a)
		    self.listWidget.addItem('\n')
	    except twitter.TwitterError as a:
		eror=QErrorMessage()
		eror.showMessage(a.message)
		eror.exec_()
	    except urllib2.HTTPError as eror:
		error = QMessageBox.critical(self.Dialog,"Error",s)
		error.show()
	    except urllib2.URLError as eror:
		error = QMessageBox.critical(self.Dialog,"Error",s)
		error.show()
		
		
#def destroyStatus(self):

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
      
	def showRetweet(self,msgItem,nameItem):
	    msg = msgItem.text()
	    name = nameItem.text()
	    new_msg = 'RT @'+name+' '+ msg
	    self.postNew(new_msg)

	def addFavorite(self,row):
	    global API
	    index = (row-1)/3
	    status = STATUS[index]
	    API.CreateFavorite(status)
	    
	    
#    #def showDirectMessage(self):
      
	def showReplies(self):
	    global REPLIES
	    global API
	    
	    
	    try:
		REPLIES = API.GetReplies()
		self.listWidget.clear()
		for s in REPLIES:
		    friend = s.GetUser()
		    a = QtCore.QString()
		    a = friend.GetScreenName()
		    self.listWidget.addItem(a)
		    a = s.GetText()
		    self.listWidget.addItem(a)
		    self.listWidget.addItem('\n')
	    except twitter.TwitterError as a:
		eror=QErrorMessage()
		eror.showMessage(a.message)
		eror.exec_()
	    except urllib2.HTTPError as eror:
		error = QMessageBox.critical(self.Dialog,"Error",s)
		error.show()
	    except urllib2.URLError as eror:
		error = QMessageBox.critical(self.Dialog,"Error",s)
		error.show()
	    
	def openContextMenu(self):
	    global STATUS
	    global API
	    
	    cursor = QCursor()
	    menu = QtGui.QMenu()
	    flag = self.listWidget.currentRow()
	    
	    if flag%3 == 0:
		retweet = menu.addAction(QtGui.QIcon("./icons/retweet.png"),"ReTweet")
		reply = menu.addAction(QtGui.QIcon("./icons/reply.png"), "Reply")
		whoIs = menu.addAction(QtGui.QIcon("./icons/whois.png"), "Who Is?")
		quitAction = menu.addAction(QtGui.QIcon('./icons/close.png'),"Quit")
	    
		#favorite.setIcon(QtGui.QIcon('icons/web64.png'))
		friend_item = self.listWidget.currentItem()
		
		if friend_item.text() == 'zarthon':
		    delete = menu.addAction(QtGui.QIcon("./icons/delete.png"),"Delete")
		    
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
		    
		if action == delete:
		    
		    dialog = QtGui.QDialog()
		    reply = QtGui.QMessageBox.warning(dialog, 'Message',"Are you sure You want to DELETE? There is no UNDOING", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

		    if reply == QtGui.QMessageBox.Yes:
			row = self.listWidget.currentRow()
			index = row/3
			self.listWidget.takeItem(row)
			self.listWidget.takeItem(row)
			self.listWidget.takeItem(row)
			print type(STATUS)
			try:
			    id_del = STATUS[index].GetId()
			    API.DestroyStatus(id_del)
			    del STATUS[index]
			    time = Timer(30.0,self.showMessage)
			    time.start()
			except twitter.TwitterError as eror:
			    error = QErrorMessage()
			    error.showMessage(eror.message)
			except urllib2.HTTPError as eror:
			    error = QMessageBox.critical(self.Dialog,"Error",s)
			    error.show()
			except urllib2.URLError as eror:
			    error = QMessageBox.critical(self.Dialog,"Error",s)
			    error.show()
			    
			Successful = QMessageBox(1,'Successful','Status Destroyed')
			Successful.show()  
			Successful.exec_()
		    
		"""if action == whoIs:
		    item = self.listWidget.currentItem()
		    self.showWhoIs(item.text())"""
		    
	    if (flag-1)%3 == 0:
		retweet = menu.addAction(QtGui.QIcon("./icons/retweet.png"),"ReTweet")
		reply = menu.addAction(QtGui.QIcon("./icons/reply.png"),"Reply")
		favorite = menu.addAction(QtGui.QIcon("./icons/favorite.png"),"Favorite")
		quitAction = menu.addAction(QtGui.QIcon('./icons/close.png'),"Quit")
	    
		action = menu.exec_(cursor.pos())
	    
		if action == retweet:
		    msgIndex = self.listWidget.currentRow()
		    self.showRetweet(self.listWidget.item(msgIndex),self.listWidget.currentItem())
		if action == quitAction:
		    qApp.quit()
		if action == favorite:
		    self.addFavorite(self.listWidget.currentRow())
		if action == reply:
		    row = self.listWidget.currentRow()
		    friend_item = self.listWidget.item(row-1)
		    self.showReply('@'+friend_item.text())
		

app = QtGui.QApplication(sys.argv)
asd = QDialog()
ui = Ui_Qtwit()
ui.setupUi(asd)
asd.show()
app.setQuitOnLastWindowClosed(False)
sys.exit(app.exec_() )
