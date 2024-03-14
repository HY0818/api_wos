from sqlalchemy.orm import Session

from . import models, schemas


# 根据wos数据库唯一标识码查询
def get_data(db: Session, ut: str):
    return db.query(models.Data).filter(models.Data.UT == ut).first()


# 根据隶属关系查询
def get_data_by_affiliations(db: Session, affiliations: str, skip: int = 0, limit: int = 100, ):
    return db.query(models.Data).filter(models.Data.Affiliations == affiliations).offset(skip).limit(
        limit).all()


# 根据出版年份查询
def get_data_by_year(db: Session, publication_year: str, skip: int = 0, limit: int = 100):
    return db.query(models.Data).filter(models.Data.Publication_Year == publication_year).offset(skip).limit(
        limit).all()


# 查询数据库指定条数信息
def get_datas(db: Session, skip: int = 0, limit: int = 1000):
    return db.query(models.Data).offset(skip).limit(limit).all()


# 根据作者姓名查询
def get_data_by_name(db: Session, author_name: str, skip: int = 0, limit: int = 10):
    return db.query(models.Data).filter(models.Data.Author_Full_Names == author_name).offset(skip).limit(
        limit).all()


# 根据出版商查询
def get_data_by_publisher(db: Session, publisher: str, skip: int = 0, limit: int = 100):
    return db.query(models.Data).filter(models.Data.Publisher == publisher).offset(skip).limit(
        limit).all()

# def create_user(db: Session, user: schemas.UserCreate):
#     fake_hashed_password = user.password + "notreallyhashed"
#     db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user


# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()
#
#
# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item
