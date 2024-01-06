class Config(object):
    DEBUG = False
    DEVELOPMENT = False

class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True
    
class ProductionConfig(Config):
    DEVELOPMENT = False
    DEBUG = False