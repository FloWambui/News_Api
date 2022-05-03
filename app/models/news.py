class News:
    '''
    News class to define news objects
    '''
 
    def __init__(self):
        pass
    
    def __init__(self, urlToImage,title,description,url,publishedAt ):
        self.urlToImage=urlToImage
        self.title=title
        self.description=description
        self.url=url
        self.publishedAt=publishedAt
