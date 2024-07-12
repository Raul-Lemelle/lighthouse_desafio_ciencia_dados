import pandas as pd

def load_and_prepare_data(file_path):
    # Carregar os dados do arquivo CSV
    df = pd.read_csv(file_path)
    
    # Converte a coluna Gross em numérica
    df['Gross'] = df['Gross'].replace({'\\$': '', ',': ''}, regex=True).astype(float)
    
    return df

def preprocess_data(df):
    # Tratar valores não numéricos em 'Released_Year'
    df['Released_Year'] = pd.to_numeric(df['Released_Year'], errors='coerce')
    df['Released_Year'] = df['Released_Year'].fillna(df['Released_Year'].median())
    df['Released_Year'] = df['Released_Year'].astype(int, errors='ignore')
    
    # Remover o sufixo ' min' e converter 'Runtime' para int
    df['Runtime'] = df['Runtime'].str.replace(' min', '')
    df['Runtime'] = pd.to_numeric(df['Runtime'], errors='coerce')
    df['Runtime'] = df['Runtime'].fillna(df['Runtime'].median())
    df['Runtime'] = df['Runtime'].astype(int)

    return df
