import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=e7089f5b14cb851e610505e4975b5415&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])

    recommended_movies = []
    recommended_movies_poster = []
    for i in distances[1:6]:
        # fetch poster from API
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_poster

st.title('Movies Recommender System')
movies = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movies_list = movies['title'].values
selected_movie_name = st.selectbox('Type or Select any movie from list', movies_list)

if st.button('View Recommendation'):
    recommended_movies, recommended_movies_poster = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movies[0])
        st.image(recommended_movies_poster[0])

    with col2:
        st.text(recommended_movies[1])
        st.image(recommended_movies_poster[1])

    with col3:
        st.text(recommended_movies[2])
        st.image(recommended_movies_poster[2])

    with col4:
        st.text(recommended_movies[3])
        st.image(recommended_movies_poster[3])

    with col5:
        st.text(recommended_movies[4])
        st.image(recommended_movies_poster[4])
