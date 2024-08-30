import mysql.connector
import pandas as pd

# Replace 'root', '', 'localhost', and 'ecommerce' with your actual credentials
connection = mysql.connector.connect(
    user='root',
    password='nitish1234',
    host='localhost',
    database='ecommerce'
)

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Query data from the 'customer' table
cursor.execute('SELECT * FROM customer')
customer_data = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])

# Query data from the 'product' table
cursor.execute('SELECT * FROM product')
product_data = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])

# Query data from the 'order_details' table
cursor.execute('SELECT * FROM order_details')
order_data = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])

# Printing first 5 records from each table
print("Customer Data:")
print(customer_data.head(), "\n")

print("Product Data:")
print(product_data.head(), "\n")

print("Order Details Data:")
print(order_data.head(), "\n")

# Close the cursor and connection
cursor.close()
connection.close()
