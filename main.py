from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        self.client = MongoClient('mongodb://localhost:45366')
        self.database = self.client['AAC']

    # Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            return self.database.animals.insert(data)  # data should be dictionary
        else:
            raise Exception("Nothing to save, because parameter is empty")

    # Create method to implement the R in CRUD.
    def read(self, data):
        if data is not None:
            return self.database.animals.find_one(data)
        else:
            raise Exception("Must define parameters.")
            return False

    # Create method to implement the U in CRUD.
    def update(self, data, newData):
        if data is not None:
            return self.database.animals.update_one(data,{'$set' : newData})
        else:
            print("Nothing to update")
            return False
    def delete(self, data):
        if data is not None:
            return self.database.animals.delete_one(data)
            print("Successfully Deleted")
        else:
            return False
        
    
    



