from pymongo import MongoClient

CLIENT = "mongodb://localhost:27017/"
DB = "demo"
COLLECTION = "watch"

class DatabaseHandler:
    def _init_(self, client: str = CLIENT, db: str = DB, collection: str = COLLECTION):
        self.client = MongoClient(client)
        self.db = self.client[db]
        self.collection = self.db[collection]

    def get_collection(self):
        return self.collection.find({})

    def create(self, movie):
        if not self.db.find_one({"_id": movie["_id"]}):
            self.db.insert_one(movie)
        else:
            print("ERR:OVERRIDING EXISTING ID")

    def read_by_name(self, movie_name):
        try:
            return self.db.find_one({"name": movie_name})
        except:
            print("Movie not found")

    def read_by_genre(self, e):
        return self.db.find_one({"genre": e})

    def read_by_lang(self, lang):
        pass