from tkinter import *
from PIL import ImageTk, Image
import mysql.connector
import csv
from tkinter import ttk



root = Tk()
root.title('crm tool')
root.geometry("400x600")


mydb = mysql.connector.connect(
        host = "localhost",
        user = "shruti",
        passwd = "shruti0912",
        database = "test",
    )

#print(mydb)

my_cursor = mydb.cursor()

#my_cursor.execute("CREATE DATABASE test")


#my_cursor.execute("SHOW DATABASES")import mysql.connector

#for db in my_cursor:

#my_cursor.execute("DROP TABLE customers")

my_cursor.execute("CREATE TABLE IF NOT EXISTS customers (first_name VARCHAR(255), \
    last_name VARCHAR(255), \
    pincode INT(10), \
    price_paid DECIMAL(10, 2), \
    user_id INT AUTO_INCREMENT PRIMARY KEY)")


#my_cursor.execute("ALTER TABLE customers ADD   (\
    #email VARCHAR(255), \
    #address_1 VARCHAR(255), \
    #address_2 VARCHAR(255), \
    #city VARCHAR(50), \
    #state VARCHAR(50), \
    #country VARCHAR(255), \
    #phone VARCHAR(255), \
    #payment_method VARCHAR(50), \
    #discount_code VARCHAR(255))")

#my_cursor.execute("SELECT * FROM customers")
#print(my_cursor.description)

#for thing in my_cursor.description:
    #print(thing)

def clear_fields():
    first_name_box.delete(0, END)
    last_name_box.delete(0, END)
    address1_box.delete(0, END)
    address2_box.delete(0, END)
    city_box.delete(0, END)
    state_box.delete(0, END)
    pincode_box.delete(0, END)
    country_box.delete(0, END)
    phone_box.delete(0, END)
    email_box.delete(0, END)
    payment_method_box.delete(0, END)
    discount_code_box.delete(0, END)
    price_paid_box.delete(0, END)

def add_customer():
    sql_command= "INSERT INTO customers (first_name, last_name, pincode, price_paid, email, address_1, address_2, city, state, country, phone, payment_method, discount_code) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (first_name_box.get(), last_name_box.get(), pincode_box.get(), price_paid_box.get(), email_box.get(), address1_box.get(), address2_box.get(), city_box.get(), state_box.get(), country_box.get(), phone_box.get(), payment_method_box.get(), discount_code_box.get())
    my_cursor.execute(sql_command, values)

    mydb.commit()

    clear_fields()

def write_to_csv(result):
    with open('customers.csv', 'a', newline='') as f:
        w = csv.writer(f, dialect='excel')
        for record in result:
            w.writerow(record)

def search_customer():
    search_customers = Tk()
    search_customers.title("Search Customers")
    search_customers.geometry("1100x600")

    def update():
        sql_command = """UPDATE customers SET first_name = %s, last_name = %s, pincode = %s, price_paid = %s, email = %s, address_1 = %s, address_2 = %s, city = %s, state = %s, country = %s, phone = %s, payment_method = %s, discount_code = %s WHERE user_id = %s"""
        

        first_name = first_name_box2.get()
        last_name = last_name_box2.get()
        pincode = pincode_box2.get()
        price_paid = price_paid_box2.get()
        email = email_box2.get()
        address_1 = address1_box2.get()
        address_2 = address2_box2.get()
        city = city_box2.get()
        state = state_box2.get()
        country = country_box2.get()
        phone = phone_box2.get()
        payment_method = payment_method_box2.get()
        discount_code = discount_code_box2.get()


        id_value = id_box2.get()
        inputs = (first_name, last_name, pincode, price_paid, email, address_1, address_2, city, state, country, phone, payment_method, discount_code, id_value)
        
        my_cursor.execute(sql_command, inputs)
        mydb.commit()

        search_customers.destroy()

    def edit_now(id, index):
        sql2 = "SELECT * FROM customers WHERE user_id = %s"
        name2 = (id, )
        result2 = my_cursor.execute(sql2, name2)
        result2 = my_cursor.fetchall()
        index +=1
        
        first_name_label = Label(search_customers, text="First Name").grid(row=index+1, column=0, sticky=W, padx=10)
        last_name_label = Label(search_customers, text= "Last Name").grid(row=index+2, column=0, sticky=W, padx=10)
        address1_label = Label(search_customers, text= "Address 1").grid(row=index+3, column=0, sticky=W, padx=10)
        address2_label = Label(search_customers, text= "Address 2").grid(row=index+4, column=0, sticky=W, padx=10)
        city_label = Label(search_customers, text= "City").grid(row=index+5, column=0, sticky=W, padx=10)
        state_label = Label(search_customers, text= "State").grid(row=index+6, column=0, sticky=W, padx=10)
        pincode_label = Label(search_customers, text= "Pincode").grid(row=index+7, column=0, sticky=W, padx=10)
        country_label = Label(search_customers, text= "Country").grid(row=index+8, column=0, sticky=W, padx=10)
        phone_label = Label(search_customers, text= "Phone Number").grid(row=index+9, column=0, sticky=W, padx=10)
        email_label = Label(search_customers, text= "Email Address").grid(row=index+10, column=0, sticky=W, padx=10)
        #username_label = Label(search_customers, text= "Username").grid(row=index+11, column=0, sticky=W, padx=10)
        payment_method_label = Label(search_customers, text= "Payment Method").grid(row=index+12, column=0, sticky=W, padx=10)
        discount_code_label = Label(search_customers, text= "Discount Code").grid(row=index+13, column=0, sticky=W, padx=10)
        price_paid_label = Label(search_customers, text= "Price Paid").grid(row=index+14, column=0, sticky=W, padx=10)
        id_label = Label(search_customers, text="User ID").grid(row=index+15, column=0, sticky=W, padx=10)

        global first_name_box2
        first_name_box2 = Entry(search_customers)
        first_name_box2.grid(row=index+1, column=1, pady=10)
        first_name_box2.insert(0, result2[0][0])


        global last_name_box2
        last_name_box2 = Entry(search_customers)
        last_name_box2.grid(row=index+2, column=1, pady=5)
        last_name_box2.insert(0, result2[0][1])

        global address1_box2
        address1_box2 = Entry(search_customers)
        address1_box2.grid(row=index+3, column=1, pady=5)
        address1_box2.insert(0, result2[0][6])

        global address2_box2 
        address2_box2 = Entry(search_customers)
        address2_box2.grid(row=index+4, column=1, pady=5)
        address2_box2.insert(0, result2[0][7])

        global city_box2
        city_box2 = Entry(search_customers)
        city_box2.grid(row=index+5, column=1, pady=5)
        city_box2.insert(0, result2[0][8])

        global state_box2
        state_box2 = Entry(search_customers)
        state_box2.grid(row=index+6, column=1, pady=5)
        state_box2.insert(0, result2[0][9])

        global pincode_box2
        pincode_box2 = Entry(search_customers)
        pincode_box2.grid(row=index+7, column=1, pady=5)
        pincode_box2.insert(0, result2[0][2])

        global country_box2
        country_box2 = Entry(search_customers)
        country_box2.grid(row=index+8, column=1, pady=5)
        country_box2.insert(0, result2[0][10])

        global phone_box2
        phone_box2 = Entry(search_customers)
        phone_box2.grid(row=index+9, column=1, pady=5)
        phone_box2.insert(0, result2[0][11])
        

        global email_box2
        email_box2 = Entry(search_customers)
        email_box2.grid(row=index+10, column=1, pady=5)
        email_box2.insert(0, result2[0][5])

        global payment_method_box2
        payment_method_box2 = Entry(search_customers)
        payment_method_box2.grid(row=index+12, column=1, pady=5)
        payment_method_box2.insert(0, result2[0][12])

        global discount_code_box2
        discount_code_box2 = Entry(search_customers)
        discount_code_box2.grid(row=index+13, column=1, pady=5)
        discount_code_box2.insert(0, result2[0][13])

        global price_paid_box2
        price_paid_box2 = Entry(search_customers)
        price_paid_box2.grid(row=index+14, column=1, pady=5)
        price_paid_box2.insert(0, result2[0][3])

        global id_box2
        id_box2 = Entry(search_customers)
        id_box2.grid(row=index+15, column=1, pady=5)
        id_box2.insert(0, result2[0][4])

        save_record = Button(search_customers, text="Update Record", command=update)
        save_record.grid(row=index+16, column=0, pady=10)
       


    def search_now():
        selected = drop.get()
        sql = ""
        if selected == "Search by...":
            test = Label(search_customers, text="Hey! You forgot to pick")
            test.grid(row=2, column=0)
        if selected == "Last Name":
            sql = "SELECT * FROM customers WHERE last_name = %s"
            
        if selected == "Email Address":
            sql = "SELECT * FROM customers WHERE email = %s"
            
        if selected == "Customer ID":
            sql = "SELECT * FROM customers WHERE user_id = %s"
            
        if selected == "First Name":
            sql = "SELECT * FROM customers WHERE first_name = %s"
            
        if selected == "Pincode":
            sql = "SELECT * FROM customers WHERE pincode = %s"


        searched = search_box.get()
        sql = "SELECT * FROM customers WHERE last_name = %s"
        name = (searched, )
        result = my_cursor.execute(sql, name)
        result = my_cursor.fetchall()

        if not result:
           result = "Record Not Found..."
           searched_label = Label(search_customers, text=result)
           searched_label.grid(row=2, column=0)

        else:
            for index, x in enumerate(result):
                num = 0
                index += 2
                id_reference = str(x[4])
                edit_button = Button(search_customers, text="Edit", command=lambda: edit_now(id_reference, index))
                edit_button.grid(row=index, column=num)
                for y in x:
                    searched_label = Label(search_customers, text=y)
                    searched_label.grid(row=index, column=num+1)
                    num +=1
            csv_button = Button(search_customers, text="Save To Excel", command=lambda: write_to_csv(result))
            csv_button.grid(row=index+1, column=0)

        #searched_label = Label(search_customers, text=result)
        #searched_label.grid(row=3, column=0, padx=10, columnspan=2)
        

    search_box = Entry(search_customers)
    search_box.grid(row=0, column=1, padx=10, pady=10)

    search_box_label = Label(search_customers, text="Search ")
    search_box_label.grid(row=0, column=0, padx=10, pady=10)

    search_button = Button(search_customers, text="Search Customers", command=search_now)
    search_button.grid(row=1, column=0, padx=10)

    drop = ttk.Combobox(search_customers, value=["Search by...", "Last Name", "Email Address", "Customer ID", "First Name", "Pincode"])
    drop.current(0)
    drop.grid(row=0, column=2)


def list_customers():
    list_customer_query = Tk()
    list_customer_query.title("List All Customers")
    list_customer_query.geometry("800x600")

    my_cursor.execute("SELECT * FROM customers")
    result = my_cursor.fetchall()
    for index, x in enumerate(result):
        num = 0
        for y in x:
            lookup_label = Label(list_customer_query, text=y)
            lookup_label.grid(row=index, column=num)
            num +=1

    csv_button = Button(list_customer_query, text="Save To Excel", command=lambda: write_to_csv(result))
    csv_button.grid(row=index+1, column=0)
    
#CREATE A LABEL
title_label = Label(root, text="test customer database", font=("Helvetica 16"))
title_label.grid(row=0, column=0, columnspan=2, pady=10)    

first_name_label = Label(root, text="First Name").grid(row=1, column=0, sticky=W, padx=10)
last_name_label = Label(root, text= "Last Name").grid(row=2, column=0, sticky=W, padx=10)
address1_label = Label(root, text= "Address 1").grid(row=3, column=0, sticky=W, padx=10)
address2_label = Label(root, text= "Address 2").grid(row=4, column=0, sticky=W, padx=10)
city_label = Label(root, text= "City").grid(row=5, column=0, sticky=W, padx=10)
state_label = Label(root, text= "State").grid(row=6, column=0, sticky=W, padx=10)
pincode_label = Label(root, text= "Pincode").grid(row=7, column=0, sticky=W, padx=10)
country_label = Label(root, text= "Country").grid(row=8, column=0, sticky=W, padx=10)
phone_label = Label(root, text= "Phone Number").grid(row=9, column=0, sticky=W, padx=10)
email_label = Label(root, text= "Email Address").grid(row=10, column=0, sticky=W, padx=10)
#username_label = Label(root, text= "Username").grid(row=11, column=0, sticky=W, padx=10)
payment_method_label = Label(root, text= "Payment Method").grid(row=12, column=0, sticky=W, padx=10)
discount_code_label = Label(root, text= "Discount Code").grid(row=13, column=0, sticky=W, padx=10)
price_paid_label = Label(root, text= "Price Paid").grid(row=14, column=0, sticky=W, padx=10)


first_name_box = Entry(root)
first_name_box.grid(row=1, column=1)
last_name_box = Entry(root)
last_name_box.grid(row=2, column=1, pady=5)
address1_box = Entry(root)
address1_box.grid(row=3, column=1, pady=5)
address2_box = Entry(root)
address2_box.grid(row=4, column=1, pady=5)
city_box = Entry(root)
city_box.grid(row=5, column=1, pady=5)
state_box = Entry(root)
state_box.grid(row=6, column=1, pady=5)
pincode_box = Entry(root)
pincode_box.grid(row=7, column=1, pady=5)
country_box = Entry(root)
country_box.grid(row=8, column=1, pady=5)
phone_box = Entry(root)
phone_box.grid(row=9, column=1, pady=5)
email_box = Entry(root)
email_box.grid(row=10, column=1, pady=5)
payment_method_box = Entry(root)
payment_method_box.grid(row=12, column=1, pady=5)
discount_code_box = Entry(root)
discount_code_box.grid(row=13, column=1, pady=5)
price_paid_box = Entry(root)
price_paid_box.grid(row=14, column=1, pady=5)


add_customer_button = Button(root, text="Add Customer To Database", command=add_customer)
add_customer_button.grid(row=15, column=0, pady=10)
clear_fields_button = Button(root, text="Clear Fields", command=clear_fields)
clear_fields_button.grid(row=15, column=1)
list_customers_button = Button(root, text="List Customer", command=list_customers)
list_customers_button.grid(row=16, column=0, sticky=S, padx=10)
search_customers_button = Button(root, text="Search/Edit Customers", command=search_customer)
search_customers_button.grid(row=16, column=1, sticky=W, padx=10)


root.mainloop()








































































    
        
        
        
            

