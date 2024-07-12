import os
import pandas as pd
from dotenv import load_dotenv
import joblib

from src.imdb.random_forest_regressor.data_preparation_imdb import prepare_data

load_dotenv()

# Carregar variáveis de ambiente
models_path = os.getenv('MODELS_PATH')
processed_path = os.getenv('PROCESSED_PATH')

def prepara_novo_file(novo_filme, name_file_processed):
    novo_filme_df = pd.DataFrame([novo_filme])
    prepare_data(novo_filme_df, name_file_processed)

def predict_imdb_rating():
    # Carregar o modelo treinado
    model = joblib.load(f'{models_path}/modelo_random_forest_imdb.pkl')

    # Carregar o dataframe pré-processado
    df = pd.read_csv(f'{processed_path}/random_forest_novo_filme_processed.csv')
    
    # Previsão de IMDb Rating para o novo filme
    prediction = model.predict(df)
        
    print(f"Previsão de IMDb Rating para o novo filme: {prediction}")

if __name__ == "__main__":
    novo_filme = {
        'Series_Title': 'The Shawshank Redemption',
        'Released_Year': '1994',
        'Certificate': 'A',
        'Runtime': '142 min',
        'Genre': 'Drama',
        'Overview': 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.',
        'Meta_score': 80.0,
        'Director': 'Frank Darabont',
        'Star1': 'Tim Robbins',
        'Star2': 'Morgan Freeman',
        'Star3': 'Bob Gunton',
        'Star4': 'William Sadler',
        'No_of_Votes': 2343110,
        'Gross': '28,341,469'
    }

    name_file_processed = 'random_forest_novo_filme_processed.csv'

    prepara_novo_file(novo_filme, name_file_processed)

    predict_imdb_rating()
