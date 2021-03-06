import os

class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL='https://newsapi.org/v2/top-headlines?country=us&apiKey=f4cbfecd4e41465c841393d6b9a1f3c9'
    NEWS_API_KEY=os.environ.get('NEWS_API_KEY')
    SECRET_KEY=os.environ.get('SECRET_KEY')



class ProdConfig(Config):
    pass


class DevConfig(Config):
    '''
    Development configuration child class
    '''
    
DEBUG = True

config_options={
    'development':DevConfig,
    'production':ProdConfig
}