from app.config.connection import DBCtrl
from sqlalchemy import Column, Integer, String, DateTime, Boolean, or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_json import mutable_json_type
from sqlalchemy.dialects.postgresql import JSONB

import datetime
import pytz
import hashlib
import os


IST = pytz.timezone('Asia/Kolkata')

dbctrl = DBCtrl()
dbSession =dbctrl.dbsession
dbQuery = dbSession.query

Base = declarative_base

class User(Base):
    __tablename__ = 'users_'
    __table_args__ = {'extend_existing': True}


    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    password_hash = Column(String)
    salt = Column(String)
    bio = Column(String)
    profile_pic = Column(String)
    interest = Column(String)
    created = Column(DateTime, default=datetime.datetime.now(IST))
    modified = Column(DateTime, default=datetime.datetime.now(IST))
    archived = Column(Boolean, default=False)
    more = Column(mutable_json_type(dbtype=JSONB, nested=True), default={})






Base.metadata.create_all(bind=DBCtrl().dbengine, checkfirst=True)
