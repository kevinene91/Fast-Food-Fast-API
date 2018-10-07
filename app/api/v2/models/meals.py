from ..db.conn import create_conn
from psycopg2.extras import RealDictCursor
import psycopg2


class MealModel:
    def __init__(self, data={}):
        self.meal_name = data.get('meal_name')
        self.meal_id = data.get('meal_id')
        self.price = data.get('price')
        self.table = data.get('table_name')
        self.db = create_conn()      

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

  

            