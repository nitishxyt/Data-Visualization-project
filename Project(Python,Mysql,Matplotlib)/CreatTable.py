import mysql.connector

# Establish a connection to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="nitish1234",
    database="ecommerce"
)

# Create a cursor object
cursor = db.cursor()

# SQL queries to create tables
create_customer_table = """
CREATE TABLE `customer` (
    `customer_id` varchar(10) NOT NULL,
    `name` varchar(100) NOT NULL,
    `city` varchar(65) NOT NULL,
    `email` varchar(45) NOT NULL,
    `phone_no` varchar(15) NOT NULL,
    `address` varchar(100) NOT NULL,
    `pin_code` int NOT NULL,
    PRIMARY KEY (`customer_id`)
);
"""

create_product_table = """
CREATE TABLE `product` (
    `product_id` varchar(10) NOT NULL,
    `product_name` varchar(100) NOT NULL,
    `category` varchar(65) NOT NULL,
    `sub_category` varchar(45) NOT NULL,
    `original_price` double NOT NULL,
    `selling_price` double NOT NULL,
    `stock` int NOT NULL,
    PRIMARY KEY (`product_id`)
);
"""

create_order_details_table = """
CREATE TABLE `order_details` (
    `order_id` int NOT NULL AUTO_INCREMENT,
    `customer_id` varchar(10) NOT NULL,
    `product_id` varchar(10) NOT NULL,
    `quantity` double NOT NULL,
    `total_price` double NOT NULL,
    `payment_mode` varchar(60) NOT NULL,
    `order_date` datetime DEFAULT NULL,
    `order_status` varchar(20) NOT NULL,
    PRIMARY KEY (`order_id`),
    KEY `customer_id` (`customer_id`),
    KEY `product_id` (`product_id`),
    CONSTRAINT `order_details_ibfk_1` FOREIGN KEY (`customer_id`)
        REFERENCES `customer` (`customer_id`),
    CONSTRAINT `order_details_ibfk_2` FOREIGN KEY (`product_id`)
        REFERENCES `product` (`product_id`)
);
"""

# Execute the SQL queries
try:
    cursor.execute(create_customer_table)
    cursor.execute(create_product_table)
    cursor.execute(create_order_details_table)
    print("Tables created successfully.")
except mysql.connector.Error as err:
    print(f"Error: {err}")

# Close the cursor and the connection
cursor.close()
db.close()
