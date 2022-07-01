import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests   
from requests.exceptions import HTTPError


news=FastAPI()

news.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True , allow_methods=["*"], allow_headers=["*"])

logging.basicConfig(filename='mylog.log', filemode='a',format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
                     datefmt='%d-%b-%y %H:%M:%S')

@news.get('/news',tags=["NEWS"])
def Topnews():
   #  newsdata.io api
   my_url =  "https://newsdata.io/api/1/news?apikey=pub_880000962e9f4f06fd6d1a7164f94fd5302d&language=en"
   try:
        response = requests.get(my_url)
        # If the response was successful, no Exception will be raised
        response.raise_for_status()
   except Exception as err:
        logging.error('Other error occurred', exc_info=True)  # Python 3.6
   else:
      response = requests.get(my_url).json()
      for i in response["results"]:
       del i["keywords"],i["creator"],i["video_url"],i["content"],i["image_url"],i["language"]
      return response["results"]

