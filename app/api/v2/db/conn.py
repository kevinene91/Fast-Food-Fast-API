import psycopg2
import os 
from .tables import queries, to_drop
from flask import current_app
from flask_bcrypt import Bcrypt
from psycopg2.extras import RealDictCursor
from app.bcrypt import BCRYPT

password = BCRYPT.generate_password_hash('testme').decode('utf-8')


# create a connection
def create_conn():
    url = current_app.config.get('POSTGRES_DATABASE_URI')
    try:
        conn = psycopg2.connect(url)
        return conn
    except psycopg2.DatabaseError as e:
        return {'message': '{}'.format(e)}


def save_test_user():
        conn = create_conn()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        try:
            query = """INSERT INTO users (user_name, email, password, role)
             values(%s, %s, %s, %s)"""
            cursor.execute(query, ('testuser', 'testuser@gmail.com', 
                                   password, 2))
            conn.commit()
            data = cursor.fetchone()
            cursor.close()   
        except psycopg2.DatabaseError as e:
            return {'message': '{}'.format(e)}


def check_if_inserted_admin():
    conn, response = create_conn(), None
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    query = """
        select exists(select 1 from users where email=testuser@gmail.com)
    """
    cursor.execute(query)
    conn.commit()


def save_test_meal():
        conn = create_conn()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        try:
            query = "INSERT INTO meals (meal_name, price) values(%s, %s)"
            cursor.execute(query, ('mayai', 100))
            conn.commit()
            data = cursor.fetchone()
            cursor.close()   
        except psycopg2.DatabaseError as e:
            return {'message': '{}'.format(e)}


def save_test_order():
        conn = create_conn()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        try:
            query = "INSERT INTO orders (meal_id, quantity) values(%s, %s)"
            cursor.execute(query, (1, 3))
            conn.commit()
            data = cursor.fetchone()
            cursor.close()
        except psycopg2.DatabaseError as e:
            return {'message': '{}'.format(e)}


# create 
def user_test_data():
    save_test_user()
    save_test_meal()
    save_test_order()


# Create Database tables
def create_db(): 
    conn = create_conn()
    curr = conn.cursor()
    conn.autocommit = False
    for query in queries:
        curr.execute(query)
        conn.commit()
    # if check_if_inserted_admin():
    return conn


# drop table for tests
def drop_db():
    conn = create_conn()
    curr = conn.cursor()
    try:
        for query in to_drop:
            curr.execute(query)
        curr.close()
        conn.commit()
    except psycopg2.DatabaseError as e:
        return "message :{}".e