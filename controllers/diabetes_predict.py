import pickle

def diabetes_predict(preg:int, glu:int, skin:int, bmi:int, age:int)->str:

    with open('diabetes_model.sav', 'rb') as model_file: 
        diabetes_model = pickle.load(model_file) 

    input_list = [preg, glu, skin, bmi, age] 

    prediction = diabetes_model.predict([input_list]) 

    if prediction[0] == 0: 
        return '0'
    else: 
        return '1'
