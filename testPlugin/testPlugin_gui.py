# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testPlugin.ui'
#
# Created: Sat Jul 05 15:08:31 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(381, 132)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lineInput = QtGui.QLineEdit(Dialog)
        self.lineInput.setObjectName(_fromUtf8("lineInput"))
        self.gridLayout.addWidget(self.lineInput, 4, 0, 1, 1)
        self.browseButton = QtGui.QPushButton(Dialog)
        self.browseButton.setObjectName(_fromUtf8("browseButton"))
        self.gridLayout.addWidget(self.browseButton, 4, 1, 1, 1)
        self.comboInputB = QtGui.QComboBox(Dialog)
        self.comboInputB.setObjectName(_fromUtf8("comboInputB"))
        self.gridLayout.addWidget(self.comboInputB, 3, 0, 1, 1)
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 2, 1, 1, 1)
        self.comboInputA = QtGui.QComboBox(Dialog)
        self.comboInputA.setObjectName(_fromUtf8("comboInputA"))
        self.gridLayout.addWidget(self.comboInputA, 2, 0, 1, 1)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 3, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 5, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.lineEdit, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.label_3.setText)
        QtCore.QObject.connect(self.comboInputA, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), self.label.setNum)
        QtCore.QObject.connect(self.comboInputB, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")), self.label_2.setText)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.comboInputA, self.comboInputB)
        Dialog.setTabOrder(self.comboInputB, self.lineInput)
        Dialog.setTabOrder(self.lineInput, self.browseButton)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.lineInput.setPlaceholderText(_translate("Dialog", "Define directory for output shapefile", None))
        self.browseButton.setText(_translate("Dialog", "Browse...", None))
        self.label.setText(_translate("Dialog", "Input Layer A", None))
        self.label_2.setText(_translate("Dialog", "Input Layer B", None))
        self.label_3.setText(_translate("Dialog", "Input Layer A", None))

