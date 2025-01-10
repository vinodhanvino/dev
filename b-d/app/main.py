from distutils.command.config import config

import uvicorn
from fastapi import FastAPI
from config.connection import DBCtrl

dbCtrl : DBCtrl = DBCtrl()
app: FastAPI = dbCtrl.app




app.include_router()






if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8025)
