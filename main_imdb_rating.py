import os
from dotenv import load_dotenv

from src.imdb.data_preparation_imdb import load_and_prepare_data, preprocess_data
from src.imdb.model_training_imdb import train_and_save_model
from src.imdb.prediction_imdb import predict_imdb_rating

# Carregar variáveis de ambiente
load_dotenv()

# Obter caminhos do arquivo csv das variáveis de ambiente
file_path = os.getenv('RAW_PATH')
file = f'{file_path}/desafio_indicium_imdb.csv'

# Caminhos dos arquivos
data_file_path = file
model_path = os.getenv('MODELS_PATH')

# Preparar os dados
df = load_and_prepare_data(data_file_path)
df = preprocess_data(df)

# Treinar e salvar o modelo
model, X_test, y_test = train_and_save_model(df, model_path)

# Novo filme para previsão
new_movie = {
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

# Prever a nota do IMDb
predicted_rating = predict_imdb_rating(new_movie, model_path)
print(f'Nota prevista do IMDb: {predicted_rating}')

# Relatar o insight
print("\nPrevisão da Nota do IMDb para 'The Shawshank Redemption'")
print(f"Título: The Shawshank Redemption")
print(f"Ano de Lançamento: 1994")
print(f"Certificado: A")
print(f"Duração: 142 min")
print(f"Gênero: Drama")
print(f"Resumo: Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.")
print(f"Meta_score: 80.0")
print(f"Diretor: Frank Darabont")
print(f"Estrelas: Tim Robbins, Morgan Freeman, Bob Gunton, William Sadler")
print(f"Número de Votos: 2,343,110")
print(f"Faturamento: $28,341,469")
print(f"Nota prevista do IMDb: {predicted_rating}")

print("\nUtilizando um modelo de regressão treinado com dados históricos de filmes, a nota prevista do IMDb para o filme 'The Shawshank Redemption' é {predicted_rating}.")
