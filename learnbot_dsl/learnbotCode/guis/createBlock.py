# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ivan/robocomp/components/learnbot/learnbot_dsl/learnbotCode/guis/createBlock.ui'
#
# Created: Wed Aug 30 19:10:13 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(613, 549)
        self.verticalLayout_4 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setMinimumSize(QtCore.QSize(102, 27))
        self.label_4.setMaximumSize(QtCore.QSize(102, 27))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_10.addWidget(self.label_4)
        self.lineEditName = QtGui.QLineEdit(Dialog)
        self.lineEditName.setMinimumSize(QtCore.QSize(331, 27))
        self.lineEditName.setMaximumSize(QtCore.QSize(331, 27))
        self.lineEditName.setToolTip("")
        self.lineEditName.setObjectName("lineEditName")
        self.horizontalLayout_10.addWidget(self.lineEditName)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setMinimumSize(QtCore.QSize(102, 27))
        self.label_2.setMaximumSize(QtCore.QSize(102, 27))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.comboBoxBlockImage = QtGui.QComboBox(Dialog)
        self.comboBoxBlockImage.setMaximumSize(QtCore.QSize(110, 27))
        self.comboBoxBlockImage.setToolTip("")
        self.comboBoxBlockImage.setObjectName("comboBoxBlockImage")
        self.horizontalLayout_3.addWidget(self.comboBoxBlockImage)
        self.pushButtonAddBlockImage = QtGui.QPushButton(Dialog)
        self.pushButtonAddBlockImage.setMaximumSize(QtCore.QSize(70, 16777215))
        self.pushButtonAddBlockImage.setAutoDefault(False)
        self.pushButtonAddBlockImage.setObjectName("pushButtonAddBlockImage")
        self.horizontalLayout_3.addWidget(self.pushButtonAddBlockImage)
        self.pushButtonRemoveBlockImage = QtGui.QPushButton(Dialog)
        self.pushButtonRemoveBlockImage.setEnabled(False)
        self.pushButtonRemoveBlockImage.setMaximumSize(QtCore.QSize(70, 16777215))
        self.pushButtonRemoveBlockImage.setAutoDefault(False)
        self.pushButtonRemoveBlockImage.setObjectName("pushButtonRemoveBlockImage")
        self.horizontalLayout_3.addWidget(self.pushButtonRemoveBlockImage)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtGui.QSpacerItem(100, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.listWidgetBlockImage = QtGui.QListWidget(Dialog)
        self.listWidgetBlockImage.setMaximumSize(QtCore.QSize(16777215, 103))
        self.listWidgetBlockImage.setObjectName("listWidgetBlockImage")
        self.horizontalLayout_4.addWidget(self.listWidgetBlockImage)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.BlockImage = QtGui.QLabel(Dialog)
        self.BlockImage.setMinimumSize(QtCore.QSize(161, 111))
        self.BlockImage.setText("")
        self.BlockImage.setObjectName("BlockImage")
        self.horizontalLayout_5.addWidget(self.BlockImage)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setMinimumSize(QtCore.QSize(102, 27))
        self.label_6.setMaximumSize(QtCore.QSize(102, 27))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.comboBoxBlockType = QtGui.QComboBox(Dialog)
        self.comboBoxBlockType.setMaximumSize(QtCore.QSize(110, 27))
        self.comboBoxBlockType.setObjectName("comboBoxBlockType")
        self.comboBoxBlockType.addItem("")
        self.comboBoxBlockType.addItem("")
        self.comboBoxBlockType.addItem("")
        self.comboBoxBlockType.addItem("")
        self.comboBoxBlockType.addItem("")
        self.comboBoxBlockType.addItem("")
        self.horizontalLayout.addWidget(self.comboBoxBlockType)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setMinimumSize(QtCore.QSize(102, 27))
        self.label_3.setMaximumSize(QtCore.QSize(102, 27))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_8.addWidget(self.label_3)
        self.lineEditFile = QtGui.QLineEdit(Dialog)
        self.lineEditFile.setMinimumSize(QtCore.QSize(331, 27))
        self.lineEditFile.setMaximumSize(QtCore.QSize(331, 27))
        self.lineEditFile.setObjectName("lineEditFile")
        self.horizontalLayout_8.addWidget(self.lineEditFile)
        self.pushButtonSelectFile = QtGui.QPushButton(Dialog)
        self.pushButtonSelectFile.setAutoDefault(False)
        self.pushButtonSelectFile.setObjectName("pushButtonSelectFile")
        self.horizontalLayout_8.addWidget(self.pushButtonSelectFile)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setMinimumSize(QtCore.QSize(102, 27))
        self.label_5.setMaximumSize(QtCore.QSize(102, 27))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.pushButtonAddVar = QtGui.QPushButton(Dialog)
        self.pushButtonAddVar.setMaximumSize(QtCore.QSize(70, 16777215))
        self.pushButtonAddVar.setAutoDefault(False)
        self.pushButtonAddVar.setObjectName("pushButtonAddVar")
        self.horizontalLayout_7.addWidget(self.pushButtonAddVar)
        self.pushButtonRemoveVar = QtGui.QPushButton(Dialog)
        self.pushButtonRemoveVar.setEnabled(False)
        self.pushButtonRemoveVar.setMaximumSize(QtCore.QSize(70, 16777215))
        self.pushButtonRemoveVar.setAutoDefault(False)
        self.pushButtonRemoveVar.setObjectName("pushButtonRemoveVar")
        self.horizontalLayout_7.addWidget(self.pushButtonRemoveVar)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.tableWidgetVars = QtGui.QTableWidget(Dialog)
        self.tableWidgetVars.setMinimumSize(QtCore.QSize(301, 0))
        self.tableWidgetVars.setMaximumSize(QtCore.QSize(301, 16777215))
        self.tableWidgetVars.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidgetVars.setAutoScroll(True)
        self.tableWidgetVars.setObjectName("tableWidgetVars")
        self.tableWidgetVars.setColumnCount(3)
        self.tableWidgetVars.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetVars.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetVars.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetVars.setHorizontalHeaderItem(2, item)
        self.tableWidgetVars.horizontalHeader().setVisible(True)
        self.tableWidgetVars.verticalHeader().setVisible(False)
        self.verticalLayout_3.addWidget(self.tableWidgetVars)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_6)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem7)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem8)
        self.pushButtonCancel = QtGui.QPushButton(Dialog)
        self.pushButtonCancel.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButtonCancel.setAutoDefault(False)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.horizontalLayout_9.addWidget(self.pushButtonCancel)
        self.pushButtonOK = QtGui.QPushButton(Dialog)
        self.pushButtonOK.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButtonOK.setObjectName("pushButtonOK")
        self.horizontalLayout_9.addWidget(self.pushButtonOK)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.pushButtonOK, self.lineEditName)
        Dialog.setTabOrder(self.lineEditName, self.comboBoxBlockImage)
        Dialog.setTabOrder(self.comboBoxBlockImage, self.pushButtonAddBlockImage)
        Dialog.setTabOrder(self.pushButtonAddBlockImage, self.pushButtonRemoveBlockImage)
        Dialog.setTabOrder(self.pushButtonRemoveBlockImage, self.listWidgetBlockImage)
        Dialog.setTabOrder(self.listWidgetBlockImage, self.comboBoxBlockType)
        Dialog.setTabOrder(self.comboBoxBlockType, self.lineEditFile)
        Dialog.setTabOrder(self.lineEditFile, self.pushButtonSelectFile)
        Dialog.setTabOrder(self.pushButtonSelectFile, self.pushButtonRemoveVar)
        Dialog.setTabOrder(self.pushButtonRemoveVar, self.tableWidgetVars)
        Dialog.setTabOrder(self.tableWidgetVars, self.pushButtonCancel)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Block name:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditName.setPlaceholderText(QtGui.QApplication.translate("Dialog", "Name Block", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Block image:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAddBlockImage.setText(QtGui.QApplication.translate("Dialog", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonRemoveBlockImage.setText(QtGui.QApplication.translate("Dialog", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "Block type:", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxBlockType.setItemText(0, QtGui.QApplication.translate("Dialog", "CONTROL", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxBlockType.setItemText(1, QtGui.QApplication.translate("Dialog", "MOTOR", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxBlockType.setItemText(2, QtGui.QApplication.translate("Dialog", "PERCEPTIVE", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxBlockType.setItemText(3, QtGui.QApplication.translate("Dialog", "PROPIOPERCEPTIVE", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxBlockType.setItemText(4, QtGui.QApplication.translate("Dialog", "OPERATOR", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxBlockType.setItemText(5, QtGui.QApplication.translate("Dialog", "VARIABLE", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "File:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditFile.setPlaceholderText(QtGui.QApplication.translate("Dialog", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonSelectFile.setText(QtGui.QApplication.translate("Dialog", "Select File", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "Variables:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAddVar.setText(QtGui.QApplication.translate("Dialog", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonRemoveVar.setText(QtGui.QApplication.translate("Dialog", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetVars.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("Dialog", "Type", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetVars.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("Dialog", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetVars.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("Dialog", "Defaul value", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancel.setText(QtGui.QApplication.translate("Dialog", "CANCEL", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonOK.setText(QtGui.QApplication.translate("Dialog", "OK", None, QtGui.QApplication.UnicodeUTF8))

