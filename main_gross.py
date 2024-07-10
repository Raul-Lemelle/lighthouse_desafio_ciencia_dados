import os
from dotenv import load_dotenv

from src.gross.data_preparation_gross import load_and_prepare_data
from src.gross.model_training_gross import train_model
from src.gross.prediction_gross import print_top_coefficients, plot_top_coefficients

def main():
    # Carregar variáveis de ambiente
    load_dotenv()

    # Obter caminhos do arquivo csv das variáveis de ambiente
    file_path = os.getenv('RAW_PATH')
    file = f'{file_path}/desafio_indicium_imdb.csv'
    
    # Preparação dos dados
    df_imdb, df_imdb_encoded = load_and_prepare_data(file)

    # Treinamento do modelo
    model, X = train_model(df_imdb_encoded)

    # Exibição dos coeficientes mais significativos
    top_coef = print_top_coefficients(model, X)

    # Plotagem dos coeficientes mais significativos
    plot_top_coefficients(top_coef)

if __name__ == "__main__":
    main()