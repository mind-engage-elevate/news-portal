import requests
import logging


logging.basicConfig(filename='mylog.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')


def News():

    # following query parameters are used
    # source, sortBy and apiKey
    query_params = {
        "sortBy": "top",
        "apiKey": "da508c7d4a5948d2b507650a4668cb02"
    }
    main_url = " https://newsapi.org/v2/top-headlines?country=us&apiKey=da508c7d4a5948d2b507650a4668cb02"
    try:
        response = requests.get(main_url)
        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except Exception as err:
        logging.error('Other error occurred', exc_info=True)
    # fetching data in json format
    else:
        res = requests.get(main_url, params=query_params)
    open_page = res.json()

    # getting all articles in a string article
    article = open_page["articles"]

    # empty list which will contain all trending news
    results = []

    for ar in article:
        results.append(ar["title"])

    for i in range(len(results)):

        # printing all trending news
        print(i + 1, results[i])


# Driver Code
if __name__ == '__main__':

    News()
