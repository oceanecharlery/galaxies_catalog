import os
import sqlalchemy as db
from sqlalchemy.orm import scoped_session, sessionmaker

engine = db.create_engine('sqlite:///galaxies.db?check_same_thread=False')
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

    def getByRightAscension(self,category) :
        query = db.select([messier]).where(messier.c.right_ascension == category)
        return self.query(query)

    def getByDiscoverer(self,category) :
        query = db.select([messier]).where(messier.c.discoverer == category)
        return self.query(query)

    def getByNGC(self,ngc) :
        query = db.select([messier]).where(messier.c.ngc == ngc)
        return self.query(query)

    def getByObjectType(self,category) :
        query = db.select([messier]).where(messier.c.object_type == category)
        return self.query(query)

    def getBySeason(self,category) :
        query = db.select([messier]).where(messier.c.season == category)
        return self.query(query)

    def getByDeclinaison(self, category) : 
        query = db.select([messier]).where(messier.c.declinaison == category)
        return self.query(query)

    def getByYear(self, min, max) : 
        query = db.select([messier]).where(messier.c.year.between(min, max))
        return self.query(query)

    def getByMagnitude(self, min, max) : 
        #min = kwargs.get('min', None)
        #max = kwargs.get('max', None)
        query = db.select([messier]).where(messier.c.magnitude.between(min, max))
        return self.query(query)