import pandas as pd

def load_and_prepare_data(file_path):
    # Converte a coluna Gross em numérica
    df = pd.read_csv(file_path)
    df['Gross'] = df['Gross'].replace({'\$': '', ',': ''}, regex=True).astype(float)
    return df

def preprocess_data(df):
    # Converta colunas categóricas em identificadores numéricos
    df['Released_Year'] = df['Released_Year'].astype(int)
    df['Runtime'] = df['Runtime'].str.replace(' min', '').astype(int)
    return df