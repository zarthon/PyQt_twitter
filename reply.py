# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Reply_Window.ui'
#
# Created: Mon Jun 21 12:24:24 2010
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
api = None
friends = None
own_status = None

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
        QtCore.QObject.connect(self.listWidget, QtCore.SIGNAL("itemDoubleClicked(QListWidgetItem*)"), self.lineEdit_2.paste)
        QtCore.QObject.connect(self.lineEdit_2, QtCore.SIGNAL("returnPressed()"), self.postReply)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Reply", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("Dialog", "Screen Names", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("Dialog", "Real Names", None, QtGui.QApplication.UnicodeUTF8))
      
    def comboFilter(self):
	global friends
	index = self.comboBox.currentIndex
	if index == 0:
	    self.listWidget.clear
	    for f in friends:
		self.listWidget.addItem('@'+f.screen_name)
	if index == 1:
	    self.listWidget.clear
	    for f in friends:
		self.listWidget.addItem(f.name)
	
    def searchFilter(self):
	global friends
	match_string = self.lineEdit.displayText
	match_list = self.listWidget.findItems(match_string,1)
	self.listWidget.clear
	for i in range(0,match_list.size+1):
	    self.listWidget.addItem(match_list[i])
	    
	

    def postReply(self):
	global api
	
	post_string = self.lineEdit.displayText()
	if post_string.size > 140:
	    post_string = post_string[:140]
	try:
	    api.PostUpdates(post_string)
	except twitter.TwitterError as eror:
	    error = QErrorMessage()
	    error.showMessage(eror.message)
	    
	Successful = QMessageBox(1,'Successful','Reply Successfully Posted')
	Successful.show()  
	Successful.exec_()

app = QtGui.QApplication(sys.argv)
asd = QtGui.QDialog()
ui = Ui_Dialog()
ui.setupUi(asd)
asd.show()
app.exec_()
