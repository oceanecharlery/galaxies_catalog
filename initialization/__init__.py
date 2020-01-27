import sqlalchemy as db
from sqlalchemy.orm import scoped_session, sessionmaker

engine = db.create_engine('sqlite:///galaxies.db?check_same_thread=False')
connection = engine.connect()
metadata = db.MetaData()
objects = db.Table('messier', metadata, autoload=True, autoload_with=engine)

class Objects:
    def __init__(self):
        pass

    def all(self):
        query = db.select([messier])
        ResultProxy = connection.execute(query)
        ResultSet = ResultProxy.fetchall()
        return {"data" : [dict(row) for row in ResultSet]}