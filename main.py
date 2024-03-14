from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import List

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# @app.post("/users/", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     db_user = crud.get_user_by_email(db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return crud.create_user(db=db, user=user)
#
#
# @app.get("/users/", response_model=list[schemas.User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = crud.get_users(db, skip=skip, limit=limit)
#     return users


@app.get("/data/data/{ut}", response_model=schemas.DataUt)
def read_data(ut: str, db: Session = Depends(get_db)):
    db_data = crud.get_data(db, ut=ut)
    if db_data is None:
        raise HTTPException(status_code=404, detail="Data not found")
    return db_data


@app.get("/data/{affiliations}", response_model=List[schemas.Data])
def read_data(affiliations: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_data = crud.get_data_by_affiliations(db, skip=skip, limit=limit, affiliations=affiliations)
    if db_data is None:
        raise HTTPException(status_code=404, detail="Data not found")
    return db_data


@app.get("/data/", response_model=List[schemas.Data])
def read_datas(skip: int = 0, limit: int = 1000, db: Session = Depends(get_db)):
    datas = crud.get_datas(db, skip=skip, limit=limit)
    return datas


@app.post("/data/{publication_year}", response_model=List[schemas.DataYear])
def read_data(publication_year: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_data = crud.get_data_by_year(db, skip=skip, limit=limit, publication_year=publication_year)
    if db_data is None:
        raise HTTPException(status_code=404, detail="Data not found")
    return db_data


@app.post("/data/data/{Author_name}", response_model=List[schemas.DataName])
def read_data(author_name: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_data1 = crud.get_data_by_name(db, skip=skip, limit=limit, author_name=author_name)
    if db_data1 is None:
        raise HTTPException(status_code=404, detail="Data not found")
    return db_data1


@app.get("/data/data/data/{Publisher}", response_model=List[schemas.DataPub])
def read_data(publisher: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_data2 = crud.get_data_by_publisher(db, skip=skip, limit=limit, publisher=publisher)
    if db_data2 is None:
        raise HTTPException(status_code=404, detail="Data not found")
    return db_data2
