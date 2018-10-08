import psycopg2
from ..db.conn import create_conn
from .base import BaseModel
from psycopg2.extras import RealDictCursor


class OrderModel(BaseModel):
    pending = 1,
    completed = 2, 
    declined = 3

    def __init__(self, data={}):
        self.table = data.get('table_name')
        self.order_id = data.get('order_id')
        self.meal_id = data.get('meal_id')
        self.user_id = data.get('user_id')
        self.username = data.get('user_name')
        self.quantity = data.get('quantity')
        self.id = data.get('id')
        self.price = data.get('price')
        self.total = data.get('total')
        self.row = data.get('row')
        self.status = data.get('status')
        self.status_default = 1
        self.db = create_conn()


    def get_meal_name(self):
        con, response = self.db, None
        cur = con.cursor(cursor_factory=RealDictCursor)
        try:
            cur.execute("""select meal_name from meals WHERE meal_id='{}'
            """.format(self.meal_id))
            response = cur.fetchone()
        except Exception as e:
            print(e)
        con.close()
        return response
        
    def get_user_name(self):
        con, response = self.db, None
        cur = con.cursor(cursor_factory=RealDictCursor)
        try:
            cur.execute("""select user_name from users WHERE user_id='{}'
            """.format(self.user_id))
            response = cur.fetchone()
        except psycopg2.DatabaseError as e:
            return {'message': '{}'.format(e)}
        con.close()
        return response


    def calculate_price(self):
        price = self.get_price()
        quantity = self.quantity
        return price * quantity

    def update_status(self):
        con = self.db
        cur = con.cursor(cursor_factory=RealDictCursor)
        try:
            cur.execute("UPDATE orders SET status='{}' WHERE order_id='{}'"
                        .format(self.status, self.order_id))
            con.commit()
        except psycopg2.DatabaseError as e:
            return {'message': '{}'.format(e)}
        con.close()
    
    def get_user_orders(self):
        con, response = self.db, None
        cur = con.cursor(cursor_factory=RealDictCursor)
        try:
            cur.execute("select * from orders where user_id='{}' "
                        .format(self.user_id))
            response = cur.fetchall()
        except psycopg2.DatabaseError as e:
            return {'message': '{}'.format(e)}
        con.close()
        return response
        
    def get_price(self):
        con, response = self.db, None
        cur = con.cursor()
        try:
            cur.execute(""" select price from meals WHERE meal_id='{}'
            """.format(self.meal_id))
            response = cur.fetchone()[0]

        except psycopg2.DatabaseError as e:
            return {'message': '{}'.format(e)}
        con.close()
        return response

    def save(self):
        data, conn = None, self.db
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        try:
            query = """ insert into orders (meal_id, user_id, quantity, total, status) 
            values('{}','{}','{}','{}','{}')
            """.format(self.meal_id,  self.user_id,  self.quantity, self.total,
                       self.status_default)
            cursor.execute(query)
            conn.commit()
            data = cursor.fetchone()
            cursor.close()
        except Exception as e:
            print(e)
        # except psycopg2.DatabaseError as e:
        #         return{'message': '{}'.format(e)}
        return data