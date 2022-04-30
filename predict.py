import pandas as pd
import matplotlib.pyplot as mplt
import seaborn as sns
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

def wq_prediction(final_features):
    data=pd.read_csv(r'C:\Users\thesu\OneDrive\Documents\water_potability.csv')
    df = pd.DataFrame(data)
    data[data['Potability'] == 0][['ph', 'Sulfate', 'Trihalomethanes']].median()
    data[data['Potability'] == 1][['ph', 'Sulfate', 'Trihalomethanes']].median()
    data['ph'].fillna(value=data['ph'].median(), inplace=True)
    data['Sulfate'].fillna(value=data['Sulfate'].median(), inplace=True)
    data['Trihalomethanes'].fillna(value=data['Trihalomethanes'].median(), inplace=True)
    X = df.drop('Potability',axis=1).values
    Y = df['Potability'].values

    X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size= 0.2, random_state=101)
    scaler = StandardScaler()
    scaler.fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)
    rdf=RandomForestClassifier()
    rdf.fit(X_train,Y_train)

    pre_fit=rdf.predict(final_features)
    return pre_fit





