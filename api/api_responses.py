from datetime import datetime

import fastapi

from models.input_model import InputModel
from controllers.diabetes_predict import diabetes_predict

router = fastapi.APIRouter()

@router.post("/diabetes_predict")
def predict(input: InputModel):
    preg = input.Pregnancies
    glu = input.Glucose
    skin = input.SkinThickness
    bmi = input.BMI
    age = input.Age

    message = diabetes_predict(preg, glu, skin, bmi, age)

    return {"message": message}