import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['title']== movie].index[0]
    distance = similarity[movie_index]

    movies_list = sorted(list(enumerate(distance)),reverse = True, key = lambda x:x[1])[1:6]

    recommended_movies=[]
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
        return reccommended_movies



movie_dict = pickle.load(open('movie_dict.pkl' , 'wb'))
movies = pd.DataFrame(movie_dict)


st.title("Movie Recommendation System")

selected_movie_name = st.selectbox("Enter the name of movie", movies['title'].values)


if st.butten('Recommend'):
    recommendation = recommend(selected_movie_name)
    for i in recommendeation:
     st.write("i")