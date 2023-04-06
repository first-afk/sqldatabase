import mysql.connector

class Database:
    def __init__(self, db_name):
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'rootpassword'
        )
        self.cursor = self.conn.cursor()
        self.cursor.execute(f'CREATE TABLE IF EXISTS {db_name}')
    
    def create_table(self):
        self.cursor.execute('''CREATE TABLE RESULT
                           (ID INT PRIMARY KEY NOT NULL,
                            STATE TEXT NOT NULL,
                            POLLING_UNIT TEXT NOT NULL,
                            VOTES INT NOT NULL);''')
        self.conn.commit()
    
    def insert_record(self, id, state, polling_unit, votes):
        self.cursor.execute(f"INSERT INTO RESULT (ID, STATE, POLLING_UNIT, VOTES) VALUES ({id}, '{state}', '{polling_unit}', {votes})")
        self.conn.commit()
    
    def execute_query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def __del__(self):
        self.conn.close()


def generate_report(database):
    query = '''
            SELECT STATE, SUM(VOTES) as TOTAL_VOTES
            FROM RESULT
            GROUP BY STATE
            ORDER BY TOTAL_VOTES DESC;
            '''
    rows = database.execute_query(query)
    
    with open('report.txt', 'w') as f:
        f.write('STATE\t\tTOTAL VOTES\n')
        f.write('--------------------------------\n')
        for row in rows:
            state = row[0]
            total_votes = row[1]
            f.write(f'{state}\t\t{total_votes}\n')


if __name__ == '__main__':
    database = Database('voting.db')
    database.create_table()
    
    database.insert_record(1, 'Lagos', 'Polling Unit A', 100)
    database.insert_record(2, 'Lagos', 'Polling Unit B', 200)
    database.insert_record(3, 'Abuja', 'Polling Unit C', 150)
    database.insert_record(4, 'Abuja', 'Polling Unit D', 300)
    
    generate_report(database)
    
    del database


    a = 1, 3, 4, 5, 6 
    print(a)