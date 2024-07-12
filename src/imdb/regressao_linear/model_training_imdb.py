import os
import joblib
from dotenv import load_dotenv
from sklearn.model_selection import train_test_split # divisão dos dados de treino e teste
from sklearn.preprocessing import OneHotEncoder # Converte variáveis categóricas em número
from sklearn.linear_model import LinearRegression # Modelo de Regressão Linear
from sklearn.compose import ColumnTransformer # Aplicar diferentes transformações a diferentes subconjuntos de colunas
from sklearn.pipeline import Pipeline # Encadear etapas de transformação sequencialmente
from sklearn.impute import SimpleImputer # utilizado em valores ausentes

def train_and_save_model(df, model_path):
    X = df.drop(['IMDB_Rating', 'Unnamed: 0', 'Overview'], axis=1) # dados de treino
    y = df['IMDB_Rating'] # dados alvo

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    numeric_features = ['Meta_score', 'No_of_Votes', 'Gross', 'Released_Year', 'Runtime']
    categorical_features = ['Certificate', 'Genre', 'Director', 'Star1', 'Star2', 'Star3', 'Star4']

    numeric_transformer = SimpleImputer(strategy='mean') # Substituir os valores ausentes pela média dos valores não ausentes na mesma coluna.
    categorical_transformer = Pipeline(steps=[
        # nome do passo, transformador
        ('imputer', SimpleImputer(strategy='constant', fill_value='missing')), # substituir os valores ausentes pela string 'missing'
        ('onehot', OneHotEncoder(handle_unknown='ignore')) # Converte variáveis categóricas em número
    ])

    preprocessor = ColumnTransformer(
        # cada transformerrs é uma tupla com 3 elementos (nome do transformador, tranformador, colunas alvo)
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)
        ])

    model = Pipeline(steps=[
        # nome do passo, transformador
        ('preprocessor', preprocessor),
        ('regressor', LinearRegression())
        ])

    # treinamento do modelo
    model.fit(X_train, y_train)

    # salva o .pkl
    load_dotenv()

    models_path = os.getenv('MODELS_PATH')
    path_and_namefile = f'{models_path}/modelo_regressao_linear_imdb_rating.pkl'
    joblib.dump(model, path_and_namefile)

    return model, X_test, y_test