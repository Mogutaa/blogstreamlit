import os
from dotenv import load_dotenv
from pymongo import MongoClient, TEXT

load_dotenv()

class MongoDB:
    def __init__(self):
        self.client = MongoClient(os.getenv("MONGODB_URI"))
        self.db = self.client[os.getenv("DB_NAME")]
        
    def get_collection(self, name):
        return self.db[name]

db = MongoDB()

# Coleções principais
users_col = db.get_collection("users")
projects_col = db.get_collection("projects")
posts_col = db.get_collection("posts")

