import datetime

import pymongo

from datetime import timedelta

def mongo_connect():
    try:
        conn = pymongo.MongoClient()
        print "Mongo is Connected"
        return conn
    except pymongo.errors.ConnectionFailure, e:
        print "could not connect to MongoDB: %s" % e



conn = mongo_connect()
db = conn['twitter_stream']
coll = db.my_collection
docs = [{"name": "Henry", "surname": "Moore", "twitter": "@henrymoore", "date": datetime.datetime.utcnow()},
       {"name": "Stephen", "surname": "Fry", "twitter": "@stephenfry", "date": datetime.datetime.utcnow() - timedelta(days=2)},
        {"name": "Stephen", "surname": "Debalus", "twitter": "@stephend", "date": datetime.datetime.utcnow() - timedelta(days=10)},
        {"name": "Stephen", "surname": "Fry", "twitter": "@stephenfry", "date": datetime.datetime.utcnow() - timedelta(days=10), "_id": "22"}]
coll.insert_many(docs)
date = datetime.datetime.utcnow()
for doc in coll.find({"date": {"$lt": date}}).sort("name"): #see also - $lte, $gte, $ne

    print doc