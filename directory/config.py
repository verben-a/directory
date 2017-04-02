import os
class DevelopmentConfig(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:thinkful@localhost:5432/alumni"
    DEBUG = True
    SECRET_KEY = os.environ.get("SECRET_KEY", os.urandom(12))


class TestConfig(object):
	SQLALCHEMY_DATABASE_URI = "postgresql://postgres:thinkful@localhost:5432/alumni-test"
	DEBUG = True