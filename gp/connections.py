from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from gp.configs import *

# sqlalchemy model 基类
Base = declarative_base()


# 数据库连接引擎，用来连接数据库
def db_connect_engine():
    engine = create_engine("%s://%s:%s@%s:%s/%s?charset=utf8mb4"
                           % (DATABASES['DRIVER'],
                              DATABASES['USER'],
                              DATABASES['PASSWORD'],
                              DATABASES['HOST'],
                              DATABASES['PORT'],
                              DATABASES['NAME']),
                           echo=False)

    if not database_exists(engine.url):
        create_database(engine.url)  # 创建库
        Base.metadata.create_all(engine)  # 创建表

    return engine


# 数据库会话，用来操作数据库表
def db_session():
    return sessionmaker(bind=db_connect_engine())
