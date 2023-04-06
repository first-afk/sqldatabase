import mysql.connector

class PollingUnitDb:
    def __init__(self, dbname, table):
        self.dbname = dbname
        self.table = table
        self.db = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'password'
        )

        self.cursor = self.db.cursor()
        self.cursor.execute(f'CREATE DATABASE IF NOT EXISTS {dbname}')
        self.cursor.execute(f'USE {dbname}')

    def query_db(self, column = '*'):
        self.cursor.execute(f'SELECT {column} from {self.table}')
        self.cursor.fetchall()
        return [f"{value}\n" for value in self.cursor]
        
    def create_table(self):
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.table} (id INTEGER PRIMARY KEY, state VARCHAR(255), polling_unit VARCHAR(255), vote INTEGER)")

    def insert_records(self, id, state, polling_unit, votes):
        values = id, state, polling_unit, votes
        self.cursor.execute(f"INSERT INTO {self.table} (id, state,polling_unit, vote) VALUE (%s, %s, %s, %s)", values)
        self.db.commit()
        
    def __del__(self):
        self.db.close()

def generate_report():
    INEC = PollingUnitDb('polling_unit', 'polling')
    INEC.create_table()
    INEC.insert_records(2, 'Lagos', 'Ikeja', 70)
    INEC.insert_records(3, 'Delta', 'Asaba', 260)
    INEC.insert_records(4, 'Rivers', 'PortHarcout', 150)

    with open('report.txt', 'w') as f:
        f.writelines(INEC.query_db())

def main():
    generate_report()


main()
    