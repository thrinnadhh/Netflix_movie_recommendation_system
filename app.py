import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_id = movies[movies.title == movie].index[0]
    recommended_movie_ids = similarity[movie_id]
    recommend_movies_dataframe = movie_titles.loc[recommended_movie_ids]
    recommended=[]
    for i in recommend_movies_dataframe.title:
        recommended.append(i)
    return recommended

movie_titles = pickle.load(open('movies.pkl', 'rb'))

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity= pickle.load(open('similar_movie.pkl', 'rb'))


st.title('Netflix Movie Recommendation System')
selected_movie_name = st.selectbox('Type the movie name (recommendation based on movie-movie)',
movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)

