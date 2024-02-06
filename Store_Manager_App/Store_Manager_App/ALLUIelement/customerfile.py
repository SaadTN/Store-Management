# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cus_sup2.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Customertest(object):
    def setupUi(self, Customertest):
        Customertest.setObjectName("Customertest")
        Customertest.resize(983, 559)
        Customertest.setStyleSheet("")
        self.gridLayout = QtWidgets.QGridLayout(Customertest)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_3 = QtWidgets.QFrame(Customertest)
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame = QtWidgets.QFrame(self.frame_3)
        self.frame.setMaximumSize(QtCore.QSize(250, 16777215))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Customer_AddBtn = QtWidgets.QPushButton(self.frame)
        self.Customer_AddBtn.setMinimumSize(QtCore.QSize(200, 0))
        self.Customer_AddBtn.setMaximumSize(QtCore.QSize(100, 35))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Customer_AddBtn.setFont(font)
        self.Customer_AddBtn.setStyleSheet("QPushButton{\n"
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
        self.Customer_AddBtn.setIconSize(QtCore.QSize(32, 32))
        self.Customer_AddBtn.setAutoRepeatDelay(200)
        self.Customer_AddBtn.setObjectName("Customer_AddBtn")
        self.gridLayout_2.addWidget(self.Customer_AddBtn, 7, 1, 1, 1)
        self.Customer_CountryLE = QtWidgets.QLineEdit(self.frame)
        self.Customer_CountryLE.setMinimumSize(QtCore.QSize(0, 40))
        self.Customer_CountryLE.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Customer_CountryLE.setFont(font)
        self.Customer_CountryLE.setStyleSheet("QLineEdit{\n"
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
        self.Customer_CountryLE.setObjectName("Customer_CountryLE")
        self.gridLayout_2.addWidget(self.Customer_CountryLE, 3, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 16, 1, 1, 1)
        self.Customer_StreetLE = QtWidgets.QLineEdit(self.frame)
        self.Customer_StreetLE.setMinimumSize(QtCore.QSize(0, 40))
        self.Customer_StreetLE.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Customer_StreetLE.setFont(font)
        self.Customer_StreetLE.setStyleSheet("QLineEdit{\n"
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
        self.Customer_StreetLE.setObjectName("Customer_StreetLE")
        self.gridLayout_2.addWidget(self.Customer_StreetLE, 5, 1, 1, 1)
        self.Customer_NameLE = QtWidgets.QLineEdit(self.frame)
        self.Customer_NameLE.setMinimumSize(QtCore.QSize(0, 40))
        self.Customer_NameLE.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Customer_NameLE.setFont(font)
        self.Customer_NameLE.setStyleSheet("QLineEdit{\n"
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
        self.Customer_NameLE.setObjectName("Customer_NameLE")
        self.gridLayout_2.addWidget(self.Customer_NameLE, 0, 1, 1, 1)
        self.Customer_CityLE = QtWidgets.QLineEdit(self.frame)
        self.Customer_CityLE.setMinimumSize(QtCore.QSize(0, 40))
        self.Customer_CityLE.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Customer_CityLE.setFont(font)
        self.Customer_CityLE.setStyleSheet("QLineEdit{\n"
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
        self.Customer_CityLE.setObjectName("Customer_CityLE")
        self.gridLayout_2.addWidget(self.Customer_CityLE, 4, 1, 1, 1)
        self.Customer_EmailLE = QtWidgets.QLineEdit(self.frame)
        self.Customer_EmailLE.setMinimumSize(QtCore.QSize(0, 40))
        self.Customer_EmailLE.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Customer_EmailLE.setFont(font)
        self.Customer_EmailLE.setStyleSheet("QLineEdit{\n"
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
        self.Customer_EmailLE.setObjectName("Customer_EmailLE")
        self.gridLayout_2.addWidget(self.Customer_EmailLE, 2, 1, 1, 1)
        self.Customer_Save = QtWidgets.QPushButton(self.frame)
        self.Customer_Save.setMinimumSize(QtCore.QSize(200, 0))
        self.Customer_Save.setMaximumSize(QtCore.QSize(100, 35))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Customer_Save.setFont(font)
        self.Customer_Save.setStyleSheet("QPushButton{\n"
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
        self.Customer_Save.setIcon(icon)
        self.Customer_Save.setIconSize(QtCore.QSize(32, 32))
        self.Customer_Save.setAutoRepeatDelay(200)
        self.Customer_Save.setObjectName("Customer_Save")
        self.gridLayout_2.addWidget(self.Customer_Save, 9, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 6, 1, 1, 1)
        self.Customer_PhoneLE = QtWidgets.QLineEdit(self.frame)
        self.Customer_PhoneLE.setMinimumSize(QtCore.QSize(0, 40))
        self.Customer_PhoneLE.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Customer_PhoneLE.setFont(font)
        self.Customer_PhoneLE.setStyleSheet("QLineEdit{\n"
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
        self.Customer_PhoneLE.setObjectName("Customer_PhoneLE")
        self.gridLayout_2.addWidget(self.Customer_PhoneLE, 1, 1, 1, 1)
        self.Customer_Delete = QtWidgets.QPushButton(self.frame)
        self.Customer_Delete.setMinimumSize(QtCore.QSize(200, 0))
        self.Customer_Delete.setMaximumSize(QtCore.QSize(100, 35))
        self.Customer_Delete.setStyleSheet("QPushButton{\n"
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
        self.Customer_Delete.setIconSize(QtCore.QSize(32, 32))
        self.Customer_Delete.setObjectName("Customer_Delete")
        self.gridLayout_2.addWidget(self.Customer_Delete, 8, 1, 1, 1)
        self.Customer_export = QtWidgets.QPushButton(self.frame)
        self.Customer_export.setMinimumSize(QtCore.QSize(200, 0))
        self.Customer_export.setMaximumSize(QtCore.QSize(100, 35))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Customer_export.setFont(font)
        self.Customer_export.setToolTip("")
        self.Customer_export.setStyleSheet("QPushButton{\n"
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
        self.Customer_export.setIconSize(QtCore.QSize(32, 32))
        self.Customer_export.setAutoRepeatDelay(200)
        self.Customer_export.setObjectName("Customer_export")
        self.gridLayout_2.addWidget(self.Customer_export, 17, 1, 1, 1)
        self.gridLayout_4.addWidget(self.frame, 0, 2, 2, 1)
        self.Customer_Search_Bar = QtWidgets.QLineEdit(self.frame_3)
        self.Customer_Search_Bar.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Customer_Search_Bar.setFont(font)
        self.Customer_Search_Bar.setStyleSheet("QLineEdit{\n"
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
        self.Customer_Search_Bar.setObjectName("Customer_Search_Bar")
        self.gridLayout_4.addWidget(self.Customer_Search_Bar, 0, 0, 1, 1)
        self.Customer_Table = QtWidgets.QTableWidget(self.frame_3)
        self.Customer_Table.setStyleSheet("QTableWidget{\n"
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
        self.Customer_Table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.Customer_Table.setObjectName("Customer_Table")
        self.Customer_Table.setColumnCount(0)
        self.Customer_Table.setRowCount(0)
        self.Customer_Table.verticalHeader().setVisible(False)
        self.gridLayout_4.addWidget(self.Customer_Table, 1, 0, 1, 1)
        self.Customer_sreachBTN = QtWidgets.QPushButton(self.frame_3)
        self.Customer_sreachBTN.setMaximumSize(QtCore.QSize(40, 16777215))
        self.Customer_sreachBTN.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Customer_sreachBTN.setFont(font)
        self.Customer_sreachBTN.setStyleSheet("QPushButton{\n"
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
        self.Customer_sreachBTN.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Sidebar_Icons/icons8-search-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Customer_sreachBTN.setIcon(icon1)
        self.Customer_sreachBTN.setIconSize(QtCore.QSize(32, 32))
        self.Customer_sreachBTN.setAutoRepeatDelay(200)
        self.Customer_sreachBTN.setObjectName("Customer_sreachBTN")
        self.gridLayout_4.addWidget(self.Customer_sreachBTN, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.frame_3, 0, 0, 1, 1)

        self.retranslateUi(Customertest)
        QtCore.QMetaObject.connectSlotsByName(Customertest)
        Customertest.setTabOrder(self.Customer_NameLE, self.Customer_PhoneLE)
        Customertest.setTabOrder(self.Customer_PhoneLE, self.Customer_EmailLE)
        Customertest.setTabOrder(self.Customer_EmailLE, self.Customer_CountryLE)
        Customertest.setTabOrder(self.Customer_CountryLE, self.Customer_CityLE)
        Customertest.setTabOrder(self.Customer_CityLE, self.Customer_StreetLE)
        Customertest.setTabOrder(self.Customer_StreetLE, self.Customer_AddBtn)
        Customertest.setTabOrder(self.Customer_AddBtn, self.Customer_Delete)
        Customertest.setTabOrder(self.Customer_Delete, self.Customer_Save)
        Customertest.setTabOrder(self.Customer_Save, self.Customer_export)
        Customertest.setTabOrder(self.Customer_export, self.Customer_Search_Bar)
        Customertest.setTabOrder(self.Customer_Search_Bar, self.Customer_sreachBTN)
        Customertest.setTabOrder(self.Customer_sreachBTN, self.Customer_Table)

    def retranslateUi(self, Customertest):
        _translate = QtCore.QCoreApplication.translate
        Customertest.setWindowTitle(_translate("Customertest", "Form"))
        self.Customer_AddBtn.setToolTip(_translate("Customertest", "Add row (Alt+A)"))
        self.Customer_AddBtn.setText(_translate("Customertest", "Add"))
        self.Customer_AddBtn.setShortcut(_translate("Customertest", "Alt+A"))
        self.Customer_CountryLE.setPlaceholderText(_translate("Customertest", "Country"))
        self.Customer_StreetLE.setPlaceholderText(_translate("Customertest", "Street Address"))
        self.Customer_NameLE.setPlaceholderText(_translate("Customertest", "Name"))
        self.Customer_CityLE.setPlaceholderText(_translate("Customertest", "City"))
        self.Customer_EmailLE.setPlaceholderText(_translate("Customertest", "Email"))
        self.Customer_Save.setToolTip(_translate("Customertest", "Save changes (Ctrl+S)"))
        self.Customer_Save.setText(_translate("Customertest", " Save"))
        self.Customer_Save.setShortcut(_translate("Customertest", "Ctrl+S"))
        self.Customer_PhoneLE.setPlaceholderText(_translate("Customertest", "Phone Number"))
        self.Customer_Delete.setToolTip(_translate("Customertest", "delete row (Ctrl+D)"))
        self.Customer_Delete.setText(_translate("Customertest", "Delete"))
        self.Customer_Delete.setShortcut(_translate("Customertest", "Ctrl+D"))
        self.Customer_export.setText(_translate("Customertest", "Export"))
        self.Customer_Search_Bar.setPlaceholderText(_translate("Customertest", "Search By Phone Number"))
