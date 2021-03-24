import json
import re
from bson import json_util
import pymongo
from FAQREvised import revised_faq_dict
from flask import jsonify, Flask, request
import json
from collections import ChainMap

conn = pymongo.MongoClient('localhost', 27017)
db = conn['FAQsRevised']
t = db.faqrevised

app = Flask(__name__)

@app.route("/FAQ")
def faq_display():
    faq_dict = revised_faq_dict
    return json.loads(json_util.dumps(faq_dict))
#FAQ_KEY
# FAQ_key_val
# I have provided all documents and my credit limit has been reduced?
# How is the statement amount calculated?
@app.route("/FAQ_key_val <string:faq_key>",methods= ['GET'])
def faq_key_value(faq_key):
    mm = faq_key
    print(mm, len(mm))
    faq_dict = revised_faq_dict
    # faq_rev = json.loads(json_util.dumps(faq_dict))
    specific_key_val = {}
    key_list = []
    for k,v in faq_dict.items():
        ml = v
        try:
            hj = re.search(mm,k)
            key_list.append(hj.group())


            print(key_list,type(key_list))
            print("V::::", ml, "TYPE", type(ml))
            specific_key_val[k]=v
        except:
            continue

    print("DICTTT", specific_key_val)
    return jsonify({"KEY":specific_key_val})

@app.route("/DBFAQ <string:faq_key>",methods= ['GET'])
def dbFAQ(faq_key):
    mm = faq_key
    table = t.find()
    key_list = []
    key_list1 = []
    count = 0
    count1 = 0
    for i in table:
        count +=1
        key_list.append(i)
    specific_key_val = {}
    specific_display_key_val = {}
    for i in range(len(key_list)):
        specific_key_val = dict(ChainMap(key_list[i]))
    print("DIDIDID",specific_key_val,"TYPE::",type(specific_key_val))
    for k,v in specific_key_val.items():
        ml = v
        try:
            hj = re.search(mm, k)
            key_list1.append(hj.group())
            print(key_list1, type(key_list1))
            print("V::::", ml, "TYPE", type(ml))
            specific_display_key_val[k] = v
        except:
            continue
        count1 += 1
        print("K::::",k,"V::::",v)
    print("DICTTT", specific_display_key_val)
    print(count1)
    return jsonify({"KEY": specific_display_key_val})

if __name__=='__main__':
    app.run('localhost', 8082)