from pydantic import BaseModel


class InputModel(BaseModel): 
	Pregnancies: int
	Glucose: int
	SkinThickness: int
	BMI: float
	Age: int