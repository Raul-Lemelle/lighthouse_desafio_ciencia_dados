# Modelo Regressão Linear
import pandas as pd

def load_and_prepare_data(file):
    # Carregando os dados
    df_imdb = pd.read_csv(file)

    # Substituindo valores ausentes e convertendo 'Gross' para float
    df_imdb['Gross'] = df_imdb['Gross'].str.replace(',', '').astype(float)
    df_imdb['Gross'] = df_imdb['Gross'].fillna(0)

    # Codificando variáveis categóricas
    df_imdb_encoded = pd.get_dummies(df_imdb, columns=['Director', 'Star1', 'Star2', 'Star3', 'Star4'])
    return df_imdb, df_imdb_encoded