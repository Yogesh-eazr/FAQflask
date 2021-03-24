import pymongo
from flask import jsonify
import json

conn = pymongo.MongoClient('localhost', 27017)
db = conn['FAQsRevised']

with open('faq_xl.json') as fp:
    data = json.load(fp)

faq_list = []
for k,v in data.items():
    faq_list.append(v)

faq_quest = []
faq_answ = []

revised_faq_dict = {}

for k,v in faq_list[0].items():
    faq_quest.append(v)

for k,v in faq_list[1].items():
    faq_answ.append(v)

b = zip(faq_quest,faq_answ)
for k, v in b:
    revised_faq_dict[k] = v

collection = db['faqrevised']

### check_keys - False is used to eleminate any key related error, there by inserting a dict file as it is on mongodb

collection.insert(revised_faq_dict, check_keys=False)