# Diabetes Prediction Project

This project predicts diabetes using a Naive Bayes model trained on patient data.

## Features
- Preprocessing of the dataset to handle missing values.
- Feature scaling using `QuantileTransformer`.
- Model training using Naive Bayes with hyperparameter tuning via `GridSearchCV`.
- Evaluation metrics: F1 Score, Precision, Recall, Accuracy.
- Model persistence using `pickle`.

## Files
- `diabetes.csv`: Dataset containing patient data and diabetes outcomes.
- `create_model.py`: Script for preprocessing, training, and saving the model.
- `diabetes_model.sav`: Saved model file for predictions.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/diabetes-prediction.git
   cd diabetes-prediction

2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
3. Run the model training script:
   ```bash
   python create_model.py
4. Run the FastAPI application:
   ```bash
   uvicorn main:app

Ensure `python-multipart` is installed to handle form data in FastAPI.
The trained model is saved as `diabetes_model.sav` in the project directory.

## Screenshots from this project
<img src="https://github.com/user-attachments/assets/be89307d-c0c2-4a9b-bb71-08e53dde13c2" width=600/>

<br>

<img src="https://github.com/user-attachments/assets/100b8a83-a5bb-4d85-a808-c1a7526d5332" width=600/>



