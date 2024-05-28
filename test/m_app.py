from fastapi import FastAPI 
from pydantic import BaseModel 
import pickle 

app = FastAPI() 

class ModelInput(BaseModel): 
	Pregnancies: int
	Glucose: int
	SkinThickness: int
	BMI: float
	Age: int

with open('diabetes_model.sav', 'rb') as model_file: 
	diabetes_model = pickle.load(model_file) 

@app.post('/diabetes_prediction') 
def diabetes_pred(input_parameters: ModelInput): 
	preg, glu, skin, bmi, age = ( 
		input_parameters.Pregnancies, input_parameters.Glucose, input_parameters.SkinThickness, input_parameters.BMI, input_parameters.Age 
	) 

	input_list = [preg, glu, skin, bmi, age] 

	prediction = diabetes_model.predict([input_list]) 

	if prediction[0] == 0: 
		return 'Không bị tiểu đường'
	else: 
		return 'Bị tiểu đường'
