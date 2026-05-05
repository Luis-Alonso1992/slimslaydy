from fastapi import FastAPI, Request
from raiderio import get_character_information
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def dashboard(request: Request):
    character = get_character_information()
    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={"character": character,}   
    )