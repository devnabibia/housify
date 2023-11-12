import os

class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://njeri:sophia@localhost/househunting'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'powerfulsecretkey'
    UPLOADED_PHOTOS_DEST ='app/static/photos'


    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
    '''
    Pruduction configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class TestConfig(Config):
    '''
    Testing configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}
