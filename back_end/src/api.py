import logging
from datetime import datetime
import requests 
from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware  

log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
api_key = 'your_api_key'
file_name = f'_{str(datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p"))}.log'

news=FastAPI()

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
        return filter(response)
     
""" This function filter response recieved from newsdata.io api """
def filter(response):
     for i in response["results"]:
         del i["keywords"],i["creator"],i["video_url"],i["content"],i["image_url"],i["language"]
     return response["results"]

