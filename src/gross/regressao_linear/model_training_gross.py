# Modelo Regressão Linear
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import pandas as pd

def train_model(df_imdb_encoded):
    # Separando as variáveis independentes e dependentes
    X = df_imdb_encoded.drop(columns=['Gross', 'Series_Title', 'Released_Year', 'Certificate', 'Runtime', 'Genre', 'Overview', 'Meta_score', 'IMDB_Rating', 'No_of_Votes'])
    y = df_imdb_encoded['Gross']

    # Dividindo os dados em conjunto de treinamento e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Treinando o modelo de Regressão Linear
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Prevendo e avaliando o modelo
    y_pred = model.predict(X_test)
    print(f'R^2 Score: {r2_score(y_test, y_pred)}')

    return model, X
