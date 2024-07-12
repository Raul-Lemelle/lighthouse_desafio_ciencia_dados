import os
import numpy as np
import pandas as pd
from dotenv import load_dotenv

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import joblib


def train_model():
    # Carregar o dataframe pré-processado
    processed_path = os.getenv('PROCESSED_PATH')
    df = pd.read_csv(f'{processed_path}/rfr_imdb_processed.csv')

    # Definir features e target
    features = ['Released_Year', 'IMDB_Rating', 'Meta_score', 'No_of_Votes']
    target = 'IMDB_Rating'

    X = df[features]
    y = df[target]

    # Dividir os dados em conjunto de treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Inicializar o modelo RandomForestRegressor
    model = RandomForestRegressor(random_state=42)

    # Treinar o modelo
    model.fit(X_train, y_train)

    # Avaliar o modelo
    y_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))

    print(f'R² Score: {r2}')
    print(f'RMSE: {rmse}')

    # Salvar o modelo treinado em um arquivo .pkl
    models_path = os.getenv('MODELS_PATH')
    joblib.dump(model, f'{models_path}/modelo_random_forest_imdb.pkl')

    # Plot_feature_importances
    feature_importances = pd.Series(model.feature_importances_, index=X.columns)
    feature_importances = feature_importances.sort_values(ascending=False)

    plt.figure(figsize=(10, 6))
    sns.barplot(x=feature_importances, y=feature_importances.index, palette='viridis')
    plt.xlabel('Importância da Característica')
    plt.ylabel('Característica')
    plt.title('Importância das Características no Modelo_2')
    plt.show()

if __name__ == "__main__":
    load_dotenv()    

    train_model()