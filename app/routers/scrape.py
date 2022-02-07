from fastapi import APIRouter , Depends , Form , status , Response , HTTPException ,Request
from fastapi.responses import HTMLResponse, FileResponse
from app.logic.scrape import ver_scrape

router = APIRouter(tags=['Scrap'])

@router.post('/scrape')
def ver_scrape(pwd : str):
    pass