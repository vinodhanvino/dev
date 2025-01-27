
import uvicorn
from fastapi import FastAPI
from config.connection import DBCtrl
from users import user_routes

dbCtrl : DBCtrl = DBCtrl()
app: FastAPI = dbCtrl.app




app.include_router(user_routes.router, prefix='/users_')






if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8025)
