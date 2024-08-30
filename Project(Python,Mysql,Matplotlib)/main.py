import mysql.connector
import random
from datetime import datetime, timedelta
from faker import Faker

# Initialize Faker
fake = Faker()

# Establish a connection to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="nitish1234",
    database="ecommerce"
)

# Create a cursor object
cursor = db.cursor()

# Function to generate random data
def generate_data():
    customers = []
    products = []
    orders = []

    # Define the 15 unique cities
    cities = [
        "New York", "Los Angeles", "Chicago", "Houston", "Phoenix",
        "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose",
        "Austin", "Jacksonville", "San Francisco", "Columbus", "Indianapolis"
    ]

    # Define categories and sub-categories
    categories = {
        "Electronics": ["Smartphones", "Laptops", "Cameras", "Headphones", "Tablets"],
        "Home Appliances": ["Refrigerators", "Microwaves", "Washing Machines", "Air Conditioners", "Vacuum Cleaners"],
        "Fashion": ["Clothing", "Footwear", "Accessories", "Jewelry", "Handbags"],
        "Books": ["Fiction", "Non-Fiction", "Comics", "Educational", "Biographies"],
        "Beauty": ["Skincare", "Makeup", "Hair Care", "Fragrances", "Personal Care"],
        "Sports": ["Fitness Equipment", "Outdoor Gear", "Sportswear", "Footwear", "Accessories"],
        "Toys": ["Action Figures", "Dolls", "Educational Toys", "Puzzles", "Board Games"],
        "Automotive": ["Car Accessories", "Motorcycle Accessories", "Car Care", "Tools", "Spare Parts"],
        "Groceries": ["Beverages", "Snacks", "Cooking Essentials", "Dairy Products", "Personal Care"],
        "Furniture": ["Living Room", "Bedroom", "Office Furniture", "Outdoor Furniture", "Storage"]
    }

    for i in range(1, 501):
        # Generate customer data using Faker
        customer_id = f"CUST{i:03}"
        name = fake.name()
        city = random.choice(cities)  # Randomly select from the predefined list of cities
        email = fake.email()
        phone_no = fake.numerify('###-###-####')  # Generate phone number in the format '123-456-7890'
        address = fake.address().replace('\n', ', ')
        pin_code = random.randint(100000, 999999)
        customers.append((customer_id, name, city, email, phone_no, address, pin_code))

        # Generate product data with realistic categories and sub-categories
        product_id = f"PROD{i:03}"
        category = random.choice(list(categories.keys()))
        sub_category = random.choice(categories[category])
        product_name = f"{sub_category} {i}"
        original_price = round(random.uniform(10.0, 1000.0), 2)
        selling_price = round(original_price * random.uniform(0.5, 0.9), 2)
        stock = random.randint(1, 100)
        products.append((product_id, product_name, category, sub_category, original_price, selling_price, stock))

        # Generate order details data
        order_id = i
        product_index = random.randint(0, len(products) - 1)  # Ensure valid index
        quantity = random.randint(1, 10)
        total_price = products[product_index][5] * quantity
        payment_mode = random.choice(["Credit Card", "Debit Card", "Net Banking", "Cash On Delivery"])
        order_date = datetime.now() - timedelta(days=random.randint(1, 365))
        order_status = random.choice(["Pending", "Shipped", "Delivered", "Cancelled"])
        orders.append((order_id, customer_id, products[product_index][0], quantity, total_price, payment_mode, order_date, order_status))

    return customers, products, orders

# Insert data into tables
def insert_data(cursor, customers, products, orders):
    insert_customer_query = """
    INSERT INTO customer (customer_id, name, city, email, phone_no, address, pin_code)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    insert_product_query = """
    INSERT INTO product (product_id, product_name, category, sub_category, original_price, selling_price, stock)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    insert_order_details_query = """
    INSERT INTO order_details (order_id, customer_id, product_id, quantity, total_price, payment_mode, order_date, order_status)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    cursor.executemany(insert_customer_query, customers)
    cursor.executemany(insert_product_query, products)
    cursor.executemany(insert_order_details_query, orders)

    db.commit()

# Generate data
customers, products, orders = generate_data()

# Insert the data into the tables
try:
    insert_data(cursor, customers, products, orders)
    print("500 rows inserted into each table successfully.")
except mysql.connector.Error as err:
    print(f"Error: {err}")

# Close the cursor and the connection
cursor.close()
db.close()
