class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL='https://newsapi.org/v2/top-headlines?country=us&apiKey=f4cbfecd4e41465c841393d6b9a1f3c9'



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True