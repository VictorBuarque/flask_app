from flask_sqlalchemy import SQLAlchemy

database = SQLAlchemy()

class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:@localhost/crm_victor'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:@localhost/crm_victor'

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
