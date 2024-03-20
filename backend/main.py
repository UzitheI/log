from fastapi import APIRouter, FastAPI, status, Depends

app=FastAPI()

from routes import user as user_route


app.include_router(user_route.router,prefix='/user',tags=['user'])