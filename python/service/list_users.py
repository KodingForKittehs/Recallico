import os
import pymongo

client = pymongo.MongoClient(os.environ.get('MONGODB_URL'))
db = client.recallico

if __name__ == '__main__':
    for user in db.users.find({}):
        print(user)
