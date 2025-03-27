# Diabetes Prediction Project

This project predicts diabetes using a Naive Bayes model trained on patient data. The dataset is preprocessed to handle missing values and scaled using a Quantile Transformer.

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
