from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
import pymysql

# 数据库连接配置
SQLALCHEMY_DATABASE_URI = (
    "mysql+pymysql://root:123456@localhost/data?charset=utf8mb4"
)

# 创建数据库引擎
engine = create_engine(SQLALCHEMY_DATABASE_URI)
# 创建数据库会话
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# 声明基类
Base = declarative_base()



