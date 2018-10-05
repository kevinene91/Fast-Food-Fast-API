from ..db.conn import create_conn
import psycopg2
from flask_bcrypt import Bcrypt
from psycopg2.extras import RealDictCursor
from app.bcrypt import BCRYPT


class UserModel:
    Admin = 2
    customer = 1
 
    def __init__(self, data={}):
        self.username = data.get('username')
        self.email = data.get('email')
        self.token_blacked = data.get('token_blacked')
        self.role = data.get('role')
        self.table = data.get('table')
        self.user_id = data.get('user_id')
        self.db = create_conn()
        if not data.get('password'):
            self.password = ''
        else:
            self.password = BCRYPT.generate_password_hash(
                        data.get('password')).decode('utf-8')

    def get_user_by_email(self):
        con, response = self.db, None
        cur = con.cursor(cursor_factory=RealDictCursor)
        try:
            cur.execute("""select * from users WHERE email='{}'
            """.format(self.email))
            response = cur.fetchall()
        except psycopg2.DatabaseError as e:
            return {'message': '{}'.format(e)}
        con.close()
        return response
    
    def get_all(self):
        con, response = self.db, None
        cur = con.cursor(cursor_factory=RealDictCursor)
        try:
            cur.execute("select * from {}".format(self.table))
            response = cur.fetchall()
        except psycopg2.DatabaseError as e:
            return {'message': '{}'.format(e)}
        con.close()
        return response

    def user_is_admin(self):
        conn, response = self.db, None
        cur = con.cursor(cursor_factory=RealDictCursor)
        try:
            cur.execute("select role from users WHERE user_id='{}'"
                        .format(self.user_id))
            response = cur.fethone()
            if response == 2:
                return True
            return False
        except psycopg2.DatabaseError as e:
            return {'message': '{}'.format(e)}

    def save(self):
        data, conn = None, self.db
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        try:
            query = """ INSERT INTO users (user_name, email, password, role)
             values(%s, %s, %s, %s)"""
            cursor.execute(query, (self.username, self.email, self.password, 
                                   self.role))
            conn.commit()
            data = cursor.fetchone()
            cursor.close()   
        except psycopg2.DatabaseError as e:
            return {'message': '{}'.format(e)}
        return data

    def blacklist(self):
        conn, response = self.db, None
        cur = conn.cursor(cursor_factory=RealDictCursor)
    
        cur.execute("""INSERT INTO blacklisted (token) values('{}')"""
                    .format(self.token_blacked))
        conn.commit()
        return True
        # except psycopg2.DatabaseError as e:
        #     return {'message': '{}'.format(e)}

    def check_if_blacklist(self):
        conn, response = self.db, None
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute(""" SELECT * FROM blacklisted WHERE token='{}' """
                    .format(self.token_blacked))
        conn.commit()

        response = cur.fetchall()
        if len(response) > 0:
            return False
        return True