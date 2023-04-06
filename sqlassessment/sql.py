import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    # password = 'sqlrootpassword',
    database = 'customers'
)

cursor = db.cursor()

# cursor.execute("CREATE DATABASE customers")
# cursor.execute("CREATE TABLE customer_info(customer_name VARCHAR(255), customer_number REVARCHAR(200))")
# cursor.execute("SHOW DATABASES")
# for x in cursor:
#     print(x)
# sql = 'INSERT INTO customer_info(customer_name, customer_number VALUE ('john', '12103909') )
# cursor.execute(sql)
# cursor.execute("ALTER TABLE customer_info ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")


cursor.execute("SELECT * FROM customer_info")
result = cursor.fetchall()

for x in result:
    print(x)
# db.commit()