import sys
from PyQt4 import QtGui,QtCore
 
class min_close_evt(object):
    def __init__(self,parent=None):
        QtGui.QTabWidget.__init__(self,parent)
        self.resize(626, 511)
 
        self.tab = QtGui.QWidget()
        self.addTab(self.tab,QtGui.QIcon("icons/apple-green.png"),"Tab")
 
        exit=QtGui.QAction(self)
        exit.setShortcut('Ctrl+Q')
	self.addAction(exit)
        self.connect(exit,QtCore.SIGNAL('triggered()'),QtCore.SLOT('close()'))
 
    def closeEvent(self,event):
        reply=QtGui.QMessageBox.question(self,'Message',"Are you sure to quit?",QtGui.QMessageBox.Yes,QtGui.QMessageBox.No)
        if reply==QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
 
app=QtGui.QApplication(sys.argv)
ob=min_close_evt()
ob.show()
app.exec_()