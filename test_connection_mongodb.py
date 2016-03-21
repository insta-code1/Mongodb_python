import pymongo

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
docs = [{"name": "Henry", "surname": "Moore", "twitter": "@henrymoore"},
       {"name": "Stephen", "surname": "Fry", "twitter": "@stephenfry"}]
coll.insert(docs)
result = coll.find_one()
print result