from typing import Optional
from sqlmodel import Field, Session ,SQLModel, create_engine, select
from datetime import datetime
from enum import Enum
from sqlalchemy import Column
from sqlalchemy_utils import ChoiceType



###############################################################


sqlite_file_name = "database_PROJECT.db"
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
    

class Sales_invoices(SQLModel, table= True):
    id: Optional [int] = Field(default= None, primary_key= True)
    customer_id: Optional [int] = Field(default= None, foreign_key= "customer.id")
    #timestamp: datetime = Field(default_factory=datetime.now(), nullable=False)
    discount_percentage: Optional[int] = 0
    invoice_total: float
    total_with_tax: float
    visible_Reference_Number: int
    note: Optional[str] = None
    URL_to_image: Optional[str] = None



class Products(SQLModel, table= True):
    id: Optional [int] = Field(default= None, primary_key= True)
    description: Optional[str] = None
    base_price: float
    IsTaxable: bool
    quantity: int


class Sales_Records(SQLModel, table= True):
    id: Optional [int] = Field(default= None, primary_key= True) 
    invoice_id: Optional[int] = Field(default=None, foreign_key="sales_invoices.id")
    product_id: Optional[int] = Field(default=None, foreign_key="products.id")
    description:  Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.now(), nullable=False)
    qunatity: int
    unit_price: float 
    total_price: float


class Return_Records(SQLModel, table=True):
    id:  Optional[int] = Field(default=None, primary_key=True)
    invoice_id: Optional[int] = Field(default=None, foreign_key="sales_invoices.id")
    item_id: Optional[int] = Field(default=None, foreign_key="sales_records.id")
    quantity: int
    timestamp:  datetime = Field(default_factory=datetime.now(), nullable=False)

#################################################################


###########################
class Transactiontype(Enum):
    sale = "sale"
    purchase = "purchase"

class Budget_Account(SQLModel, table= True):
    transaction_id: Optional[int] = Field(default=None, primary_key=True)
    transaction_type: Transactiontype = Field(sa_column=Column(ChoiceType(Transactiontype)))
    amount: float
    description:  Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.now(), nullable=False)


###########################


#################################################################

class Suppliers(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name:  Optional[str] = Field(default=None)
    email:  Optional[str] = Field(default=None)
    phone_number: str
    country:  Optional[str] = Field(default=None)
    city:  Optional[str] = Field(default=None)
    street_address:  Optional[str] = Field(default=None)
    fast_delivery_rating: int
    reliability_rating: int
    Note:  Optional[str] = Field(default=None)

class Purchase_invoice(SQLModel, table= True):
    id: Optional[int] = Field(default=None, primary_key=True) 
    timestamp:  datetime = Field(default_factory=datetime.now(), nullable=False)
    invoice_total: float
    visible_Reference_Number: str
    note:  Optional[str] = None
    Supplier_id: Optional[int] = Field(default=None, foreign_key="suppliers.id")

class Purchase_Records(SQLModel, table= True):
    id: Optional[int] = Field(default=None, primary_key=True) 
    price:  float
    quantity: int
    description:  Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.now(), nullable=False)
    invoice_id: Optional[int] = Field(default=None, foreign_key="purchase_invoice.id")

################################################################

#customer= Customer(name="Tariq",email="tariqzr1234@gmail.com",phonenumber="0530162615")
#sales_invoices= Sales_invoices(invoice_total=200.93, total_with_tax= 220.50,visible_Reference_Number=6)
# sales_records = Sales_Records()
# return_records= Return_Records()
# product= Products()
# budget= Budget_Account()
# suppliers= Suppliers()
# purchase_invoice = Purchase_invoice()
# purchase_record = Purchase_Records()


################################################################




  


#with Session(engine) as session:
#     session.add(customer)
      #session.add(sales_invoices)
#     # session.add(sales_records)
#     # session.add(return_records)
#     # session.add(product)
#     # session.add(budget)
#     # session.add(suppliers)
#     # session.add(purchase_invoice)
#     # session.add(purchase_record)
#     session.commit()

# #if __name__ == "__main__":