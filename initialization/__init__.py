import os
import sqlalchemy as db
from sqlalchemy.orm import scoped_session, sessionmaker

engine = db.create_engine('sqlite:///galaxies.db?check_same_thread=False')
###engine = db.create_engine('sqlite:///galaxies.sqlite') 
connection = engine.connect()
metadata = db.MetaData()
messier = db.Table('messier', metadata, autoload=True, autoload_with=engine)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False,bind=engine))

class Messier:
    def __init__(self):
        pass


    def query(self,query):
        ResultProxy = connection.execute(query)
        ResultSet = ResultProxy.fetchall()
        return {"data" : [dict(row) for row in ResultSet]}

    def all(self):
        query = db.select([messier])
        ResultProxy = connection.execute(query)
        ResultSet = ResultProxy.fetchall()
        return {"data" : [dict(row) for row in ResultSet]}


    def getByMessier(self,id) :
        query = db.select([messier]).where(messier.c.messier == id)
        return self.query(query)

    def getByConstellation(self,category) :
        query = db.select([messier]).where(messier.c.constellation == category)
        return self.query(query)

    def getByConstellationEN(self,category) :
        query = db.select([messier]).where(messier.c.constellation_en == category)
        return self.query(query)

    def getByConstellationFR(self,category) :
        query = db.select([messier]).where(messier.c.constellation_fr == category)
        return self.query(query)

    def getByConstellationLATIN(self,category) :
        query = db.select([messier]).where(messier.c.constellation_latin == category)
        return self.query(query)

    def getByDiscoverer(self,category) :
        query = db.select([messier]).where(messier.c.messier == category)
        return self.query(query)

    def getByNGC(self,category) :
        query = db.select([messier]).where(messier.c.messier == category)
        return self.query(query)

    def getByObject_Type(self,category) :
        query = db.select([messier]).where(messier.c.messier == category)
        return self.query(query)

    def getBySeason(self,category) :
        query = db.select([messier]).where(messier.c.messier == category)
        return self.query(query)