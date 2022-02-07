from app.modules.scraper import MovieScrap
from app.modules.database_handler import DatabaseHandler
from hashlib import sha256

def ver_scrape(pwd: str):
    print(sha256(pwd))
    if sha256(pwd) == "614b50aa05247f1afaad1512ee19034bd16cd348b3d35a0c548cec37e9b896da":
        print("work")
    elif False : 
        scraper = MovieScrap(14,6)
        handler = DatabaseHandler()
        movies = scraper.scrape() 
        for movie in movies:
            handler.create(movie)


ver_scrape("C0mpleX_P@$$w0rd")
