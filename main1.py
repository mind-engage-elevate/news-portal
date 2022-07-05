
import requests
from requests.exceptions import HTTPError
from fastapi import FastAPI,HTTPException
import logging

app=FastAPI()
logging.basicConfig(filename='test.log',format='%(asctime)s:%(levelname)s:%(message)s')

@app.get("/")
def news():
    try:
        main_url="https://newsdata.io/api/1/news?apikey=pub_8144b6b37b8522ef6c6e77859704c30cdbc1"
        news=requests.get(main_url).json()
        logging.info("Request successful")
        return news
    except:
        logging.error("Can't fetch news")
        raise HTTPException(status_code=404, detail="Can't fetch news")
        


    
        
    



