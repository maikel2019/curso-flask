class Config(object):
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI="mysql+pymysql://root:JGLDNqMNgdc51G3r@localhost:3306/pruebas"