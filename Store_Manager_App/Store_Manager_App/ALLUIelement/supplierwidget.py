# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Supplier2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_supplierW(object):
    def setupUi(self, supplierW):
        supplierW.setObjectName("supplierW")
        supplierW.resize(737, 721)
        self.gridLayout = QtWidgets.QGridLayout(supplierW)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_3 = QtWidgets.QFrame(supplierW)
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.supplier_Table = QtWidgets.QTableWidget(self.frame_3)
        self.supplier_Table.setStyleSheet("QTableWidget{\n"
"\n"
"\n"
"\n"
"background-color: rgb(220,220, 220);\n"
"\n"
"\n"
"font: \"Sitka Heading\";\n"
"padding: 3px;\n"
"border:2px solid #62D5FF;\n"
"border-radius: 10px;\n"
"font: bold 15px;\n"
"\n"
"color: rgb(0, 0, 0);\n"
"font: 15pt\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"QTableWidget:focus{\n"
"\n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"    \n"
"    \n"
"    border:2px solid rgb(255, 167, 72);\n"
"}")
        self.supplier_Table.setObjectName("supplier_Table")
        self.supplier_Table.setColumnCount(0)
        self.supplier_Table.setRowCount(0)
        self.supplier_Table.verticalHeader().setVisible(False)
        self.gridLayout_4.addWidget(self.supplier_Table, 1, 0, 1, 1)
        self.supplier_Search_Bar = QtWidgets.QLineEdit(self.frame_3)
        self.supplier_Search_Bar.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.supplier_Search_Bar.setFont(font)
        self.supplier_Search_Bar.setStyleSheet("QLineEdit{\n"
"\n"
"\n"
"\n"
"background-color: rgb(220,220, 220);\n"
"\n"
"\n"
"font: \"Sitka Heading\";\n"
"padding: 3px;\n"
"border:2px solid #62D5FF;\n"
"border-radius: 10px;\n"
"font: bold 15px;\n"
"\n"
"color: rgb(0, 0, 0);\n"
"font: 15pt\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"QLineEdit:focus{\n"
"\n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"    \n"
"    \n"
"    border:2px solid rgb(255, 167, 72);\n"
"}")
        self.supplier_Search_Bar.setObjectName("supplier_Search_Bar")
        self.gridLayout_4.addWidget(self.supplier_Search_Bar, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.frame_3)
        self.frame.setMaximumSize(QtCore.QSize(250, 16777215))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.supplier_CityLE = QtWidgets.QLineEdit(self.frame)
        self.supplier_CityLE.setMinimumSize(QtCore.QSize(0, 40))
        self.supplier_CityLE.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.supplier_CityLE.setFont(font)
        self.supplier_CityLE.setStyleSheet("QLineEdit{\n"
"\n"
"\n"
"\n"
"background-color: rgb(220,220, 220);\n"
"\n"
"\n"
"font: \"Sitka Heading\";\n"
"padding: 3px;\n"
"border:2px solid #62D5FF;\n"
"border-radius: 10px;\n"
"font: bold 15px;\n"
"\n"
"color: rgb(0, 0, 0);\n"
"font: 15pt\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"QLineEdit:focus{\n"
"\n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"    \n"
"    \n"
"    border:2px solid rgb(255, 167, 72);\n"
"}")
        self.supplier_CityLE.setObjectName("supplier_CityLE")
        self.gridLayout_2.addWidget(self.supplier_CityLE, 4, 1, 1, 1)
        self.supplier_EmailLE = QtWidgets.QLineEdit(self.frame)
        self.supplier_EmailLE.setMinimumSize(QtCore.QSize(0, 40))
        self.supplier_EmailLE.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.supplier_EmailLE.setFont(font)
        self.supplier_EmailLE.setStyleSheet("QLineEdit{\n"
"\n"
"\n"
"\n"
"background-color: rgb(220,220, 220);\n"
"\n"
"\n"
"font: \"Sitka Heading\";\n"
"padding: 3px;\n"
"border:2px solid #62D5FF;\n"
"border-radius: 10px;\n"
"font: bold 15px;\n"
"\n"
"color: rgb(0, 0, 0);\n"
"font: 15pt\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"QLineEdit:focus{\n"
"\n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"    \n"
"    \n"
"    border:2px solid rgb(255, 167, 72);\n"
"}")
        self.supplier_EmailLE.setObjectName("supplier_EmailLE")
        self.gridLayout_2.addWidget(self.supplier_EmailLE, 2, 1, 1, 1)
        self.supplier_PhoneLE = QtWidgets.QLineEdit(self.frame)
        self.supplier_PhoneLE.setMinimumSize(QtCore.QSize(0, 40))
        self.supplier_PhoneLE.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.supplier_PhoneLE.setFont(font)
        self.supplier_PhoneLE.setStyleSheet("QLineEdit{\n"
"\n"
"\n"
"\n"
"background-color: rgb(220,220, 220);\n"
"\n"
"\n"
"font: \"Sitka Heading\";\n"
"padding: 3px;\n"
"border:2px solid #62D5FF;\n"
"border-radius: 10px;\n"
"font: bold 15px;\n"
"\n"
"color: rgb(0, 0, 0);\n"
"font: 15pt\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"QLineEdit:focus{\n"
"\n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"    \n"
"    \n"
"    border:2px solid rgb(255, 167, 72);\n"
"}")
        self.supplier_PhoneLE.setObjectName("supplier_PhoneLE")
        self.gridLayout_2.addWidget(self.supplier_PhoneLE, 1, 1, 1, 1)
        self.supplier_StreetLE = QtWidgets.QLineEdit(self.frame)
        self.supplier_StreetLE.setMinimumSize(QtCore.QSize(0, 40))
        self.supplier_StreetLE.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.supplier_StreetLE.setFont(font)
        self.supplier_StreetLE.setStyleSheet("QLineEdit{\n"
"\n"
"\n"
"\n"
"background-color: rgb(220,220, 220);\n"
"\n"
"\n"
"font: \"Sitka Heading\";\n"
"padding: 3px;\n"
"border:2px solid #62D5FF;\n"
"border-radius: 10px;\n"
"font: bold 15px;\n"
"\n"
"color: rgb(0, 0, 0);\n"
"font: 15pt\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"QLineEdit:focus{\n"
"\n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"    \n"
"    \n"
"    border:2px solid rgb(255, 167, 72);\n"
"}")
        self.supplier_StreetLE.setObjectName("supplier_StreetLE")
        self.gridLayout_2.addWidget(self.supplier_StreetLE, 5, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 9, 1, 1, 1)
        self.supplier_reali = QtWidgets.QLineEdit(self.frame)
        self.supplier_reali.setMinimumSize(QtCore.QSize(0, 40))
        self.supplier_reali.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.supplier_reali.setFont(font)
        self.supplier_reali.setStyleSheet("QLineEdit{\n"
"\n"
"\n"
"\n"
"background-color: rgb(220,220, 220);\n"
"\n"
"\n"
"font: \"Sitka Heading\";\n"
"padding: 3px;\n"
"border:2px solid #62D5FF;\n"
"border-radius: 10px;\n"
"font: bold 15px;\n"
"\n"
"color: rgb(0, 0, 0);\n"
"font: 15pt\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"QLineEdit:focus{\n"
"\n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"    \n"
"    \n"
"    border:2px solid rgb(255, 167, 72);\n"
"}")
        self.supplier_reali.setObjectName("supplier_reali")
        self.gridLayout_2.addWidget(self.supplier_reali, 7, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 19, 1, 1, 1)
        self.supplier_Delete = QtWidgets.QPushButton(self.frame)
        self.supplier_Delete.setMinimumSize(QtCore.QSize(200, 0))
        self.supplier_Delete.setMaximumSize(QtCore.QSize(100, 35))
        self.supplier_Delete.setStyleSheet("QPushButton{\n"
"\n"
"\n"
"background-color: rgba(15, 76, 117, 255);\n"
"font: \"Sitka Heading\";\n"
"padding: 3px;\n"
"border: 2px ;\n"
"border-radius: 10px;\n"
"font: bold 15px;\n"
"\n"
"color: rgb(255, 255, 255);\n"
"font: 15pt\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    background-color:rgba(21, 113, 174,255);\n"
"    border: 2px solid rgba(255, 255, 255, 255)\n"
"\n"
"\n"
"}")
        self.supplier_Delete.setIconSize(QtCore.QSize(32, 32))
        self.supplier_Delete.setObjectName("supplier_Delete")
        self.gridLayout_2.addWidget(self.supplier_Delete, 17, 1, 1, 1)
        self.supplier_FDR = QtWidgets.QLineEdit(self.frame)
        self.supplier_FDR.setMinimumSize(QtCore.QSize(0, 40))
        self.supplier_FDR.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.supplier_FDR.setFont(font)
        self.supplier_FDR.setStyleSheet("QLineEdit{\n"
"\n"
"\n"
"\n"
"background-color: rgb(220,220, 220);\n"
"\n"
"\n"
"font: \"Sitka Heading\";\n"
"padding: 3px;\n"
"border:2px solid #62D5FF;\n"
"border-radius: 10px;\n"
"font: bold 15px;\n"
"\n"
"color: rgb(0, 0, 0);\n"
"font: 15pt\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"QLineEdit:focus{\n"
"\n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"    \n"
"    \n"
"    border:2px solid rgb(255, 167, 72);\n"
"}")
        self.supplier_FDR.setObjectName("supplier_FDR")
        self.gridLayout_2.addWidget(self.supplier_FDR, 6, 1, 1, 1)
        self.supplier_Note = QtWidgets.QLineEdit(self.frame)
        self.supplier_Note.setMinimumSize(QtCore.QSize(0, 40))
        self.supplier_Note.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.supplier_Note.setFont(font)
        self.supplier_Note.setStyleSheet("QLineEdit{\n"
"\n"
"\n"
"\n"
"background-color: rgb(220,220, 220);\n"
"\n"
"\n"
"font: \"Sitka Heading\";\n"
"padding: 3px;\n"
"border:2px solid #62D5FF;\n"
"border-radius: 10px;\n"
"font: bold 15px;\n"
"\n"
"color: rgb(0, 0, 0);\n"
"font: 15pt\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"QLineEdit:focus{\n"
"\n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"    \n"
"    \n"
"    border:2px solid rgb(255, 167, 72);\n"
"}")
        self.supplier_Note.setObjectName("supplier_Note")
        self.gridLayout_2.addWidget(self.supplier_Note, 8, 1, 1, 1)
        self.supplier_Add = QtWidgets.QPushButton(self.frame)
        self.supplier_Add.setMinimumSize(QtCore.QSize(200, 0))
        self.supplier_Add.setMaximumSize(QtCore.QSize(100, 35))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.supplier_Add.setFont(font)
        self.supplier_Add.setStyleSheet("QPushButton{\n"
"\n"
"\n"
"background-color: rgba(15, 76, 117, 255);\n"
"font: \"Sitka Heading\";\n"
"padding: 3px;\n"
"border: 2px ;\n"
"border-radius: 10px;\n"
"font: bold 15px;\n"
"\n"
"color: rgb(255, 255, 255);\n"
"font: 15pt\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    background-color:rgba(21, 113, 174,255);\n"
"    border: 2px solid rgba(255, 255, 255, 255)\n"
"\n"
"\n"
"}")
        self.supplier_Add.setIconSize(QtCore.QSize(32, 32))
        self.supplier_Add.setAutoRepeatDelay(200)
        self.supplier_Add.setObjectName("supplier_Add")
        self.gridLayout_2.addWidget(self.supplier_Add, 10, 1, 1, 1)
        self.supplier_NameLE = QtWidgets.QLineEdit(self.frame)
        self.supplier_NameLE.setMinimumSize(QtCore.QSize(0, 40))
        self.supplier_NameLE.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.supplier_NameLE.setFont(font)
        self.supplier_NameLE.setStyleSheet("QLineEdit{\n"
"\n"
"\n"
"\n"
"background-color: rgb(220,220, 220);\n"
"\n"
"\n"
"font: \"Sitka Heading\";\n"
"padding: 3px;\n"
"border:2px solid #62D5FF;\n"
"border-radius: 10px;\n"
"font: bold 15px;\n"
"\n"
"color: rgb(0, 0, 0);\n"
"font: 15pt\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"QLineEdit:focus{\n"
"\n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"    \n"
"    \n"
"    border:2px solid rgb(255, 167, 72);\n"
"}")
        self.supplier_NameLE.setObjectName("supplier_NameLE")
        self.gridLayout_2.addWidget(self.supplier_NameLE, 0, 1, 1, 1)
        self.supplier_Save = QtWidgets.QPushButton(self.frame)
        self.supplier_Save.setMinimumSize(QtCore.QSize(200, 0))
        self.supplier_Save.setMaximumSize(QtCore.QSize(100, 35))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.supplier_Save.setFont(font)
        self.supplier_Save.setStyleSheet("QPushButton{\n"
"\n"
"\n"
"background-color: rgba(15, 76, 117, 255);\n"
"font: \"Sitka Heading\";\n"
"padding: 3px;\n"
"border: 2px ;\n"
"border-radius: 10px;\n"
"font: bold 15px;\n"
"\n"
"color: rgb(255, 255, 255);\n"
"font: 15pt\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    background-color:rgba(21, 113, 174,255);\n"
"    border: 2px solid rgba(255, 255, 255, 255)\n"
"\n"
"\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Sidebar_Icons/Savew.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.supplier_Save.setIcon(icon)
        self.supplier_Save.setIconSize(QtCore.QSize(32, 32))
        self.supplier_Save.setAutoRepeatDelay(200)
        self.supplier_Save.setObjectName("supplier_Save")
        self.gridLayout_2.addWidget(self.supplier_Save, 18, 1, 1, 1)
        self.supplier_CountryLE = QtWidgets.QLineEdit(self.frame)
        self.supplier_CountryLE.setMinimumSize(QtCore.QSize(0, 40))
        self.supplier_CountryLE.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.supplier_CountryLE.setFont(font)
        self.supplier_CountryLE.setStyleSheet("QLineEdit{\n"
"\n"
"\n"
"\n"
"background-color: rgb(220,220, 220);\n"
"\n"
"\n"
"font: \"Sitka Heading\";\n"
"padding: 3px;\n"
"border:2px solid #62D5FF;\n"
"border-radius: 10px;\n"
"font: bold 15px;\n"
"\n"
"color: rgb(0, 0, 0);\n"
"font: 15pt\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"QLineEdit:focus{\n"
"\n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"    \n"
"    \n"
"    border:2px solid rgb(255, 167, 72);\n"
"}")
        self.supplier_CountryLE.setObjectName("supplier_CountryLE")
        self.gridLayout_2.addWidget(self.supplier_CountryLE, 3, 1, 1, 1)
        self.supplier_Export = QtWidgets.QPushButton(self.frame)
        self.supplier_Export.setMinimumSize(QtCore.QSize(200, 0))
        self.supplier_Export.setMaximumSize(QtCore.QSize(100, 35))
        self.supplier_Export.setStyleSheet("QPushButton{\n"
"\n"
"\n"
"background-color: rgba(15, 76, 117, 255);\n"
"font: \"Sitka Heading\";\n"
"padding: 3px;\n"
"border: 2px ;\n"
"border-radius: 10px;\n"
"font: bold 15px;\n"
"\n"
"color: rgb(255, 255, 255);\n"
"font: 15pt\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    background-color:rgba(21, 113, 174,255);\n"
"    border: 2px solid rgba(255, 255, 255, 255)\n"
"\n"
"\n"
"}")
        self.supplier_Export.setIconSize(QtCore.QSize(32, 32))
        self.supplier_Export.setObjectName("supplier_Export")
        self.gridLayout_2.addWidget(self.supplier_Export, 20, 1, 1, 1)
        self.gridLayout_4.addWidget(self.frame, 0, 2, 2, 1)
        self.supplier_sreachBTN = QtWidgets.QPushButton(self.frame_3)
        self.supplier_sreachBTN.setMaximumSize(QtCore.QSize(35, 16777215))
        self.supplier_sreachBTN.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.supplier_sreachBTN.setFont(font)
        self.supplier_sreachBTN.setStyleSheet("QPushButton{\n"
"\n"
"\n"
"background-color: rgba(15, 76, 117, 255);\n"
"font: \"Sitka Heading\";\n"
"padding: 3px;\n"
"border: 2px ;\n"
"border-radius: 10px;\n"
"font: bold 15px;\n"
"\n"
"color: rgb(255, 255, 255);\n"
"font: 15pt\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    background-color:rgba(21, 113, 174,255);\n"
"    border: 2px solid rgba(255, 255, 255, 255)\n"
"\n"
"\n"
"}")
        self.supplier_sreachBTN.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Sidebar_Icons/icons8-search-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.supplier_sreachBTN.setIcon(icon1)
        self.supplier_sreachBTN.setIconSize(QtCore.QSize(32, 32))
        self.supplier_sreachBTN.setAutoRepeatDelay(200)
        self.supplier_sreachBTN.setObjectName("supplier_sreachBTN")
        self.gridLayout_4.addWidget(self.supplier_sreachBTN, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.frame_3, 0, 0, 1, 1)

        self.retranslateUi(supplierW)
        QtCore.QMetaObject.connectSlotsByName(supplierW)

    def retranslateUi(self, supplierW):
        _translate = QtCore.QCoreApplication.translate
        supplierW.setWindowTitle(_translate("supplierW", "Form"))
        self.supplier_Search_Bar.setPlaceholderText(_translate("supplierW", "Search By Phone Number"))
        self.supplier_CityLE.setPlaceholderText(_translate("supplierW", "City"))
        self.supplier_EmailLE.setPlaceholderText(_translate("supplierW", "Email"))
        self.supplier_PhoneLE.setPlaceholderText(_translate("supplierW", "Phone Number"))
        self.supplier_StreetLE.setPlaceholderText(_translate("supplierW", "Street Address"))
        self.supplier_reali.setPlaceholderText(_translate("supplierW", "Real"))
        self.supplier_Delete.setText(_translate("supplierW", "DELETE"))
        self.supplier_FDR.setPlaceholderText(_translate("supplierW", "FDR"))
        self.supplier_Note.setPlaceholderText(_translate("supplierW", "Note"))
        self.supplier_Add.setText(_translate("supplierW", "ADD"))
        self.supplier_NameLE.setPlaceholderText(_translate("supplierW", "Name"))
        self.supplier_Save.setText(_translate("supplierW", "Save"))
        self.supplier_CountryLE.setPlaceholderText(_translate("supplierW", "Country"))
        self.supplier_Export.setToolTip(_translate("supplierW", "Print to pdf"))
        self.supplier_Export.setText(_translate("supplierW", "Export"))
        self.supplier_Export.setShortcut(_translate("supplierW", "Ctrl+P"))
