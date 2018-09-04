
import os 

class Config(object): 
	DEBUG = False 
	CSRF_ENABLED = True 
	SECRET = os.getenv('SECRET')

class DevelopmentConfig(Config):
	DEBUG = True


class TestingConfig(Config): 
	Testing = True
	DEBUG = True

class ProductionConfig(Config): 
	DEBUG = False 
	Testing = False


app_config = {
	'development': DevelopmentConfig, 
	'production': ProductionConfig, 
	'testing': TestingConfig,
}