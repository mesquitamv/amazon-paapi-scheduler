from pymongo import MongoClient

class Database(object):
  
  def __init__(self, host, port, username, password):
    
    self.client = MongoClient(host, port, username = username, password = password)
    self.db = self.client.schedulerDB
    
  def insert_one(self, data):
    self.db.scheduler.insert_one(data)
    
  def insert_many(self, data):
    self.db.scheduler.insert_many(data)
  
  def return_conn(self):
    return self.db