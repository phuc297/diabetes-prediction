import fastapi
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import status

from view_models.diabetes.result_status import ResultStatusViewModel 
from controllers.diabetes_predict import diabetes_predict

router = fastapi.APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse, include_in_schema=False)
async def form(request: Request):
    vm = ResultStatusViewModel(request)
    return templates.TemplateResponse("/index.html", vm.to_dict())

@router.post("/", response_class=HTMLResponse, include_in_schema=False)
async def form(request: Request):
    vm = ResultStatusViewModel(request)
    await vm.load()
    params = f'?preg={vm.preg}&glu={vm.glu}&skin={vm.skin}&bmi={vm.bmi}&age={vm.age}&message={vm.message}'
    response = fastapi.responses.RedirectResponse(f"/predict{params}", status_code=status.HTTP_302_FOUND)
    return response 

@router.get("/predict", response_class=HTMLResponse, include_in_schema=False)
def target_status(request: Request, preg:str, glu:str, skin:str, bmi:str, age:str):
    vm = ResultStatusViewModel(request)
    if preg.isdigit() and glu.isdigit() and skin.isdigit() and bmi.isdigit() and age.isdigit():
        vm.preg = preg
        vm.glu = glu
        vm.skin = skin
        vm.bmi = bmi
        vm.age = age
        vm.diabetes_predict()
    else:
        vm.message = "Needs to be number"
    return templates.TemplateResponse("/predict.html", vm.to_dict())

