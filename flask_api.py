import crochet
crochet.setup()  # initialize crochet before further imports
import re
import numpy as np
from flask import Flask, jsonify
from scrapy import signals
from scrapy.crawler import CrawlerRunner
from scrapy.signalmanager import dispatcher

from web_scraping.web_scraping.spiders import quotes_spider

app = Flask(__name__)
output_data = []
output_element = []
crawl_runner = CrawlerRunner()
final_output = []
post_otput = []
# crawl_runner = CrawlerRunner(get_project_settings()) if you want to apply settings.py

@app.route("/scrape")
def scrape():
    # run crawler in twisted reactor synchronously
    output_data.clear()
    final_output.clear()
    scrape_with_crochet()
    final_output.append(post_otput)
    print("OUTPUT DATA", output_data)
    print("POST",post_otput)
    return jsonify(final_output)

@app.route("/scrape/element <int:element_id>",methods= ['GET'])
def element_scrap(element_id):
    b = input("Pls enter element or quote ")
    output_element.clear()
    scrap_element(b)
    print("ELEMENT scrap *********************")
    print(f" ELEMENENET {element_id}")
    output_element.append(post_otput)
    aa = np.array([output_element])
    print("output_element", output_element, len(output_element), type(output_element), aa.shape)
    num = output_element[:]
    print("NUMMMMM:::", num, type(num), len(num))
    # return jsonify(num[f"element {element_id}"])
    return jsonify(num[element_id])
    # return jsonify({"out_put =": output_element[:]})


ab = ""

count = 0
@app.route("/enter",methods = ['GET'])
def enter_password():
    ab = input("Enter password")
    global count
    count += 1
    b = password(ab,count)
    if(b == "FINISHED TRIAL"):
        return scrape()
    else:
        return b

def password(a,c):
    if(a=="hello"):
        return "WASSUP BOT"
    else:
        if(c == 3):
            return "FINISHED TRIAL"
        else:
            enter_password()

@crochet.wait_for(timeout=60.0)
def scrape_with_crochet():
    # signal fires when single item is processed
    # and calls _crawler_result to append that item
    dispatcher.connect(_crawler_result, signal=signals.item_scraped)
    eventual = crawl_runner.crawl(
        quotes_spider.Quotes)
    print("SCRAPE WITH CROCHET *******************")
    return eventual  # returns a twisted.internet.defer.'Deferred'

@crochet.wait_for(timeout=60.0)
def scrap_element(element_id):
    dispatcher.connect(_element_crawler, signal=signals.item_scraped)
    print("Scrape ELEMENT :::****************")
    evenitual = crawl_runner.crawl(
        quotes_spider.Quotes)
    print("Eveniiiiitual", evenitual)
    return evenitual

@app.route("/scrape",methods = ['POST'])
def post_element():
    elle = {"element 44": "jealousy",
            "element 45": "possessiveness",
            "element 46": "temperment"}
    # output_data.clear()
    # output_data.append(elle)
    post_otput.append(elle)
    return jsonify({"Created": post_otput})
    # return jsonify({"Created":output_data})

def _crawler_result(item, response, spider):
    """
    We're using dict() to decode the items.
    Ideally this should be done using a proper export pipeline.
    """
    # output_data.append(dict(item))
    final_output.append(dict(item))

def _element_crawler(item,response, spider):
    # output_data.append(dict(item))
    # print("_element_crawler :::: ")
    # item.update(post_otput)
    print("ITEM ", item, "Type :", type(item))
    orr = "^element\s\d+"
    for i in item:
        a = re.search(orr, i)
        if(i==a.group()):
            # print("KEYS OF ITEM :", i, "VALUE OF ITEM :", item[i])
            output_element.append(dict(item))
        else:
            continue

if __name__=='__main__':
    app.run('localhost', 8080)