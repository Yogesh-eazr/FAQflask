import pymongo
import json
conn = pymongo.MongoClient('localhost', 27017)
db = conn['FAQs']
count = 0

# with open('faq_xl.json', 'r') as f:
#     data = f.read()

# with open('faq_xl.json') as fp:
#     data = json.load(fp)
# print(type(data))

data = json.load(open('faq_xl.json'))

print(data)

## created a table
collection = db['faq']

## flooding a table
collection.insert_one(data)
