import sys
import time
from PyQt4 import QtGui
app = QtGui.QApplication(sys.argv)
barra = QtGui.QProgressBar()
barra.show()
barra.setMinimum(0)
barra.setMaximum(10)
for a in range(10):
    time.sleep(1)
    barra.setValue(a)
app.exec_()
