class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
    SECRET_KEY = "bmk@$ecretkey15#08#2020#15#02#55"


    # Flask - security

    SECURITY_PASSWORD_SALT = 'saltysaltypasswordomg'
    SECURITY_PASSWORD_HASH = 'sha512_crypt'