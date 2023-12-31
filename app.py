from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# creating an instance of the FastAPI amd the Jinja2Templates class
app = FastAPI()
templates = Jinja2Templates(directory="templates")


# endpoints for the website
@app.get("/login", response_class=HTMLResponse)
async def render_login(request: Request):
  return templates.TemplateResponse("login.html", {"request": request})


@app.get("/signup", response_class=HTMLResponse)
async def render_signup(request: Request):
  return templates.TemplateResponse("signup.html", {"request": request})


@app.get("/dashboard", response_class=HTMLResponse)
async def render_dashboard(request: Request):
  return templates.TemplateResponse("dashboard.html", {"request": request})


@app.get("/editfile", response_class=HTMLResponse)
async def render_editfile(request: Request):
  return templates.TemplateResponse("editfile.html", {"request": request})


@app.get("/settings", response_class=HTMLResponse)
async def render_settings(request: Request, userid: str):
  return templates.TemplateResponse("settings.html", {"request": request, "username": userid})
