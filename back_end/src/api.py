import logging
from datetime import datetime
import requests 
from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware 
# import sys
# print(sys.path)  
from mongoengine import connect
from models import Prev_news
import json


log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
api_key = 'pub_880000962e9f4f06fd6d1a7164f94fd5302d'
file_name = f'_{str(datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p"))}.log'

news=FastAPI()

"""Connect to MongoDB"""
connect(db="school",host="localhost", port=27017)

news.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True 
                   , allow_methods=["*"], allow_headers=["*"])

logging.basicConfig(filename=file_name, filemode='a',format=log_fmt,level='INFO')

"""Whenever get request made on '/news' endpoint 'top_news' function will fetch news 
from newsdata.io api and after filtering return result.
"""
@news.get('/news',tags=["NEWS"])
def top_news():
   newsdata_url = "https://newsdata.io/api/1/news?apikey={0}&language=en".format(api_key) 
   try:
        response = requests.get(newsdata_url)
        logging.info("Request successful")
   except:
        logging.error('Error occurred', exc_info=True) 
        raise HTTPException(status_code=404, detail="Can't fetch news") 
   else:
        response = requests.get(newsdata_url).json()
        add_db(response)
        return filter(response)
     
""" This function filter response recieved from newsdata.io api """
def filter(response):
     for i in response["results"]:
         del i["keywords"],i["creator"],i["video_url"],i["content"],i["image_url"],i["language"]
     return response["results"]

""" This function add news into the Database """
def add_db(response):
     for i in response["results"]:
         documnt=Prev_news(title=i["title"],category=i["category"],description=i["description"]
                             ,country=i["country"],pubdate=i["pubDate"],source_id=i["source_id"]
                             ,link=i["link"])
         documnt.save()
     

@news.get("/get_old_news", tags=["OLD NEWS"])
def old_news():
     list_of_old_news=json.loads(Prev_news.objects().to_json())
     # str_old_news=Oldnews.objects().to_json()
     # list_of_old_news=json.loads(all_old_news)
     return list_of_old_news
