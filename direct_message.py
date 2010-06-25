# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DirectMessage.ui'
#
# Created: Fri Jun 25 22:44:08 2010
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Direct(object):
    def setupUi(self, Dialog,screenName):
        Dialog.setObjectName("Dialog")
        Dialog.resize(328, 277)
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
        
        length = len(FRIENDS)
        screen = []
        for i in range(0,length):
	    self.comboBox.addItem(str(FRIENDS[i].GetScreenName()))
	    screen.append(str(FRIENDS[i].GetScreenName()))
	    
	index = screen.find(screenName)
	self.comboBox.setCurrentIndex(index)
	self.Api = API
        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.newDirect)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("Dialog", "test", None, QtGui.QApplication.UnicodeUTF8))
        
    def newDirect(self):
	text = self.plainTextEdit.toPlainText()
	if text.size()>140:
	    text = text.remove(140,99999999)
	    msg = QMessageBox(1,"Large Text","Only Following Message will be Posted: \n"+text)
	    text = str(text)
	    try:
		API.PostUpdates(status)
		Time_Action(self)
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
