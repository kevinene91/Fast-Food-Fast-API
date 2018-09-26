import psycopg2
import os 
from .tables import queries

#create a connection
def create_conn():
	conn = psycopg2.connect(os.getenv('DB_URL'))
	return conn


#Create Database tables
def create_db(): 
    conn = create_conn()
    curr = conn.cursor()
    for query in queries:
        curr.execute(query)

    curr.close()
    conn.commit()
    conn.close()