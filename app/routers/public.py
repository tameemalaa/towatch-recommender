from fastapi import APIRouter , Depends , Form , status , Response , HTTPException ,Request
from pydantic import BaseModel
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from typing import Optional

router = APIRouter(tags=['Public'])
templates = Jinja2Templates(directory="../templates")

#DATABASE_HANDLER

@router.get('/',response_class = HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "test": "tessst"})


@router.get('/about')
def about():
    return {"about " : " fml square" , " about2 " : " I'm a json "}

@router.get('/search')
def search():
    return {"search " : " fml square" , " search " : " I'm a json "}

@router.get('/results')
def results():
    return {"results " : " fml square" , " results " : " I'm a json "}

@router.get('/movie/')
def show_movie(id:int):
    pass

@router.post('/custom')
def recommender():
    pass

@router.post('/extract')
def extract():
    pass