import os
import pandas as pd
from dotenv import load_dotenv
from sklearn.preprocessing import LabelEncoder
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

def prepare_data(file, name_file_processed):
    if isinstance(file, pd.DataFrame):
        # Se for um DataFrame do Pandas, continua com ele
        df = file.copy()
    else:
        # Caso contrário, carrega o arquivo CSV
        df = pd.read_csv(file)
    
    
    # Coluna Released_Year
    # Limpar espaços em branco e converter para tipo numérico tratando erros
    df['Released_Year'] = df['Released_Year'].str.strip()  # Remover espaços em branco
    df['Released_Year'] = pd.to_numeric(df['Released_Year'], errors='coerce')  # Converter e tratar erros
    # Converter para inteiro, lidando com NaN
    df['Released_Year'] = df['Released_Year'].astype('Int64')  # Usar 'Int64' para lidar com NaNs

    # Coluna Runtime
    # Converter a coluna 'Runtime' para inteiro, extraindo apenas os dígitos
    df['Runtime'] = df['Runtime'].str.extract(r'(\d+)').astype(int)

    # Coluna Gross
    # Remover vírgulas e converter para tipo numérico, tratando NaN
    df['Gross'] = df['Gross'].str.replace(',', '').fillna('0').astype(int)

    # Verifica se as colunas estão presentes antes de tentar removê-las
    columns_to_drop = ['Unnamed: 0', 'Series_Title', 'Overview']
    df.drop(columns=[col for col in columns_to_drop if col in df], inplace=True, errors='ignore')

    # Coluna Certificate
    df['Certificate'] = df['Certificate'].fillna('Unknown')

    # Colunas Meta_score e Coluna Released_Year
    df = interative_imputer(df)

    # Codificar variáveis categóricas usando LabelEncoder
    label_encoder = LabelEncoder()
    df['Certificate'] = label_encoder.fit_transform(df['Certificate'].astype(str))
    df['Genre'] = label_encoder.fit_transform(df['Genre'])
    df['Director'] = label_encoder.fit_transform(df['Director'])
    df['Star1'] = label_encoder.fit_transform(df['Star1'])
    df['Star2'] = label_encoder.fit_transform(df['Star2'])
    df['Star3'] = label_encoder.fit_transform(df['Star3'])
    df['Star4'] = label_encoder.fit_transform(df['Star4'])

    # Salvar o dataframe processado em um novo arquivo CSV
    processed_path = os.getenv('PROCESSED_PATH')
    df.to_csv(f'{processed_path}/{name_file_processed}', index=False)
    print(df.head(2))

def interative_imputer(df):
    # Selecionar colunas numéricas para a imputação
    numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns

    # Configurar o Iterative Imputer
    imputer = IterativeImputer()

    # Ajustar o imputer e transformar os dados
    df[numerical_cols] = imputer.fit_transform(df[numerical_cols])
    
    return df
    

if __name__ == "__main__":
    load_dotenv()

    name_file = 'rfr_imdb_processed.csv'
    raw_path = os.getenv('RAW_PATH')
    file = f'{raw_path}/desafio_indicium_imdb.csv'

    prepare_data(file=file, name_file_processed=name_file)