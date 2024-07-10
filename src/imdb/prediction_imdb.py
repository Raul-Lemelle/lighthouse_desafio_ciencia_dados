import pandas as pd
import joblib
import os

def predict_imdb_rating(new_movie, model_path):
    model_filename = os.path.join(model_path, 'model_imdb_rating.pkl')
    model = joblib.load(model_filename)

    new_movie_df = pd.DataFrame([new_movie])
    new_movie_df['Gross'] = new_movie_df['Gross'].replace({'\$': '', ',': ''}, regex=True).astype(float)
    new_movie_df['Released_Year'] = new_movie_df['Released_Year'].astype(int)
    new_movie_df['Runtime'] = new_movie_df['Runtime'].str.replace(' min', '').astype(int)
    
    predicted_rating = model.predict(new_movie_df)
    return predicted_rating[0]
