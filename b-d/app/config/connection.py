from fastapi import FastAPI
from pypattyrn.creational.singleton import Singleton
from sqlalchemy import create_engine
from _config import DB_PROD_URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.scoping import ScopedSession, scoped_session
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.gzip import GZipMiddleware

class DBCtrl(object, metaclass=Singleton):

    def __init__(self):
        self.app = FastAPI()
        self.DBEngine = None
        self.init_db()
        self.setup_middlewares()

    def init_db(self):
        self.dbengine = create_engine(DB_PROD_URL, pool_pre_ping=True, connect_args={
            "keepalives": 1,
            "keepalives_idle": 1,
            "keepalives_interval": 1,
            "keepalives_count": 1,
        })
        sessionMaker = sessionmaker(autocommit=False, autoflush=False, bind=self.dbengine)
        self.dbsession: ScopedSession = scoped_session(sessionMaker)

    def setup_middlewares(self):
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
        self.app.add_middleware(GZipMiddleware, minimum_size=50)