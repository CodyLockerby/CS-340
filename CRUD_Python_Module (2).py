# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        #   
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (username, password,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
            
        # Create
    def create(self, data):
        if data is not None:
            result = self.collection.insert_one(data)
            return result.acknowledged
        return False

        # Read
    def read(self, query):
        if query is not None:
            result = self.collection.find(query)
            return list(result)
        return []

        #Update
    def update(self, query, new_data):
        if query is not None and new_data is not None:
            result = self.collection.update_many(
                query,
                {"$set": new_data}
            )
            return result.modified_count
        return 0

        # Delete
    def delete(self, query):
        if query is not None:
            result = self.collection.delete_many(query)
            return result.deleted_count
        return 0