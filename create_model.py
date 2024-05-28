import numpy as np
import pandas as pd 
from sklearn.preprocessing import QuantileTransformer
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.metrics import f1_score, precision_score, recall_score, accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
import pickle
df=pd.read_csv("diabetes.csv")

df['Glucose']=df['Glucose'].replace(0,df['Glucose'].mean())#normal distribution
df['BloodPressure']=df['BloodPressure'].replace(0,df['BloodPressure'].mean())#normal distribution
df['SkinThickness']=df['SkinThickness'].replace(0,df['SkinThickness'].median())#skewed distribution
df['Insulin']=df['Insulin'].replace(0,df['Insulin'].median())#skewed distribution
df['BMI']=df['BMI'].replace(0,df['BMI'].median())#skewed distribution

df_selected=df.drop(['BloodPressure','Insulin','DiabetesPedigreeFunction'],axis='columns')

x=df_selected
quantile  = QuantileTransformer()
X = quantile.fit_transform(x)
df_new=quantile.transform(X)
df_new=pd.DataFrame(X)
df_new.columns =['Pregnancies', 'Glucose','SkinThickness','BMI','Age','Outcome']

target_name='Outcome'
y= df_new[target_name]
X=df_new.drop(target_name,axis=1)

X_train, X_test, y_train, y_test= train_test_split(X,y,test_size=0.2,random_state=0)

param_grid_nb = {
    'var_smoothing': np.logspace(0,-3, num=200)
}
nbModel_grid = GridSearchCV(estimator=GaussianNB(), param_grid=param_grid_nb, verbose=1, scoring='f1', n_jobs=-1, cv=10)

best_model= nbModel_grid.fit(X_train, y_train)

nb_pred=best_model.predict(X_test)

print("Classification Report is:\n",classification_report(y_test,nb_pred))
print("\n F1:\n",f1_score(y_test,nb_pred))
print("\n Precision score is:\n",precision_score(y_test,nb_pred))
print("\n Recall score is:\n",recall_score(y_test,nb_pred))
print("\n Accuracy:\n",accuracy_score(y_test,nb_pred))


filename = 'diabetes_model.sav'
pickle.dump(best_model, open(filename, 'wb'))