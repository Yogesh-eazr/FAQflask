import pymongo


conn = pymongo.MongoClient('localhost', 27017)
db = conn['myHEADERS']

count = 0
with open('seg_headerslist.json', 'r') as f:
    data = f.read()

for i in data:
    print(i)
    count += 1
    if count == 10:
        break
    else:
        continue
collection = db['headers_keyword']
