from fastapi import FastAPI, BackgroundTasks, HTTPException, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

from fastapi.templating import Jinja2Templates
import crud
import schemas
from database import get_db, engine
import models

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/index", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.post("/translate", response_model=schemas.TaskResponse)
def translate(request: schemas.TranslationRequest):
    pass
    # TODO:
    # task = crud.create_translation_task(get_db.db, request.text, request.languages)
    
    # background_tasks.add_task(perform_translation, task.id, request.text, request.languages, get_db.db)
    
    # return {"task_id": {task.id}}