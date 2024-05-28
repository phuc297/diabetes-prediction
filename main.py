
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


from api import api_responses
from views import result_status

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(api_responses.router)
app.include_router(result_status.router)


