#6

import sqlite3

def query(sql,data):
    with sqlite.connect("coffee_shop.db") as db:
        cursor=db.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.execute(sql,data)
        db.commit()
def insert_product_type_data(records):
    sql="insert into ProductType(Description) values(?)"
    for record in records:
        query(sql,record)
        
def insert_product_data(records):
    sql="insert into ProductType(Name,Price,ProductTypeID) values(?,?,?)"
    for record in records:
        query(sql,record)
        
if __name__== "__main__":
    product_type=[("Coffee",),("Tea",),("Cold Drink",)]
    insert_product_type_data(product_types)
    #products=[("Americano",2.0,1),("Mocha",3.5,1),("Green Tea",1.25,2)]
    #insert_product_data(products)
    products=[("Banana",3.25,4),("Lemon Cake",2.15,5)]
    insert_product_data(products)
