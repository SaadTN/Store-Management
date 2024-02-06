import os
import sys

from datetime import datetime , date
from PyQt5 import QtCore, QtGui, QtWidgets,QtSql
from sqlmodel import SQLModel, create_engine, Session, Field, select
from fpdf import FPDF
from time import *

from GUI_Elements import Mainfile
from ALLUIelement.reference_num_gen import generate
from modules_file import *
from create_table_fpdf2 import PDF
from ALLUIelement.Icons_Qrc import *


class Mainapp(Mainfile):
    def __init__(self):
        create_db_and_tables()
        app = QtWidgets.QApplication(sys.argv)
        self.create_widgets()
        self.click_check()
        self.Realtime = localtime(time())
        self.Ftime = datetime(self.Realtime.tm_year,self.Realtime.tm_mon,self.Realtime.tm_mday)
        self.wantedID = 'still not used'
        self.wantedID_purchase = 'still not used'

        sys.exit(app.exec_())

    def click_check(self):
        self.sidebarui.PurchaseBtn.clicked.connect(self.show_purchase)
        self.sidebarui.Customer.clicked.connect(self.Show_customer)
        self.sidebarui.Show_supplier.clicked.connect(self.Show_supplier)
        self.sidebarui.HomeBtn.clicked.connect(self.Show_home)
        self.sidebarui.SalesRecordsBTN.clicked.connect(self.Show_invoice)
        self.sidebarui.Product_Btn.clicked.connect(self.Show_Products)
        self.sidebarui.Budget_BTN.clicked.connect(self.Show_Budget_account)
        self.sidebarui.History_BTN.clicked.connect(self.Show_History)
        

        self.Customerui.Customer_AddBtn.clicked.connect(self.add_to_customer_table)
        self.Customerui.Customer_Delete.clicked.connect(self.You_sure)
        self.Customerui.Customer_Save.clicked.connect(self.edit_customer)
        self.Customerui.Customer_sreachBTN.clicked.connect(self.refersh_customer_table)
        self.Customerui.Customer_export.clicked.connect(self.export_Customer)

        self.supplierui.supplier_Add.clicked.connect(self.add_to_supplier_table)
        self.supplierui.supplier_Delete.clicked.connect(self.You_sure)
        self.supplierui.supplier_Save.clicked.connect(self.edit_supplier)

        self.Invoiceui.INV_add.clicked.connect(self.add_to_invoice_table)
        self.Invoiceui.INV_add.clicked.connect(self.Show_SalesRecord)
        self.Invoiceui.INV_Edit.clicked.connect(self.edit_invoice)
        self.Invoiceui.INV_Delete.clicked.connect(self.You_sure)
        self.Invoiceui.INV_print.clicked.connect(self.make_SI_pdf)
        self.Invoiceui.INV_searchBTN.clicked.connect(self.refersh_invoice_table)
        self.Invoiceui.INV_show_invoiceBTN.clicked.connect(self.show_SinvoiceBtn)
        self.Invoiceui.INV_show_invoiceBTN.clicked.connect(self.refersh_SR_table)
        self.Invoiceui.INV_show_invoiceBTN.clicked.connect(self.Show_SalesRecord)


        self.Invoiceui.INV_print_2.clicked.connect(self.export_invoice)


        #self.Salesrecordui.SR_add.clicked.connect(self.Search_for_customer)
        self.Salesrecordui.SR_Delete.clicked.connect(self.You_sure)
        self.Salesrecordui.SR_add.clicked.connect(self.add_to_SR_table)
        self.Salesrecordui.SR_save.clicked.connect(self.Srecords_save)
        self.Salesrecordui.SR_Done.clicked.connect(self.Srecords_save)
        self.Salesrecordui.SR_Done.clicked.connect(self.Show_invoice)
        self.Salesrecordui.SR_Done.clicked.connect(self.SR_done_btn)


        self.ProductWui.product_AddBtn.clicked.connect(self.add_to_product_table)
        self.ProductWui.product_Delete.clicked.connect(self.You_sure)
        self.ProductWui.product_Save.clicked.connect(self.edit_product)
        self.ProductWui.product_sreachBTN.clicked.connect(self.refersh_Product_table)


        self.BudgetWui.Budget_AddBtn.clicked.connect(self.add_to_budget_table)
        self.BudgetWui.Budget_Delete.clicked.connect(self.You_sure)
        
        self.PurchasewUI.Purchase_AddBtn.clicked.connect(self.add_to_purshace_invoice_table)
        self.PurchasewUI.Purchase_AddBtn.clicked.connect(self.Show_Purchase_Record)
        self.PurchasewUI.Purchase_sreachBTN.clicked.connect(self.refersh_purshace_invoice_table)
        self.PurchasewUI.Purchase_print.clicked.connect(self.make_PI_pdf)
        self.PurchasewUI.Purchase_Delete.clicked.connect(self.You_sure)
        self.PurchasewUI.Purchase_showInvoice.clicked.connect(self.show_PinvoiceBtn)
        self.PurchasewUI.Purchase_showInvoice.clicked.connect(self.refersh_purchase_Records_table)
        self.PurchasewUI.Purchase_showInvoice.clicked.connect(self.Show_Purchase_Record)
        

        self.Purchase_RecordwUI.PR_Add.clicked.connect(self.add_to_purchase_Records_table)
        self.Purchase_RecordwUI.PR_Delete.clicked.connect(self.You_sure)
        self.Purchase_RecordwUI.PR_Done.clicked.connect(self.Precords_save)
        self.Purchase_RecordwUI.PR_Done.clicked.connect(self.show_purchase)
        self.Purchase_RecordwUI.PR_Done.clicked.connect(self.PR_done_btn)

        


##########################################

    def choose_product_data(self):

        if self.ProductWui.product_Search_Bar.text() != "":
            with Session(engine) as session:
                statement = select(Product).where(Product.description == self.ProductWui.product_Search_Bar.text())
                result = session.exec(statement)
                product_instance = result.all()
                #self.Invoiceui.INV_TableWid.setItem(customer_instance)
                return product_instance
        else:
            with Session(engine) as session:
                statment = select(Product)
                result = session.exec(statment)
                allProducts = result.all()
                return allProducts


    
    def add_to_product_table(self):
        try:
            productName = self.ProductWui.product_Name.text()
            productPrice =  self.ProductWui.product_PriceLineEdit.text()
            productQuantity =  self.ProductWui.product_QuantityLineEdit.text()
            Productistaxabile = False

            productInst = Product(description = productName, base_price= productPrice, quantity=productQuantity,IsTaxable=Productistaxabile)

            with Session(engine) as session:
                session.add(productInst)
                session.commit()

            self.ProductWui.product_Table.scrollToBottom()
            self.refersh_Product_table()
        except:
            print('erroe')


   
    def remove_from_product_table(self):
        try:
            row_index = self.ProductWui.product_Table.currentRow()
            cell_content = self.ProductWui.product_Table.item(row_index,0).text() 

            with Session(engine) as session:
                statement = select(Product).where(Product.id == int(cell_content))
                results = session.exec(statement)
                instanceProduct = results.first()
                print(instanceProduct)


                session.delete(instanceProduct)    
                session.commit()

            self.refersh_Product_table()
        except:
            print('there is an error here')



            



    def refersh_Product_table(self):
        self.ProductWui.product_Table.clear()
        
        self.Product_Data = self.choose_product_data()
        self.ProductWui.product_Table.setRowCount(len(self.Product_Data))
        self.ProductWui.product_Table.setColumnCount(4)
        self.ProductWui.product_Table.setHorizontalHeaderLabels(['id', 'Product name','Price','quantity'])
        
        self.ProductWui.product_Table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

         
        self.ProductIdList = []
        self.ProductNameList = []
        self.ProductPriceList = []
        self.ProductQuantityList= []

      
        for j in self.Product_Data:
            self.ProductIdList.append(j.id)
            self.ProductNameList.append(j.description)
            self.ProductPriceList.append(j.base_price)
            self.ProductQuantityList.append(j.quantity)

            

        for jdx, j in enumerate(self.ProductIdList):
            self.ProductWui.product_Table.setItem(jdx,0, QtWidgets.QTableWidgetItem(str(j)))
        for jdx, j in enumerate(self.ProductNameList):
            self.ProductWui.product_Table.setItem(jdx,1, QtWidgets.QTableWidgetItem(str(j)))
        for jdx, j in enumerate(self.ProductPriceList):
            self.ProductWui.product_Table.setItem(jdx,2, QtWidgets.QTableWidgetItem(str(j)))
        for jdx, j in enumerate(self.ProductQuantityList):
            self.ProductWui.product_Table.setItem(jdx,3, QtWidgets.QTableWidgetItem(str(j)))



    def edit_product(self):
        try:        
            with Session(engine) as session:        
                row_index =  self.ProductWui.product_Table.currentRow()
                column_index =  self.ProductWui.product_Table.currentColumn()
                current_cell_content =  self.ProductWui.product_Table.item(row_index,column_index).text()       
                statement = select(Product).where(Product.id == row_index+1)
                results = session.exec(statement)
                product_instance = results.one()        
                if column_index == 0:
                    product_instance.id = current_cell_content  
                elif column_index == 1:
                    product_instance.description = current_cell_content
                elif column_index == 2:
                    product_instance.base_price = current_cell_content
                elif column_index == 3:
                    product_instance.quantity = current_cell_content        

                session.add(product_instance)

                session.commit()

                self.refersh_Product_table()
        except:
            print('error1')


##########################################


    def choose_SR_data(self):
            
        
        with Session(engine) as session:
            if self.choosenSRcond == 0:
                statement = select(Sales_Record)
                result = session.exec(statement)
                allSRecords = result.all()
                return allSRecords
            elif self.choosenSRcond == 1:
                statment = select(Sales_invoice).where(Sales_invoice.id == self.wantedID)
                result = session.exec(statment)
                recs1_from_invoice = result.one().records

                return recs1_from_invoice
            elif self.choosenSRcond == 2:
                statment = select(Sales_invoice).where(Sales_invoice.id == int(self.cell_content))
                result = session.exec(statment)
                recs2_from_invoice = result.one().records
                return recs2_from_invoice
            

    def add_to_SR_table(self):
        try: 

            timestamp = self.Ftime
            quantityy =  self.Salesrecordui.SR_Quantity.text()
            description =  self.Salesrecordui.SR_Description.text()
            discount =  self.Salesrecordui.SR_Discount.text()
            phonesearch = self.Salesrecordui.SR_PhoneNumber.text()



            with Session(engine) as session:

                statement = select(Customer).where(Customer.phonenumber == phonesearch)
                result = session.exec(statement)
                CusInst = result.first()



                if self.choosenSRcond == 1: 
                    statement2 = select(Sales_invoice).where(Sales_invoice.id == self.wantedID )
                elif self.choosenSRcond == 2:
                    statement2 = select(Sales_invoice).where(Sales_invoice.id == int(self.cell_content))
                result2 = session.exec(statement2)
                invoice_idd = result2.first()
                invoice_idd.customer = CusInst
                invoice_idd.discount_percentage = discount
                session.add(invoice_idd)




               # This is to assign the prices in each Sales Record from the Product + to check if the inventory is enough
                statement3 =select(Product).where(Product.id == int(self.Salesrecordui.SR_ProductID.text()))
                result3 = session.exec(statement3)
                productid = result3.first()

                if  (productid.quantity - int(quantityy)) < 0 :
                    print("We don't have enough quantity")
                else: 
                    productid.quantity -= int(quantityy)
                    session.add(productid)

                    unit_price_from_product= productid.base_price
                    total_price= float(unit_price_from_product) * float(quantityy)

                    salesRecordInst = Sales_Record( invoice= invoice_idd,product= productid, timestamp=timestamp, qunatity=quantityy, description=description , discount= discount,unit_price=unit_price_from_product, total_price=total_price)
                    session.add(salesRecordInst)
                    session.commit()

                self.refersh_SR_table()
                self.Salesrecordui.SR_ProductID.clear()
                self.Salesrecordui.SR_Quantity.clear()
                self.Salesrecordui.SR_Description.clear()




                #stat = select(Sales_invoice).where(Sales_invoice.id == self.wantedID )
                #resss = session.exec(stat)
                #invoice_idd = resss.first()

                # This is to make the: invoice total = the sum of the prices of each Sales record
                invoice_lists = []
                for i in invoice_idd.records:
                   invoice_lists.append(float(i.total_price))
                self.invoice_listtt = sum(invoice_lists)
                invoice_idd.invoice_total = self.invoice_listtt
                invoice_idd.total_with_tax= (invoice_idd.invoice_total * 1.15 ) * ( (100-(int(discount))) /100 )  
                session.add(invoice_idd)
                session.commit()


                self.refersh_invoice_table()
                self.refersh_SR_table()





            self.Salesrecordui.SR_table.scrollToBottom()
        except:
            print('error2')





    def remove_from_SR_table(self):
        try:
            row_index = self.Salesrecordui.SR_table.currentRow()
            cell_content = self.Salesrecordui.SR_table.item(row_index,0).text() 

            with Session(engine) as session:
                statement = select(Sales_Record).where(Sales_Record.id == int(cell_content))
                results = session.exec(statement)
                instanceSR = results.one()


                session.delete(instanceSR)    
                session.commit()

            self.refersh_SR_table()
        except:
            pass


        
    def show_SinvoiceBtn(self):
        self.row_index =  self.Invoiceui.INV_TableWid.currentRow()
        self.cell_content =  self.Invoiceui.INV_TableWid.item(self.row_index,0).text()


    def refersh_SR_table(self):
        if self.Rightside.currentIndex() == 9:
            variable = self.HistoryWui.Sales_Table_history
            self.choosenSRcond = 0
        elif self.wantedID == 'still not used':
            variable = self.Salesrecordui.SR_table
            self.choosenSRcond = 2
            self.Salesrecordui.SR_add.hide()
            self.Salesrecordui.SR_save.hide()
            self.Salesrecordui.SR_Delete.setText("Return Item")
        else:
            self.Salesrecordui.SR_add.show()
            self.Salesrecordui.SR_save.show()
            variable = self.Salesrecordui.SR_table
            self.choosenSRcond = 1
            


        variable.clear()
        self.Sales_records_Data = self.choose_SR_data()
        variable.setRowCount(len(self.Sales_records_Data))
        variable.setColumnCount(8)
        variable.setHorizontalHeaderLabels(['id', 'invoice_id','product_id','description','timestamp','qunatity','unit_price','total_price'])
        variable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)


        self.idListSR = []
        self.invoice_idSR = []
        self.product_idSR = []
        self.descriptionSR= []
        self.qunatitySR = []
        self.unit_priceSR = []
        self.total_priceSR = []
      
        for j in self.Sales_records_Data:
            self.idListSR.append(j.id)
            
            self.invoice_idSR.append(j.invoice_id)
            self.product_idSR.append(j.product_id)
            self.descriptionSR.append(j.description)
            self.qunatitySR.append(j.qunatity)
            self.unit_priceSR.append(j.unit_price)
            self.total_priceSR.append(j.total_price)
            

        for jdx, j in enumerate(self.idListSR):
            variable.setItem(jdx,0, QtWidgets.QTableWidgetItem(str(j)))
        for jdx, j in enumerate(self.invoice_idSR):
            variable.setItem(jdx,1, QtWidgets.QTableWidgetItem(str(j)))
        for jdx, j in enumerate(self.product_idSR):
            variable.setItem(jdx,2, QtWidgets.QTableWidgetItem(str(j)))
        for jdx, j in enumerate(self.descriptionSR):
            variable.setItem(jdx,3, QtWidgets.QTableWidgetItem(str(j)))        
        for jdx, j in enumerate(self.qunatitySR):
            variable.setItem(jdx,4, QtWidgets.QTableWidgetItem(str(j)))
        for jdx, j in enumerate(self.qunatitySR):
            variable.setItem(jdx,5, QtWidgets.QTableWidgetItem(str(j)))
        for jdx, j in enumerate(self.unit_priceSR):
            variable.setItem(jdx,6, QtWidgets.QTableWidgetItem(str(j)))
        for jdx, j in enumerate(self.total_priceSR):
            variable.setItem(jdx,7, QtWidgets.QTableWidgetItem(str(j)))



    def SR_done_btn(self):
        self.Salesrecordui.SR_Discount.clear()
        self.Salesrecordui.SR_PhoneNumber.clear()
        print(self.Salesrecordui.SR_table.rowCount())
        if self.Salesrecordui.SR_table.rowCount() == 0:
            with Session(engine) as session:
                if self.wantedID != 'still not used':
                    statement = select(Sales_invoice).where(Sales_invoice.id == self.wantedID)
                else:
                    statement = select(Sales_invoice).where(Sales_invoice.id == int(self.cell_content))
                results = session.exec(statement)
                instanceinvoice = results.one()

                session.delete(instanceinvoice)    
                session.commit()
                
        else:
            try:
                with Session(engine) as session:
                    statement = select(Sales_invoice).where(Sales_invoice.id == self.wantedID)
                    results = session.exec(statement)
                    instanceinvoice = results.one()
                    transaction = Budget_Account(transaction_type= "Deposit" , amount= instanceinvoice.total_with_tax, description= "Sale", timestamp= instanceinvoice.timestamp)
                    session.add(transaction)           
                    session.commit()
            except:
                pass
        self.wantedID = 'still not used'
        self.refersh_invoice_table()
        self.refersh_budget_table()
                     
        
            

    def Srecords_save(self):
        if self.wantedID != 'still not used':
            with Session(engine) as session:
                stat = select(Sales_invoice).where(Sales_invoice.id == self.wantedID)
                res = session.exec(stat)
                row = res.one()

                invoice_lists = []
                for i in row.records:
                   invoice_lists.append(float(i.total_price * i.qunatity))
                self.invoice_listtt = sum(invoice_lists)
                print(self.invoice_listtt)
                row.invoice_total = self.invoice_listtt
                session.add(row)
                session.commit()
         
            self.refersh_invoice_table()
            self.refersh_SR_table()




####################################

    def add_to_invoice_table(self):
        try:
        

            self.Salesrecordui.SR_table.setRowCount(0)
            self.Salesrecordui.SR_table.setHorizontalHeaderLabels(['id', 'invoice_id','product_id','description','timestamp','qunatity','unit_price','total_price'])

            phonesearch = self.Salesrecordui.SR_PhoneNumber.text()
            discount_p =  self.Salesrecordui.SR_Discount.text()
            timestamp = self.Ftime
            visible_Reference_Number =  generate(8)
            note_for_sale_invoice ='' #self.Salesrecordui.SR_note.text()



            # to connect the customer to the invoice 
            with Session(engine) as session:
                statement = select(Customer).where(Customer.phonenumber == phonesearch)
                result = session.exec(statement)
                CusInst = result.first()

            # this is to add the invoices in the database

                salesInvoice_Inst = Sales_invoice(customer= CusInst, timestamp =timestamp, discount_percentage= discount_p , visible_Reference_Number= visible_Reference_Number, note= note_for_sale_invoice)
                session.add(salesInvoice_Inst)
                session.commit()
            self.refersh_invoice_table()



            self.Invoiceui.INV_TableWid.scrollToBottom()


            self.wantedID  = self.Invoice_ID_list[len(self.Invoice_ID_list)-1]
            print(self.wantedID)
        except: 
            print('error')

        


   
    def remove_from_invoice_table(self):
        try:
            row_index = self.Invoiceui.INV_TableWid.currentRow()
            cell_content = self.Invoiceui.INV_TableWid.item(row_index,0).text() 

            with Session(engine) as session:
                statement = select(Sales_invoice).where(Sales_invoice.id == int(cell_content))
                results = session.exec(statement)
                instanceinvoice = results.one()
                therecords_in_invoice = instanceinvoice.records

                session.delete(instanceinvoice) 
                # session.delete(therecords_in_invoice)
                   
                session.commit()
            self.refersh_invoice_table()
        except:
            print('error')




    def choose_invoice_data(self):
        print(self.Invoiceui.INV_Search_Bar.text())
        if self.Invoiceui.INV_Search_Bar.text() != "":
            with Session(engine) as session:
                statement = select(Customer).where(Customer.phonenumber == self.Invoiceui.INV_Search_Bar.text())
                result = session.exec(statement)
                customer_instance = result.first().invoices
                #self.Invoiceui.INV_TableWid.setItem(customer_instance)
                return customer_instance
        else:
            with Session(engine) as session:
                statment = select(Sales_invoice)
                result = session.exec(statment)
                all_invoice = result.all()

                return all_invoice
        
        



    def refersh_invoice_table(self):

        self.Invoiceui.INV_TableWid.clear()
        self.Invoice_Data = self.choose_invoice_data()
        self.Invoiceui.INV_TableWid.setRowCount(len(self.Invoice_Data))
        self.Invoiceui.INV_TableWid.setColumnCount(6)
        self.Invoiceui.INV_TableWid.setHorizontalHeaderLabels(['id', 'Timestamp','Discount','invoice total','total with tax','Reference_Number'])
        
        self.Invoiceui.INV_TableWid.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

         
        self.Invoice_ID_list = []
        self.Invoice_timestamp_list = []
        self.Invoice_discount_list = []
        self.Invoice_total_list= []
        self.Invoice_totalWTax_list = []
        self.Invoice_refNum_list = []

             

        for j in self.Invoice_Data:
            self.Invoice_ID_list.append(j.id)
            self.Invoice_timestamp_list.append(j.timestamp)
            self.Invoice_discount_list.append(j.discount_percentage)
            self.Invoice_total_list.append(j.invoice_total)
            self.Invoice_totalWTax_list.append(j.total_with_tax)
            self.Invoice_refNum_list.append(j.visible_Reference_Number)


        for jdx, j in enumerate(self.Invoice_ID_list):
            self.Invoiceui.INV_TableWid.setItem(jdx,0, QtWidgets.QTableWidgetItem(str(j)))
        for jdx, j in enumerate(self.Invoice_timestamp_list):
            self.Invoiceui.INV_TableWid.setItem(jdx,1, QtWidgets.QTableWidgetItem(str(j)))
        for jdx, j in enumerate(self.Invoice_discount_list):
            self.Invoiceui.INV_TableWid.setItem(jdx,2, QtWidgets.QTableWidgetItem(str(j)))
        for jdx, j in enumerate(self.Invoice_total_list):
            self.Invoiceui.INV_TableWid.setItem(jdx,3, QtWidgets.QTableWidgetItem(str(j)))
        for jdx, j in enumerate(self.Invoice_totalWTax_list):
            self.Invoiceui.INV_TableWid.setItem(jdx,4, QtWidgets.QTableWidgetItem(str(j)))
        for jdx, j in enumerate(self.Invoice_refNum_list):
            self.Invoiceui.INV_TableWid.setItem(jdx,5, QtWidgets.QTableWidgetItem(str(j)))
        
            
    def export_invoice(self):
        invoiceCSV = open("Invoices.csv",'w')
        invoiceCSV.write('ID,Invoice time, Discount, Invoice total, Total with tax, Visible refernce number\n')
        for j in self.Invoice_Data:
            self.Invoice_ID_list.append(j.id)
            self.Invoice_timestamp_list.append(j.timestamp)
            self.Invoice_discount_list.append(j.discount_percentage)
            self.Invoice_total_list.append(j.invoice_total)
            self.Invoice_totalWTax_list.append(j.total_with_tax)
            self.Invoice_refNum_list.append(j.visible_Reference_Number)
            invoiceCSV.write(f"{j.id},{j.timestamp},{j.discount_percentage},{j.invoice_total},{j.total_with_tax},{j.visible_Reference_Number}\n")
        invoiceCSV.close()


    def edit_invoice(self):
    
        with Session(engine) as session:

            row_index =  self.Invoiceui.INV_TableWid.currentRow()
            column_index=  self.Invoiceui.INV_TableWid.currentColumn()
            cell_content =  self.Invoiceui.INV_TableWid.item(row_index,column_index).text()

            statement = select(Sales_invoice).where(Sales_invoice.id == row_index+1)
            results = session.exec(statement)
            invoice_instance = results.one()


            if column_index == 0:
                invoice_instance.id = cell_content  
            elif column_index == 1:
                invoice_instance.timestamp = cell_content
            elif column_index == 2:
                invoice_instance.discount_percentage = cell_content
            elif column_index== 3:
                invoice_instance.invoice_total = cell_content
            elif column_index== 4:
                invoice_instance.total_with_tax = cell_content
            elif column_index== 5:
                invoice_instance.visible_Reference_Number = cell_content
            
            session.add(invoice_instance)
           
            session.commit()
        
            self.refersh_SR_table()

        #def show_Sinvoice(self):
        #    row_index =  self.Invoiceui.INV_TableWid.currentRow()
        #    select_id = self.Invoiceui.INV_TableWid.item(0,row_index)
        #    with Session(engine) as session:
        #        statement = select(Sales_invoice).where(Sales_invoice.id == int(select_id))
        #        result = session


##########################################


    def choose_customer_data(self):
        if self.Customerui.Customer_Search_Bar.text() != "":
            with Session(engine) as session:
                statement = select(Customer).where(Customer.phonenumber == self.Customerui.Customer_Search_Bar.text())
                ressult = session.exec(statement)
                all_customers = ressult.all()

                return all_customers
        else:
            with Session(engine) as session:
                statment = select(Customer)
                result = session.exec(statment)
                all_Customer = result.all()
 
                return all_Customer


    def add_to_customer_table(self):
        customerName = self.Customerui.Customer_NameLE.text()
        customerEmail = self.Customerui.Customer_EmailLE.text()
        customerPhoneNum =  self.Customerui.Customer_PhoneLE.text()
        customerCountry =  self.Customerui.Customer_CountryLE.text()
        customerCity =  self.Customerui.Customer_CityLE.text()
        customerstreetadd =  self.Customerui.Customer_StreetLE.text()
        
        
        
        customer = Customer(name=  customerName,email= customerEmail, phonenumber= customerPhoneNum,country= customerCountry,city= customerCity ,streetadress= customerstreetadd)
        
        with Session(engine) as session1:
            session1.add(customer)
            session1.commit()
        self.refersh_customer_table()
        self.Customerui.Customer_Table.scrollToBottom()

   
    def remove_from_customer_table(self):
        try:
            h = self.Customerui.Customer_Table.currentRow()
            g = self.Customerui.Customer_Table.item(h,0).text() 

            with Session(engine) as session:
                statement = select(Customer).where(Customer.id == int(g))
                results = session.exec(statement)
                instanceCUSTOMER = results.one()
                #session.delete((instanceCUSTOMER.invoices))
                session.delete(instanceCUSTOMER)    
                session.commit()

            self.refersh_customer_table()
        except:
            pass
                



    def refersh_customer_table(self):
        self.Customerui.Customer_Table.clear()
        
        self.Customer_Data = self.choose_customer_data()
        self.Customerui.Customer_Table.setRowCount(len(self.Customer_Data))
        self.Customerui.Customer_Table.setColumnCount(7)
        self.Customerui.Customer_Table.setHorizontalHeaderLabels(['id', 'Name','Email','Phone Number','Country','City','street'])
        
        self.Customerui.Customer_Table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

         
        self.idList = []
        self.nameList = []
        self.email = []
        self.phoneNo = []
        self.country = []
        self.city = []
        self.street = []
        
        for j in self.Customer_Data:
            self.idList.append(j.id)
            self.nameList.append(j.name)
            self.email.append(j.email)
            self.phoneNo.append(j.phonenumber)
            self.country.append(j.country)
            self.city.append(j.city)
            self.street.append(j.streetadress)

        for jdx, j in enumerate(self.idList):
            self.Customerui.Customer_Table.setItem(jdx,0, QtWidgets.QTableWidgetItem(str(j)))
        for jdx, j in enumerate(self.nameList):
            self.Customerui.Customer_Table.setItem(jdx,1, QtWidgets.QTableWidgetItem(str(j)))
        for jdx, j in enumerate(self.email):
            self.Customerui.Customer_Table.setItem(jdx,2, QtWidgets.QTableWidgetItem(str(j)))
        for jdx, j in enumerate(self.phoneNo):
            self.Customerui.Customer_Table.setItem(jdx,3, QtWidgets.QTableWidgetItem(str(j)))
        for jdx, j in enumerate(self.country):
            self.Customerui.Customer_Table.setItem(jdx,4, QtWidgets.QTableWidgetItem(str(j)))
        for jdx, j in enumerate(self.city):
            self.Customerui.Customer_Table.setItem(jdx,5, QtWidgets.QTableWidgetItem(str(j)))
        for jdx, j in enumerate(self.street):
            self.Customerui.Customer_Table.setItem(jdx,6, QtWidgets.QTableWidgetItem(str(j)))
        
 
    def edit_customer(self):

        with Session(engine) as session:

            row_index =  self.Customerui.Customer_Table.currentRow()
            cell_content= self.Customerui.Customer_Table.item(row_index,0).text()
            column_index=  self.Customerui.Customer_Table.currentColumn()
            current_cell_content =  self.Customerui.Customer_Table.item(row_index,column_index).text()
            


            statement = select(Customer).where(Customer.id == int(cell_content))
            results = session.exec(statement)
            customer_instance = results.one()


            if column_index == 0:
                customer_instance.id = current_cell_content  
            elif column_index == 1:
                customer_instance.name = current_cell_content
            elif column_index == 2:
                customer_instance.email = current_cell_content
            elif column_index== 3:
                customer_instance.phonenumber = current_cell_content
            elif column_index== 4:
                customer_instance.country = current_cell_content
            elif column_index== 5:
                customer_instance.city = current_cell_content
            elif column_index== 6:
                customer_instance.streetadress = current_cell_content

            session.add(customer_instance)
           
            session.commit()
        
            self.refersh_customer_table()
            


##########################################

    def choose_supplier_data(self):
        if self.supplierui.supplier_Search_Bar.text() != "":
            with Session(engine) as session:
                statement = select(Supplier).where(Supplier.phone_number == self.supplierui.supplier_Search_Bar.text())
                ressult = session.exec(statement)
                all_suppliers = ressult.all()

                return all_suppliers
        else:
            with Session(engine) as session:
                statment = select(Supplier)
                result = session.exec(statment)
                all_suppliers = result.all()
 
                return all_suppliers

    def add_to_supplier_table(self):
        try:
            supplierName = self.supplierui.supplier_NameLE.text()
            supplierEmail = self.supplierui.supplier_EmailLE.text()
            supplierPhoneNum =  self.supplierui.supplier_PhoneLE.text()
            supplierCountry =  self.supplierui.supplier_CountryLE.text()
            supplierCity =  self.supplierui.supplier_CityLE.text()
            supplierstreetadd =  self.supplierui.supplier_StreetLE.text()
            supplierfast =  self.supplierui.supplier_FDR.text()
            supplierreal =  self.supplierui.supplier_reali.text()
            suppliernote =  self.supplierui.supplier_Note.text()
            self.supplierui.supplier_Table.scrollToBottom()
            supplier = Supplier(name=  supplierName,email= supplierEmail, phone_number= supplierPhoneNum,country= supplierCountry,city= supplierCity ,street_address= supplierstreetadd, fast_delivery_rating= supplierfast,reliability_rating=supplierreal,Note=suppliernote )
            
            with Session(engine) as session1:
                session1.add(supplier)
                session1.commit()
            self.refersh_supplier_table()
        except:
            print('error')
            
    def remove_from_supplier_table(self):
        try:

            h = self.supplierui.supplier_Table.currentRow()
            g = self.supplierui.supplier_Table.item(h,0).text() 
        
            with Session(engine) as session:
                statement = select(Supplier).where(Supplier.id == int(g))
                results = session.exec(statement)
                instanceSupplier = results.one()
                session.delete(instanceSupplier)    
                session.commit()
            self.refersh_supplier_table()
        except:
            pass
    def refersh_supplier_table(self):
        self.supplierui.supplier_Table.clear()
        self.data = self.choose_supplier_data()
        self.supplierui.supplier_Table.setRowCount(len(self.data))
        self.supplierui.supplier_Table.setColumnCount(10)
        self.supplierui.supplier_Table.setHorizontalHeaderLabels(['id', 'Name','Email','Phone Number','Country','City','street','fast','real','note'])
        self.supplierui.supplier_Table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.idList1 = []
        self.nameList1 = []
        self.email1 = []
        self.phoneNo1 = []
        self.country1 = []
        self.city1 = []
        self.street1 = []
        self.fast1 = []
        self.real1 = []
        self.note1 = []

        for j in self.data:
            self.idList1.append(j.id)
            self.nameList1.append(j.name)
            self.email1.append(j.email)
            self.phoneNo1.append(j.phone_number)
            self.country1.append(j.country)
            self.city1.append(j.city)
            self.street1.append(j.street_address)
            self.fast1.append(j.fast_delivery_rating)
            self.real1.append(j.reliability_rating)
            self.note1.append(j.Note)
        for jdx, j in enumerate(self.idList1):
            self.supplierui.supplier_Table.setItem(jdx,0, QtWidgets.QTableWidgetItem(str(j)))
        for jdx, j in enumerate(self.nameList1):
            self.supplierui.supplier_Table.setItem(jdx,1, QtWidgets.QTableWidgetItem(str(j)))
        for jdx, j in enumerate(self.email1):
            self.supplierui.supplier_Table.setItem(jdx,2, QtWidgets.QTableWidgetItem(str(j)))
        for jdx, j in enumerate(self.phoneNo1):
            self.supplierui.supplier_Table.setItem(jdx,3, QtWidgets.QTableWidgetItem(str(j)))
        for jdx, j in enumerate(self.country1):
            self.supplierui.supplier_Table.setItem(jdx,4, QtWidgets.QTableWidgetItem(str(j)))
        for jdx, j in enumerate(self.city1):
            self.supplierui.supplier_Table.setItem(jdx,5, QtWidgets.QTableWidgetItem(str(j)))
        for jdx, j in enumerate(self.street1):
            self.supplierui.supplier_Table.setItem(jdx,6, QtWidgets.QTableWidgetItem(str(j)))
        for jdx, j in enumerate(self.fast1):
            self.supplierui.supplier_Table.setItem(jdx,7, QtWidgets.QTableWidgetItem(str(j)))
        for jdx, j in enumerate(self.real1):
            self.supplierui.supplier_Table.setItem(jdx,8, QtWidgets.QTableWidgetItem(str(j)))
        for jdx, j in enumerate(self.note1):
            self.supplierui.supplier_Table.setItem(jdx,9, QtWidgets.QTableWidgetItem(str(j)))

    def edit_supplier(self):
        try:
            with Session(engine) as session:
                h = self.supplierui.supplier_Table.currentRow()
                statement = select(Supplier).where(Supplier.id == h+1)
                results = session.exec(statement)
                row = results.one()
                a= self.supplierui.supplier_Table.currentColumn()
                g = self.supplierui.supplier_Table.item(h,a).text()
                if a == 0:
                    row.id = g  
                elif a == 1:
                    row.name = g
                elif a == 2:
                    row.email = g
                elif a == 3:
                    row.phone_number = g
                elif a == 4:
                    row.country = g
                elif a == 5:
                    row.city = g
                elif a == 6:
                    row.street_address = g
                elif a == 7:
                    row.fast_delivery_rating = g
                elif a == 8:
                    row.reliability_rating = g
                elif a == 9:
                    row.Note = g
                session.add(row)
                session.commit()
            self.refersh_supplier_table()   
        except:
                print('error')

    def make_SI_pdf(self):
        row_index =  self.Invoiceui.INV_TableWid.currentRow()
        print(row_index)
        cell_content= self.Invoiceui.INV_TableWid.item(row_index,0).text()
       
        with Session(engine) as session:
            statement = select(Sales_invoice).where(Sales_invoice.id == int(cell_content) )
            result = session.exec(statement)
            invoiceInst = result.first()
            recs_in_invoice = invoiceInst.records
            customer_from_invoice = invoiceInst.customer
            print(recs_in_invoice)
        
            self.printIdList = []
            self.printDescriptionList = []
            self.printQuantityList = []
            self.printUnitPriceList = []
            self.printTotalPriceList = []
            for i in recs_in_invoice:
                self.printIdList.append(i.id)
                self.printDescriptionList.append(i.product.description)
                self.printQuantityList.append(i.qunatity)
                self.printUnitPriceList.append(i.unit_price)
                self.printTotalPriceList.append(i.total_price)

            
        


            data_as_dict = {"Item": self.printIdList ,
                    "description":self.printDescriptionList ,
                    "quantity":self.printQuantityList,
                    "Unit price":self.printUnitPriceList,
                    "Total":self.printTotalPriceList,
                    #"city":city,
                   # "streetadress":street
                }
            pdf = PDF()
            pdf.add_page(format= "a4")
            #pdf.add_page(format= "letter")
            y=10
            pdf.set_text_color(60)
            pdf.set_font("helvetica","B",size=30)
            pdf.set_xy(146,20)
            #pdf.set_draw_color(255,0,0)
            pdf.cell(45,12,"INVOICE",border=0)
            pdf.set_fill_color(215)
            pdf.set_text_color(0)
            pdf.set_font("","B",size=10)
            pdf.set_xy(15,y+50)
            pdf.cell(75,7,"    BILL TO:",fill = True, border= 1)
            pdf.set_font(size=10)
            pdf.set_xy(15,y+60)
            # this is for the customer details
            pdf.multi_cell(40,5,f" [{customer_from_invoice.id}]\n [{customer_from_invoice.name}]\n [{customer_from_invoice.email}]\n [{customer_from_invoice.phonenumber}]\n [{customer_from_invoice.country}]\n [{customer_from_invoice.city}]\n [{customer_from_invoice.streetadress}]\n  ")
            pdf.set_font("","B",size=10)
            pdf.set_xy(110,y+50)
            #pdf.set_draw_color(255,0,0)
            pdf.cell(40,7,"DATE:",fill=True,border=1,align="C")
            pdf.ln
            pdf.cell(40,7,"INVOICE #:",fill=True,border=1,align="C")
            pdf.set_font(size=10)
            pdf.set_xy(110,y+58)
            pdf.cell(40,7,f"{invoiceInst.timestamp}",border=1,align="C")
            pdf.ln
            pdf.cell(40,7,f"#{invoiceInst.id}",border=1,align="C")
            pdf.set_xy(100,y+100)
            pdf.create_table(table_data = data_as_dict,title= "",align_header='L', align_data='L', cell_width=[15,70,30,30,30,], x_start=15,  emphasize_style='BIU',emphasize_color=(255,0,0))
            pdf.set_x(140)
            pdf.multi_cell(50,7,f"INVOICE TOTAL: {invoiceInst.invoice_total}\nTOTAL WITH TAX: {invoiceInst.total_with_tax} ", border =1)
            #pdf.multi_cell(20,5,f" [{invoiceInst.invoice_total}]\n [{invoiceInst.total_with_tax}]\n [{}]\n ")
            pdf.output(f'sales_invoice_number_{invoiceInst.id}.pdf')
            os.system(f'sales_invoice_number_{invoiceInst.id}.pdf')




    def choose_purchase_Records_data(self):
        with Session(engine) as session:
            if self.choosenPRcond == 0:
                statement = select(Purchase_Record)
                result = session.exec(statement)
                allPRecords = result.all()
                print(allPRecords)
                return allPRecords
            elif self.choosenPRcond == 1:
                statment = select(Purchase_invoice).where(Purchase_invoice.id == self.wantedID_purchase)
                result = session.exec(statment)
                precs_from_invoice = result.one().pprecords
                #invoice_lists = []
                #for i in precs_from_invoice:
                #    invoice_lists.append(float(i.price))
                #self.invoice_listtt = sum(invoice_lists)
                return precs_from_invoice
            elif self.choosenPRcond == 2:
                statment = select(Purchase_invoice).where(Purchase_invoice.id == int(self.cell_contentt))
                result = session.exec(statment)
                recs2_from_invoice = result.one().pprecords
                return recs2_from_invoice           


    def add_to_purchase_Records_table(self):
        
        try:
            Phonenumber = self.Purchase_RecordwUI.PR_PhoneNumber.text()
            #Product_id= self.Purchase_RecordwUI.PR_ProductID.text()
            Product_quantity =  self.Purchase_RecordwUI.PR_Quantity.text()
            price= 0 #self.Purchase_RecordwUI.PR_Price.text()
            Description =  self.Purchase_RecordwUI.PR_Description.text()

            with Session(engine) as session:
                statement = select(Supplier).where(Supplier.phone_number == Phonenumber)
                result = session.exec(statement)
                SupInst = result.first()




                statement1 = select(Purchase_invoice).where(Purchase_invoice.id == self.wantedID_purchase )
                result1 = session.exec(statement1)
                Invoice_from_precord = result1.first()
                Invoice_from_precord.supplier = SupInst
                session.add(Invoice_from_precord)


               
                statement2 =select(Product).where(Product.id == int(self.Purchase_RecordwUI.PR_ProductID.text()))
                result2 = session.exec(statement2)
                productid = result2.first()
                price_precord = productid.base_price
                print(f'the prod{productid}')

                productid.quantity += int(Product_quantity)
                session.add(productid)
                



                salesRecordInst = Purchase_Record( pproduct= productid, timestamp= self.Ftime, quantity=Product_quantity, description=Description , price=price_precord, pinvoice=Invoice_from_precord)

                session.add(salesRecordInst)
                session.commit()


                self.refersh_purchase_Records_table()
                self.Purchase_RecordwUI.PR_ProductID.clear()
                self.Purchase_RecordwUI.PR_Quantity.clear()
                self.Purchase_RecordwUI.PR_Description.clear()
                

                # invoice_lists = []
                # for i in Invoice_from_precord.pprecords:
                #     invoice_lists.append(float(i.price ))
                # self.invoice_listtt = sum(invoice_lists)
                # Invoice_from_precord.invoice_total = self.invoice_listtt
                # session.add(Invoice_from_precord)
                # session.commit()

                self.refersh_purshace_invoice_table()
                self.refersh_purchase_Records_table()


            
               
            self.refersh_purchase_Records_table()
            self.Purchase_RecordwUI.PR_table.scrollToBottom()
        except:
            print('error')

   
    def remove_purchase_Records_table(self):
        try:

            row_index = self.Purchase_RecordwUI.PR_table.currentRow()
            cell_content = self.Purchase_RecordwUI.PR_table.item(row_index,0).text() 
        
            with Session(engine) as session:
                statement = select(Purchase_Record).where(Purchase_Record.id == int(cell_content))
                results = session.exec(statement)
                instancepurchase = results.one()


                session.delete(instancepurchase)    
                session.commit()
            self.refersh_purchase_Records_table()
        except:
            print('error')

    def show_PinvoiceBtn(self):
        self.row_indexx =  self.PurchasewUI.Purchase_Table.currentRow()
        self.cell_contentt =  self.PurchasewUI.Purchase_Table.item(self.row_indexx,0).text()


    def refersh_purchase_Records_table(self):
        if self.Rightside.currentIndex() == 9:
            variable = self.HistoryWui.Purchase_Table_history
            self.choosenPRcond = 0
        elif self.wantedID_purchase == 'still not used':

            # self.row_index =  self.PurchasewUI.Purchase_Table.currentRow()
            # self.cell_content =  self.PurchasewUI.Purchase_Table.item(self.row_index,0).text()
            variable = self.Purchase_RecordwUI.PR_table
            self.choosenPRcond = 2
            self.Purchase_RecordwUI.PR_Add.hide()
            self.Purchase_RecordwUI.PR_Save.hide()
            self.Purchase_RecordwUI.PR_Delete.setText("Return Item")
        else:
            variable = self.Purchase_RecordwUI.PR_table
            self.Purchase_RecordwUI.PR_Add.show()
            self.Purchase_RecordwUI.PR_Save.show()
            self.choosenPRcond = 1

        variable.clear()
        self.Purshace_record_Data = self.choose_purchase_Records_data()
        variable.setRowCount(len(self.Purshace_record_Data))
        variable.setColumnCount(6)
        variable.setHorizontalHeaderLabels(['id', 'price','quantity','description','timestamp','invoice_id'])
        variable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.PR_ID = []
        self.PR_price = []
        self.PR_quantity = []
        self.PR_description = []
        self.PR_timestamp = []
        self.PR_invoice_id = []
        
        

        for h in self.Purshace_record_Data:
            self.PR_ID.append(h.id)
            self.PR_price.append(h.price)
            self.PR_quantity.append(h.quantity)
            self.PR_description.append(h.description)
            self.PR_timestamp.append(h.timestamp)
            self.PR_invoice_id.append(h.invoice_id)
        print(self.PR_invoice_id)
          
        for jdx, h in enumerate(self.PR_ID):
            variable.setItem(jdx,0, QtWidgets.QTableWidgetItem(str(h)))
        for jdx,h in enumerate(self.PR_price):
            variable.setItem(jdx,1, QtWidgets.QTableWidgetItem(str(h)))
        for jdx, h in enumerate(self.PR_quantity):
            variable.setItem(jdx,2, QtWidgets.QTableWidgetItem(str(h)))
        for jdx, h in enumerate(self.PR_description):
            variable.setItem(jdx,3, QtWidgets.QTableWidgetItem(str(h)))
        for jdx, h in enumerate(self.PR_timestamp):
            variable.setItem(jdx,4, QtWidgets.QTableWidgetItem(str(h)))
        for jdx, h in enumerate(self.PR_invoice_id):
            variable.setItem(jdx,5, QtWidgets.QTableWidgetItem(str(h)))


            
    def PR_done_btn(self):
        
        self.Purchase_RecordwUI.PR_PhoneNumber.clear()
        self.Purchase_RecordwUI.PR_ProductID.clear()
        print(self.Purchase_RecordwUI.PR_table.rowCount())
        if self.Purchase_RecordwUI.PR_table.rowCount() == 0:
            with Session(engine) as session:
                if self.wantedID_purchase != 'still not used':
                    statement = select(Purchase_invoice).where(Purchase_invoice.id == self.wantedID_purchase)
                    print('choosen')
                else:
                    statement = select(Purchase_invoice).where(Purchase_invoice.id == int(self.cell_contentt))
                results = session.exec(statement)
                instanceinvoice = results.one()
    
    
                session.delete(instanceinvoice)    
                session.commit()
        else:
            try:
                with Session(engine) as session:
                    statement = select(Purchase_invoice).where(Purchase_invoice.id == self.wantedID_purchase)
                    results = session.exec(statement)
                    instanceinvoice = results.one()
                    transaction = Budget_Account(transaction_type= "Withdraw" , amount= instanceinvoice.invoice_total, description= "Purchase", timestamp= instanceinvoice.timestamp)
                    session.add(transaction)           
                    session.commit()
            except:
                pass

        self.wantedID_purchase = 'still not used'
        self.refersh_purshace_invoice_table()

        
    def Precords_save(self):
        if self.wantedID_purchase != 'still not used':
            with Session(engine) as session:
                stat = select(Purchase_invoice).where(Purchase_invoice.id == self.wantedID_purchase)
                res = session.exec(stat)
                Invoice_from_precord = res.one()

                invoice_lists = []
                for i in Invoice_from_precord.pprecords:
                    invoice_lists.append(float(i.price * i.quantity))
                self.invoice_listtt = sum(invoice_lists)
                Invoice_from_precord.invoice_total = self.invoice_listtt
                session.add(Invoice_from_precord)
                session.commit()
        
        self.refersh_purshace_invoice_table()
        self.refersh_purchase_Records_table()

##############################################################
   
    def add_to_purshace_invoice_table(self):
   
        try:   
            self.Purchase_RecordwUI.PR_table.setRowCount(0)
            self.Purchase_RecordwUI.PR_table.setHorizontalHeaderLabels(['id', 'invoice_id','product_id','description','timestamp','qunatity','unit_price','total_price'])

            phonesearch = self.Purchase_RecordwUI.PR_PhoneNumber.text()

            timestamp = datetime.now()
            visible_Reference_Number =  generate(8)
            note_for_purchase_invoice =''




            # to connect the customer to the invoice 
            with Session(engine) as session:
                statement = select(Supplier).where(Supplier.phone_number == phonesearch)
                result = session.exec(statement)
                SupInst = result.first()

            # this is to add the invoices in the database

                PurshaceInvoice_Inst = Purchase_invoice(supplier = SupInst, timestamp =timestamp, visible_Reference_Number= visible_Reference_Number, note= note_for_purchase_invoice,invoice_total=0)
                session.add(PurshaceInvoice_Inst)
                session.commit()




            self.refersh_purshace_invoice_table()
            self.wantedID_purchase  = self.purshase_ID_list[len(self.purshase_ID_list)-1]
            print(self.wantedID_purchase)

            self.PurchasewUI.Purchase_Table.scrollToBottom()
        except:
                print('error')

 
       
 
 
  
    def remove_from_purshace_invoice_table(self):
        try:
           row_index = self.PurchasewUI.Purchase_Table.currentRow()
           cell_content = self.PurchasewUI.Purchase_Table.item(row_index,0).text() 
    
           with Session(engine) as session:
               statement = select(Purchase_invoice).where(Purchase_invoice.id == int(cell_content))
               results = session.exec(statement)
               instanceinvoice = results.one()
               print(instanceinvoice)

    
               session.delete(instanceinvoice)    
               session.commit()
           self.refersh_purshace_invoice_table()
        except:
            print('error')
        
 
 
 
    def choose_product_invoice_data(self):
        print(self.PurchasewUI.Purchase_Search_Bar.text())
        if self.PurchasewUI.Purchase_Search_Bar.text() != "":
            with Session(engine) as session:
                statement = select(Supplier).where(Supplier.phone_number == self.PurchasewUI.Purchase_Search_Bar.text())
                result = session.exec(statement)
                supplier_instance = result.one().pinvoices
                #self.Customerui.Customer_Table.setItem(customer_instance)
                return supplier_instance
        else:
            with Session(engine) as session:
                statment = select(Purchase_invoice)
                result = session.exec(statment)
                all_invoice = result.all()
 
                return all_invoice
        
        
 
 
 
    def refersh_purshace_invoice_table(self):
 
        self.PurchasewUI.Purchase_Table.clear()
        self.Purhase_invoice_data = self.choose_product_invoice_data()
        self.PurchasewUI.Purchase_Table.setRowCount(len(self.Purhase_invoice_data))
        self.PurchasewUI.Purchase_Table.setColumnCount(4)
        self.PurchasewUI.Purchase_Table.setHorizontalHeaderLabels(['id', 'Timestamp','invoice total','Reference number'])
        
        self.PurchasewUI.Purchase_Table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        print(f'the length is {len(self.Purhase_invoice_data)}')
 
         
        self.purshase_ID_list = []
        self.purshase_timestamp_list = []
        self.purshase_total_list= []
        self.purshase_refNum_list = []
 
             
        for j in self.Purhase_invoice_data:
            self.purshase_ID_list.append(j.id)
            self.purshase_timestamp_list.append(j.timestamp)
            self.purshase_total_list.append(j.invoice_total)
            self.purshase_refNum_list.append(j.visible_Reference_Number)

     
 
        for jdx, j in enumerate(self.purshase_ID_list):
            self.PurchasewUI.Purchase_Table.setItem(jdx,0, QtWidgets.QTableWidgetItem(str(j)))
        for jdx, j in enumerate(self.purshase_timestamp_list):
            self.PurchasewUI.Purchase_Table.setItem(jdx,1, QtWidgets.QTableWidgetItem(str(j)))
        for jdx, j in enumerate(self.purshase_total_list):
            self.PurchasewUI.Purchase_Table.setItem(jdx,2, QtWidgets.QTableWidgetItem(str(j)))
        for jdx, j in enumerate(self.purshase_refNum_list):
            self.PurchasewUI.Purchase_Table.setItem(jdx,3, QtWidgets.QTableWidgetItem(str(j)))
        
 
    def edit_purshace_invoice(self):
        try:
            with Session(engine) as session:
            
                row_index =  self.PurchasewUI.Purchase_Table.currentRow()
                column_index=  self.PurchasewUI.Purchase_Table.currentColumn()
                cell_content =  self.PurchasewUI.Purchase_Table.item(row_index,column_index).text()
    
                statement = select(Purchase_invoice).where(Purchase_invoice.id == row_index+1)
                results = session.exec(statement)
                invoice_instance = results.one()
    
    
                if column_index == 0:
                    invoice_instance.id = cell_content  
                elif column_index == 1:
                    invoice_instance.timestamp = cell_content
                elif column_index == 2:
                    invoice_instance.invoice_total = cell_content
                elif column_index== 3:
                    invoice_instance.visible_Reference_Number = cell_content
    
                session.add(invoice_instance)
               
                session.commit()
            
            self.refersh_purshace_invoice_table()
            self.refersh_supplier_table()
        except:
            print('error')


        #def show_invoice_BTN(self)




            
    def make_PI_pdf(self):
        row_index =  self.PurchasewUI.Purchase_Table.currentRow()
        print(row_index)
        cell_content= self.PurchasewUI.Purchase_Table.item(row_index,0).text()
       
        with Session(engine) as session:
            statement = select(Purchase_invoice).where(Purchase_invoice.id == int(cell_content) )
            result = session.exec(statement)
            invoiceInst = result.first()
            precs_in_invoice = invoiceInst.pprecords
            supplier_from_invoice = invoiceInst.supplier
            print(precs_in_invoice)
        
            self.printIdList = []
            self.printDescriptionList = []
            self.printQuantityList = []
            self.printUnitPriceList = []
            self.printTotalPriceList = []
            for i in precs_in_invoice:
                self.printIdList.append(i.id)
                self.printDescriptionList.append(i.pproduct.description)
                self.printQuantityList.append(i.quantity)
                self.printUnitPriceList.append(i.price)
                self.printTotalPriceList.append((i.price)* (i.quantity))

            
        


            data_as_dict = {"Item": self.printIdList ,
                    "description":self.printDescriptionList ,
                    "quantity":self.printQuantityList,
                    "Unit price":self.printUnitPriceList,
                    "Total":self.printTotalPriceList,
                    #"city":city,
                   # "streetadress":street
                }
            pdf = PDF()
            pdf.add_page(format= "a4")
            #pdf.add_page(format= "letter")
            y=10
            pdf.set_text_color(60)
            pdf.set_font("helvetica","B",size=30)
            pdf.set_xy(146,20)
            #pdf.set_draw_color(255,0,0)
            pdf.cell(45,12,"INVOICE",border=0)
            pdf.set_fill_color(215)
            pdf.set_text_color(0)
            pdf.set_font("","B",size=10)
            pdf.set_xy(15,y+50)
            pdf.cell(75,7,"    BILL TO:",fill = True, border= 1)
            pdf.set_font(size=10)
            pdf.set_xy(15,y+60)
            # please dont put all of the supplier's info 
            pdf.multi_cell(40,5,f" [{supplier_from_invoice.id}]\n [{supplier_from_invoice.name}]\n [{supplier_from_invoice.email}]\n [{supplier_from_invoice.phone_number}]\n [{supplier_from_invoice.country}]\n [{supplier_from_invoice.city}]\n [{supplier_from_invoice.street_address}]\n  ")
            pdf.set_font("","B",size=10)
            pdf.set_xy(110,y+50)
            #pdf.set_draw_color(255,0,0)
            pdf.cell(40,7,"DATE:",fill=True,border=1,align="C")
            pdf.ln
            pdf.cell(40,7,"INVOICE #:",fill=True,border=1,align="C")
            pdf.set_font(size=10)
            pdf.set_xy(110,y+58)
            pdf.cell(40,7,f"{invoiceInst.timestamp}",border=1,align="C")
            pdf.ln
            pdf.cell(40,7,f"#{invoiceInst.id}",border=1,align="C")
            pdf.set_xy(100,y+100)
            pdf.create_table(table_data = data_as_dict,title= "",align_header='L', align_data='L', cell_width=[15,70,30,30,30,], x_start=15,  emphasize_style='BIU',emphasize_color=(255,0,0))
            pdf
            #pdf.multi_cell(20,5,f" [{supplier_from_invoice.}]\n [{supplier_from_invoice.}]\n [{supplier_from_invoice.}]\n ")
            pdf.output(f'purchase_invoice_number_{invoiceInst.id}.pdf')
            os.system(f'purchase_invoice_number_{invoiceInst.id}.pdf')



##############################################################
    def choose_Budget_data(self):
        with Session(engine) as session:
            statement = select(Budget_Account)
            ressult = session.exec(statement)
            all_budgets = ressult.all()
            return all_budgets


    def add_to_budget_table(self):
        try:
            TransactionTypeX = self.BudgetWui.BD_combobox.currentText()
            TransactionAmountX = self.BudgetWui.Budget_amount.text()
            TransactionDescriptionX =  self.BudgetWui.Budget_description.text()
            timestamp = self.Ftime
            print('type iss')
            print(TransactionTypeX)



            self.Customerui.Customer_Table.scrollToBottom()

            transaction = Budget_Account(transaction_type= TransactionTypeX, amount= TransactionAmountX, description= TransactionDescriptionX, timestamp= timestamp)

            with Session(engine) as session1:
                session1.add(transaction)
                session1.commit()
            self.refersh_budget_table()
        except:
                print('error')

   
    def remove_from_budget_table(self):
        try:
            h = self.BudgetWui.Budget_Table.currentRow()
            g = self.BudgetWui.Budget_Table.item(h,0).text() 

            with Session(engine) as session:
                statement = select(Budget_Account).where(Budget_Account.transaction_id == int(g))
                results = session.exec(statement)
                instancebudget = results.one()


                session.delete(instancebudget)    
                session.commit()

            self.refersh_budget_table()
        except:
            print('error')



    def refersh_budget_table(self):
        self.BudgetWui.Budget_Table.clear()
        
        self.budget_data = self.choose_Budget_data()
        self.BudgetWui.Budget_Table.setRowCount(len(self.budget_data))
        self.BudgetWui.Budget_Table.setColumnCount(5)
        #self.BudgetWui.Budget_Table.setItem(0,4,fo)


        self.BudgetWui.Budget_Table.setHorizontalHeaderLabels(['id', 'transaction Type','time','Description','Amount'])
        
        self.BudgetWui.Budget_Table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.budget_idList = []
        self.budget_Type = []
        self.budget_amount = []
        self.budget_description = []
        self.Budget_timestamp = []

        
        for j in self.budget_data:
            self.budget_idList.append(j.transaction_id)
            self.budget_Type.append(j.transaction_type)
            self.budget_amount.append(j.amount)
            self.budget_description.append(j.description)
            self.Budget_timestamp.append(j.timestamp)
        print(self.budget_Type)


        for jdx, j in enumerate(self.budget_idList):
            self.BudgetWui.Budget_Table.setItem(jdx,0, QtWidgets.QTableWidgetItem(str(j)))
        for jdx, j in enumerate(self.budget_Type):
            self.BudgetWui.Budget_Table.setItem(jdx,1, QtWidgets.QTableWidgetItem(str(j)))
        for jdx, j in enumerate(self.Budget_timestamp):
            self.BudgetWui.Budget_Table.setItem(jdx,2, QtWidgets.QTableWidgetItem(str(j)))
        for jdx, j in enumerate(self.budget_description):
            self.BudgetWui.Budget_Table.setItem(jdx,3, QtWidgets.QTableWidgetItem(str(j)))
        for jdx, j in enumerate(self.budget_amount):
            self.BudgetWui.Budget_Table.setItem(jdx,4, QtWidgets.QTableWidgetItem(str(j)))


        



    def You_sure(self):
        self.Yousurew.show()

        if self.Rightside.currentIndex() == 1:
            self.Yousurewui.IM_Sure_BTN.clicked.connect(self.remove_from_purshace_invoice_table)
            self.Yousurewui.Cancel_BTN.clicked.connect(self.show_purchase)
            self.Yousurewui.IM_Sure_BTN.clicked.connect(self.show_purchase)

        if self.Rightside.currentIndex() == 2:
            self.Yousurewui.IM_Sure_BTN.clicked.connect(self.remove_from_customer_table)
            self.Yousurewui.Cancel_BTN.clicked.connect(self.Show_customer)
            self.Yousurewui.IM_Sure_BTN.clicked.connect(self.Show_customer)

        elif self.Rightside.currentIndex() == 3:
            self.Yousurewui.IM_Sure_BTN.clicked.connect(self.remove_from_supplier_table)
            self.Yousurewui.Cancel_BTN.clicked.connect(self.Show_supplier)
            self.Yousurewui.IM_Sure_BTN.clicked.connect(self.Show_supplier)

        elif self.Rightside.currentIndex() == 4:
            self.Yousurewui.IM_Sure_BTN.clicked.connect(self.remove_from_invoice_table)
            self.Yousurewui.Cancel_BTN.clicked.connect(self.Show_invoice)
            self.Yousurewui.IM_Sure_BTN.clicked.connect(self.Show_invoice)
        
        elif self.Rightside.currentIndex() == 5:
            self.Yousurewui.IM_Sure_BTN.clicked.connect(self.remove_from_SR_table)
            self.Yousurewui.Cancel_BTN.clicked.connect(self.Show_SalesRecord)
            self.Yousurewui.IM_Sure_BTN.clicked.connect(self.Show_SalesRecord)

        elif self.Rightside.currentIndex() == 6:
            self.Yousurewui.IM_Sure_BTN.clicked.connect(self.remove_from_product_table)
            self.Yousurewui.Cancel_BTN.clicked.connect(self.Show_Products)
            self.Yousurewui.IM_Sure_BTN.clicked.connect(self.Show_Products)

        elif self.Rightside.currentIndex() == 7:
            self.Yousurewui.IM_Sure_BTN.clicked.connect(self.remove_purchase_Records_table)
            self.Yousurewui.Cancel_BTN.clicked.connect(self.Show_Purchase_Record)
            self.Yousurewui.IM_Sure_BTN.clicked.connect(self.Show_Purchase_Record)

        elif self.Rightside.currentIndex() == 8:
            self.Yousurewui.IM_Sure_BTN.clicked.connect(self.remove_from_budget_table)
            self.Yousurewui.Cancel_BTN.clicked.connect(self.Show_Budget_account)
            self.Yousurewui.IM_Sure_BTN.clicked.connect(self.Show_Budget_account)
        
            

            
    def export_invoice(self):
        invoiceCSV = open("Invoices.csv",'w')
        invoiceCSV.write('ID,Invoice time, Discount, Invoice total, Total with tax, Visible refernce number\n')
        for j in self.Invoice_Data:
            self.Invoice_ID_list.append(j.id)
            self.Invoice_timestamp_list.append(j.timestamp)
            self.Invoice_discount_list.append(j.discount_percentage)
            self.Invoice_total_list.append(j.invoice_total)
            self.Invoice_totalWTax_list.append(j.total_with_tax)
            self.Invoice_refNum_list.append(j.visible_Reference_Number)
            invoiceCSV.write(f"{j.id},{j.timestamp},{j.discount_percentage},{j.invoice_total},{j.total_with_tax},{j.visible_Reference_Number}\n")
        invoiceCSV.close()

    def export_purchase_invoice(self):
        PR_CSV_file = open("Purchase Invoices.csv",'w')
        PR_CSV_file.write('ID,Time Stamp , Invoice Total,Visible refernce number\n')
        for j in self.Purhase_invoice_data:
            self.purshase_ID_list.append(j.id)
            self.purshase_timestamp_list.append(j.timestamp)
            self.purshase_total_list.append(j.invoice_total)
            self.purshase_refNum_list.append(j.visible_Reference_Number)
            PR_CSV_file.write(f"{j.id},{j.timestamp},{j.invoice_total},{j.visible_Reference_Number}\n")
        PR_CSV_file.close()

    def export_Customer(self):
        Customer_CSV_file = open("Customer.csv",'w')
        Customer_CSV_file.write('ID,Name , Email,Phone Number,Country, Street\n')
        for j in self.Customer_Data:
            self.idList.append(j.id)
            self.nameList.append(j.name)
            self.email.append(j.email)
            self.phoneNo.append(j.phonenumber)
            self.country.append(j.country)
            self.city.append(j.city)
            self.street.append(j.streetadress)
            Customer_CSV_file.write(f"{j.id},{j.name},{j.email},{j.phonenumber},{j.country},{j.city},{j.streetadress}\n")
        Customer_CSV_file.close()

    def export_Product(self):
        Customer_CSV_file = open("Product.csv",'w')
        Customer_CSV_file.write('ID,Name , Email,Phone Number,Country, Street\n')
        for j in self.Customer_Data:
            self.idList.append(j.id)
            self.nameList.append(j.name)
            self.email.append(j.email)
            self.phoneNo.append(j.phonenumber)
            self.country.append(j.country)
            self.city.append(j.city)
            self.street.append(j.streetadress)
            Customer_CSV_file.write(f"{j.id},{j.name},{j.email},{j.phonenumber},{j.country},{j.city},{j.streetadress}\n")
        Customer_CSV_file.close()

    def export_Sales_history(self):
        Sales_history_CSV_file = open("Sales_Histry.csv",'w')
        Sales_history_CSV_file.write('ID,Invoice_ID , Product_ID,Description,Time, Qunatity, Unit_price,total_price\n')
        for j in self.Sales_records_Data:

            self.idListSR.append(j.id)
            self.invoice_idSR.append(j.invoice_id)
            self.product_idSR.append(j.product_id)
            self.descriptionSR.append(j.description)
            self.qunatitySR.append(j.qunatity)
            self.unit_priceSR.append(j.unit_price)
            self.total_priceSR.append(j.total_price)
            Sales_history_CSV_file.write(f"{j.id},{j.invoice_id},{j.product_id},{j.description},{j.qunatity},{j.unit_price},{j.total_price}\n")
        Sales_history_CSV_file.close()


    def export_purchase_history(self):
        Purchase_history_CSV_file = open("Purchase_Histry.csv",'w')
        Purchase_history_CSV_file.write('ID,price , quantity , Description,Time, Invoice ID\n')
        for j in self.Purshace_record_Data:
            self.PR_ID.append(j.id)
            self.PR_price.append(j.price)
            self.PR_quantity.append(j.quantity)
            self.PR_description.append(j.description)
            self.PR_timestamp.append(j.timestamp)
            self.PR_invoice_id.append(j.invoice_id)
            Purchase_history_CSV_file.write(f"{j.id},{j.price},{j.quantity},{j.description},{j.timestamp},{j.invoice_id}\n")
        Purchase_history_CSV_file.close()
        
    def export_invoice(self):
        invoiceCSV = open("Invoices.csv",'w')
        invoiceCSV.write('ID,Invoice time, Discount, Invoice total, Total with tax, Visible refernce number\n')
        for j in self.Invoice_Data:
            self.Invoice_ID_list.append(j.id)
            self.Invoice_timestamp_list.append(j.timestamp)
            self.Invoice_discount_list.append(j.discount_percentage)
            self.Invoice_total_list.append(j.invoice_total)
            self.Invoice_totalWTax_list.append(j.total_with_tax)
            self.Invoice_refNum_list.append(j.visible_Reference_Number)
            invoiceCSV.write(f"{j.id},{j.timestamp},{j.discount_percentage},{j.invoice_total},{j.total_with_tax},{j.visible_Reference_Number}\n")
        invoiceCSV.close()
        

        

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myApp = Mainapp()
    sys.exit(app.exec_())