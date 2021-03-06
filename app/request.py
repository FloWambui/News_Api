import urllib.request, json
from .models import News


#Get api key
api_key = None
base_url= None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']


# def request(self,url,category):
#         self.base_url = url
#         self.req = request.urlopen(self.base_url.format(category))
#         resp = self.req.read()
#         data = json.loads(resp)
#         return data

# def get_news(id):
#     get_news_details_url = base_url.format(id,api_key)

#     with urllib.request.urlopen(get_news_details_url) as url:
#         news_details_data = url.read()
#         news_details_response = json.loads(news_details_data)

#         news_object = ()
#         if news_details_response:
#             id = news_details_response.get('id')
#             title = news_details_response.get('title')
#             urlToImage = news_details_response.get('urlToImage')
#             description = news_details_response.get('description')
#             url = news_details_response.get('url')
#             publishedAt = news_details_response.get('publishedAt')

#             news_object = News(urlToImage,title,description,url,publishedAt)

#     return news_object



def get_news():
    '''
    Function that gets the json response to the url request
    '''
    get_news_url='https://newsapi.org/v2/top-headlines?country=us&apiKey=f4cbfecd4e41465c841393d6b9a1f3c9'
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data=url.read()
        get_news_response=json.loads(get_news_data)
        news_results=None 

        if get_news_response['articles']:
            news_results_list=get_news_response['articles']
            news_results=process_results(news_results_list)

    return news_results


def process_results(news_list):
    news_results=[]
    for news_item in news_list:
        urlToImage = news_item.get('urlToImage')
        title = news_item.get('title')
        description = news_item.get('description')
        url = news_item.get('url')
        publishedAt = news_item.get('publishedAt')
        author = news_item.get('author')
        news_object = News(urlToImage,title,description,url,publishedAt,author)
        news_results.append(news_object)

    return news_results

