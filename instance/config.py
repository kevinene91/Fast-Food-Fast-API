
import os 


class Config(object): 
    """
    Base config
     """
    DEBUG = False 
    CSRF_ENABLED = True 
    SECRET_KEY = os.getenv('SECRET_KEY')
    POSTGRES_DATABASE_URI = os.getenv('DATABASE_URL')


class DevelopmentConfig(Config):
    """
    Config for development
    """
    DEBUG = True


class TestingConfig(Config): 
    """
   Testing config
    """
    Testing = True
    DEBUG = True
    POSTGRES_DATABASE_URI = os.getenv('TEST_DATABASE_URL')


class ProductionConfig(Config): 
    """
    Production config
    """
    DEBUG = False 
    Testing = False
    
    app_config = {
        'development': DevelopmentConfig, 
        'production': ProductionConfig, 
        'testing': TestingConfig,
        }
