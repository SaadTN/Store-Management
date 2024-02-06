import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets,QtSql
from ALLUIelement.sidebar import Ui_Form as Sidebar
from ALLUIelement.purchaseW import Ui_Purchase as PurchaseC


from ALLUIelement.SalesRecods import Ui_SalesRocrods as Sales_RecordsC
from ALLUIelement.home  import Ui_homw as HomeC
from ALLUIelement.customerfile import Ui_Customertest as CustomerC
from ALLUIelement.supplierwidget import Ui_supplierW as SupplierC
from ALLUIelement.Products import Ui_Form as ProductC
from ALLUIelement.Invoice import Ui_Invoice as invoiceC
from ALLUIelement.Purchase_Record import Ui_Form as Purchase_recoredC
from ALLUIelement.SalesRecords import Ui_SalesRocrods as SalesRocrodsC
from ALLUIelement.Budget import Ui_Form as BudgetAccountC
from ALLUIelement.History import Ui_Form as HistoryC
from ALLUIelement.You_Sure import Ui_Form as You_sure
from sqlmodel import SQLModel, create_engine, Session, Field, select
from modules_file import *
from create_table_fpdf2 import PDF
from fpdf import FPDF
from time import time








class Mainfile():
    def create_widgets(self):
        
        SideBar = QtWidgets.QWidget()
        self.sidebarui = Sidebar()
        self.sidebarui.setupUi(SideBar)



        HomeScreenW = QtWidgets.QWidget()
        self.home_2ui= HomeC()
        self.home_2ui.setupUi(HomeScreenW)


        # Sales_recoredsW = QtWidgets.QWidget()
        # self.Salesrecui = Sales_RecordsC()
        # self.Salesrecui.setupUi(Sales_recoredsW)


        PurchaseW = QtWidgets.QWidget()
        self.PurchasewUI = PurchaseC()
        self.PurchasewUI.setupUi(PurchaseW)

        Purchase_Recordw = QtWidgets.QWidget()
        self.Purchase_RecordwUI = Purchase_recoredC()
        self.Purchase_RecordwUI.setupUi(Purchase_Recordw)
             
        CustomerW = QtWidgets.QWidget()
        self.Customerui = CustomerC()
        self.Customerui.setupUi(CustomerW)

        supplierW = QtWidgets.QWidget()
        self.supplierui = SupplierC()
        self.supplierui.setupUi(supplierW)


        InvoiceW = QtWidgets.QWidget()
        self.Invoiceui = invoiceC()
        self.Invoiceui.setupUi(InvoiceW)
     

        SalesrecordW = QtWidgets.QWidget()
        self.Salesrecordui = SalesRocrodsC()
        self.Salesrecordui.setupUi(SalesrecordW)

        ProductW = QtWidgets.QWidget()
        self.ProductWui = ProductC()
        self.ProductWui.setupUi(ProductW)


        BudgetW = QtWidgets.QWidget()
        self.BudgetWui = BudgetAccountC()
        self.BudgetWui.setupUi(BudgetW)
        self.refersh_budget_table()

        HistoryW = QtWidgets.QWidget()
        self.HistoryWui = HistoryC()
        self.HistoryWui.setupUi(HistoryW)

        self.Yousurew = QtWidgets.QWidget()
        self.Yousurewui = You_sure()
        self.Yousurewui.setupUi(self.Yousurew)


        

        self.Leftside = QtWidgets.QStackedWidget()
        self.Leftside.addWidget(SideBar)#the index is always starts with 0
        self.Leftside.setMaximumWidth(250)
        

        self.Rightside = QtWidgets.QStackedWidget()
        self.Rightside.addWidget(HomeScreenW) #the index is 0
        self.Rightside.addWidget(PurchaseW) #the index is 1
        self.Rightside.addWidget(CustomerW) #the index is 3
        self.Rightside.addWidget(supplierW) #the index is 4
        self.Rightside.addWidget(InvoiceW)
        self.Rightside.addWidget(SalesrecordW)
        self.Rightside.addWidget(ProductW)
        self.Rightside.addWidget(Purchase_Recordw)
        self.Rightside.addWidget(BudgetW)
        self.Rightside.addWidget(HistoryW)
      
        self.layout = QtWidgets.QHBoxLayout()
        self.layout.addWidget(self.Leftside)
        self.layout.addWidget(self.Rightside)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0,0,0,0)

        self.mainwindow = QtWidgets.QWidget()
        self.mainwindow.setLayout(self.layout)
        self.mainwindow.resize(1500,1000)
        self.mainwindow.show()
    
    def Show_home(self):
        self.Rightside.setCurrentIndex(0)
        self.Leftside.setCurrentIndex(0)
        

    def show_purchase(self):
        self.Rightside.setCurrentIndex(1)
        self.Leftside.setCurrentIndex(0)
        self.Yousurew.hide()
        self.refersh_purshace_invoice_table()      

    def Show_customer(self):
        self.Rightside.setCurrentIndex(2)
        self.Leftside.setCurrentIndex(0)
        self.Yousurew.hide()
        self.refersh_customer_table()

      

    def Show_supplier(self):
        self.Rightside.setCurrentIndex(3)
        self.Leftside.setCurrentIndex(0)
        self.Yousurew.hide()
        self.refersh_supplier_table()
    


    def Show_invoice(self):
        self.Rightside.setCurrentIndex(4)
        self.Leftside.setCurrentIndex(0)
        self.Yousurew.hide()
        
        self.refersh_invoice_table()


    def Show_SalesRecord(self):
        self.Rightside.setCurrentIndex(5)
        self.Leftside.setCurrentIndex(0)
        self.Yousurew.hide()
        self.refersh_SR_table()
        self.refersh_invoice_table()

        
    def Show_Products(self):
        self.Rightside.setCurrentIndex(6)
        self.Leftside.setCurrentIndex(0)
        self.Yousurew.hide()
        self.refersh_Product_table()

    def Show_Purchase_Record(self):
        self.Rightside.setCurrentIndex(7)
        self.Leftside.setCurrentIndex(0)
        self.Yousurew.hide()
        self.refersh_purchase_Records_table()


    def Show_Budget_account(self):
        self.Rightside.setCurrentIndex(8)
        self.Leftside.setCurrentIndex(0)
        self.refersh_budget_table()
    def Show_History(self):
        self.Rightside.setCurrentIndex(9)
        self.Leftside.setCurrentIndex(0)
        self.refersh_SR_table()
        self.refersh_purchase_Records_table()
        
