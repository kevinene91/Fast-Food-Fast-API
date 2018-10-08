
from .base import BaseModel
from psycopg2.extras import RealDictCursor
import psycopg2
from ..db.conn import create_conn

class MealModel(BaseModel):
    def __init__(self, data={}):
        self.meal_name = data.get('meal_name')
        self.meal_id = data.get('meal_id')
        self.price = data.get('price')
        self.db = create_conn()
        self.table = data.get('table_name')
        self.id = data.get('id')
        self.row = data.get('row')

    def get_by_name(self):
        con, response = self.db, None
        cur = con.cursor()
        try:
            cur.execute("""select * from meals WHERE meal_name='{}'
            """.format(self.meal_name))
            response = cur.fetchall()
        except psycopg2.DatabaseError as e:
            return {'message': '{}'.format(e)}
        con.close()
        return response

    def update_name(self):
        con, response = self.db, None
        cur = con.cursor(cursor_factory=RealDictCursor)
        try:
            cur.execute("""UPDATE meals SET meal_name='{}', price='{}' WHERE meal_id='{}'
            """.format(self.meal_name, self.price, self.meal_id))
            con.commit()
        except psycopg2.DatabaseError as e:
            return {'message': '{}'.format(e)}
        con.close()

    def save(self):
        data, conn = None, self.db
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        try:
            query = """insert into meals (meal_name, price) values('{}','{}')
            """.format(self.meal_name, self.price)
            cursor.execute(query)
            conn.commit()
            data = cursor.fetchone()
            cursor.close()   
        except psycopg2.DatabaseError as e:
            return {'message': '{}'.format(e)}
        return data
            