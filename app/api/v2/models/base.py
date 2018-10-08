from ..db.conn import create_conn
from psycopg2.extras import RealDictCursor
import psycopg2


class BaseModel:
    def __init__(self, data={}):
        self.table = data.get('table_name')
        self.db = create_conn()
        self.id = data.get('id')
        self.row = data.get('row')

    def get_by_id(self):
        con, response = self.db, None
        cur = con.cursor(cursor_factory=RealDictCursor)
        try:
            cur.execute("select * from {} WHERE {}='{}'".format(self.table, self.id, self.row))
            response = cur.fetchone()
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

    def delete(self):
        con = self.db
        cur = con.cursor(cursor_factory=RealDictCursor)
        try:
            cur.execute("""delete from {} where {} ='{}'
            """.format(self.table, self.id, self.row))
            con.commit()
        except psycopg2.DatabaseError as e:
            return {'message': '{}'.format(e)}
        con.close()
