import uvicorn
from routers import scrape
from routers import public
from fastapi import FastAPI

app = FastAPI()
app.include_router(public.router)
app.include_router(scrape.router)

if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1",port=80)

