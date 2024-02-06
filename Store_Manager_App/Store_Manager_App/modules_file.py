from typing import Optional
from sqlmodel import Field, Session ,SQLModel, create_engine, select, Relationship
from datetime import datetime,date
from enum import Enum
from sqlalchemy import Column
# from sqlalchemy_utils import ChoiceType
from time import time



###############################################################


sqlite_file_name = "database_fall22.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url)


class Customer(SQLModel, table= True):
    id: Optional [int] = Field(default= None, primary_key= True)
    name: str = Field(default= None)
    email: Optional[str] = None
    phonenumber: str 
    country: Optional[str] = None
    city: Optional[str] = None
    streetadress: Optional[str] = Field(default= None)

    # these are the invoices that connect to one customer
    invoices: Optional['Sales_invoice'] = Relationship(back_populates= 'customer')
    

class Sales_invoice(SQLModel, table= True):
    id: Optional [int] = Field(default= None, primary_key= True)
    customer_id: Optional [int] = Field(default= None, foreign_key= "customer.id")
    timestamp: datetime
    discount_percentage: Optional[int] = 0
    invoice_total: Optional[float]
    total_with_tax: Optional[float]
    visible_Reference_Number: Optional[str]
    note: Optional[str] = None
    URL_to_image: Optional[str] = Field(default= None)

    #this is the customer connected to this invoice 
    customer: Optional[Customer] = Relationship(back_populates= 'invoices')

    records: Optional['Sales_Record'] = Relationship(back_populates= 'invoice')
    return_records :Optional['Return_Record'] = Relationship(back_populates= 'invoice')



class Sales_Record(SQLModel, table= True):
    id: Optional [int] = Field(default= None, primary_key= True) 
    invoice_id: Optional[int] = Field(default=None, foreign_key="sales_invoice.id")
    product_id: Optional[int] = Field(default=None, foreign_key="product.id")
    description:  Optional[str] = None
    timestamp: datetime 
    qunatity: Optional[int]
    unit_price: Optional[float] = Field(default= None)
    total_price: Optional[float] = Field(default= None)

    #sales_record: Optional['Return_Record'] = Relationship(back_populates= 'return_record_item_id_relation')

    invoice : Optional[Sales_invoice] = Relationship(back_populates= 'records')
    
    product: Optional['Product'] = Relationship(back_populates= 'records')


class Product(SQLModel, table= True):
    description: Optional[str] = None
    base_price: float
    IsTaxable: Optional[bool]
    quantity: int

    id: Optional [int] = Field(default= None, primary_key= True)
    records: Optional[Sales_Record] = Relationship(back_populates= 'product')
    precords: Optional['Purchase_Record'] = Relationship(back_populates= 'pproduct')




class Return_Record(SQLModel, table=True):
    id:  Optional[int] = Field(default=None, primary_key=True)
    quantity: int
    timestamp:  datetime 

    item_id: Optional[int] = Field(default=None, foreign_key="sales_record.id")
    #return_record_item_id_relation: Optional[Sales_Record] = Relationship(back_populates= 'sales_record')

    invoice_id: Optional[int] = Field(default=None, foreign_key="sales_invoice.id")
    invoice: Optional[Sales_invoice] = Relationship(back_populates= 'return_records')


#################################################################


###########################
class Transactiontype(Enum):
    Deposit = "Deposit"
    Withdraw = "Withdraw"

class Budget_Account(SQLModel, table= True):
    transaction_id: Optional[int] = Field(default=None, primary_key=True)
    transaction_type: str #= Field(sa_column=Column(ChoiceType(Transactiontype)))
    amount: float
    description:  Optional[str] = None
    timestamp: datetime 


###########################


#################################################################

class Supplier(SQLModel, table=True):
    name:  Optional[str] = Field(default=None)
    email:  Optional[str] = Field(default=None)
    phone_number: str
    country:  Optional[str] = Field(default=None)
    city:  Optional[str] = Field(default=None)
    street_address:  Optional[str] = Field(default=None)
    fast_delivery_rating: int
    reliability_rating: int
    Note:  Optional[str] = Field(default=None)

    id: Optional[int] = Field(default=None, primary_key=True)
    pinvoices: Optional['Purchase_invoice'] = Relationship(back_populates= 'supplier')


class Purchase_invoice(SQLModel, table= True):
    id: Optional[int] = Field(default=None, primary_key=True) 
    Supplier_id: Optional[int] = Field(default=None, foreign_key="supplier.id")
    timestamp:  datetime 
    invoice_total: float
    visible_Reference_Number: str
    note:  Optional[str] = None 


    supplier: Optional['Supplier'] = Relationship(back_populates= 'pinvoices')
    pprecords: Optional['Purchase_Record'] = Relationship(back_populates= 'pinvoice')

class Purchase_Record(SQLModel, table= True):
    id: Optional[int] = Field(default=None, primary_key=True) 
    invoice_id: Optional[int] = Field(default=None, foreign_key="purchase_invoice.id")
    product_id: Optional[int] = Field(default=None, foreign_key="product.id")
    price:  Optional[float]
    quantity: Optional[int]
    description:  Optional[str] = None
    timestamp: datetime 

    pinvoice: Optional['Purchase_invoice'] = Relationship(back_populates= 'pprecords')
    pproduct: Optional[Product] = Relationship(back_populates='precords')



def create_db_and_tables():
    SQLModel.metadata.create_all(engine)



if __name__ == "__main__":
    create_db_and_tables()
