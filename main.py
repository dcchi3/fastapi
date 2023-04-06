"""Entry point to the application"""
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

def start_application():
    """Setting up necessary stuff during application start up"""
    app = FastAPI(title="Test Project", version="1.0")
    origins = [
        '<http://localhost>',
        '<http://localhost:8080>'
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    ) 

    return app
     
app = start_application()
if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)