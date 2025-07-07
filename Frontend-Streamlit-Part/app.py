import streamlit as st
import pickle
import pandas as pd
import requests

# TMDB API Key
TMDB_API_KEY = 'e7089f5b14cb851e610505e4975b5415'

# Load movie data and similarity matrix
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Function to fetch movie details including trailer link
def fetch_movie_details(movie_id):
    # Details URL
    details_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
    details_resp = requests.get(details_url).json()

    poster_path = details_resp.get('poster_path')
    poster_url = f"https://image.tmdb.org/t/p/w500/{poster_path}" if poster_path else None

    genres = [genre['name'] for genre in details_resp.get('genres', [])]
    rating = round(details_resp.get('vote_average', 0.0), 2)
    runtime = details_resp.get('runtime', 'N/A')
    overview = details_resp.get('overview', 'No description available.')

    # Trailer URL
    videos_url = f"https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key={TMDB_API_KEY}&language=en-US"
    videos_resp = requests.get(videos_url).json()
    trailer_url = None
    for video in videos_resp.get('results', []):
        if video['type'] == 'Trailer' and video['site'] == 'YouTube':
            trailer_url = f"https://www.youtube.com/watch?v={video['key']}"
            break

    return poster_url, genres, rating, runtime, overview, trailer_url

# Recommendation function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])

    recommended_data = []

    for i in distances[1:7]:
        movie_id = movies.iloc[i[0]].movie_id
        title = movies.iloc[i[0]].title
        poster, genres, rating, runtime, overview, trailer = fetch_movie_details(movie_id)

        recommended_data.append({
            'title': title,
            'poster': poster,
            'genres': genres,
            'rating': rating,
            'runtime': runtime,
            'overview': overview,
            'trailer': trailer
        })

    return recommended_data

# Streamlit App UI
st.set_page_config(page_title="🎬 Movie Recommender", layout="wide")
st.title("🎬 Movie Recommender System")

# Movie selection
movies_list = movies['title'].values
selected_movie_name = st.selectbox('Type or select a movie from the list:', movies_list)

# Recommendation trigger
if st.button('View Recommendation'):
    with st.spinner("Finding similar movies..."):
        recommended_data = recommend(selected_movie_name)

    st.subheader("🎯 Top 6 Recommendations for You")

    for row in range(0, len(recommended_data), 3):
        cols = st.columns(3)
        for idx in range(3):
            if row + idx < len(recommended_data):
                movie = recommended_data[row + idx]
                with cols[idx]:
                    st.image(movie['poster'], use_container_width=True)
                    st.markdown(f"### {movie['title']}")
                    st.markdown(f"⭐ **{movie['rating']:.2f}** | 🕒 {movie['runtime']} mins")
                    st.markdown(f"**Genres:** {', '.join(movie['genres'])}")
                    st.markdown(f"**Overview:** {movie['overview'][:150]}...")
                    if movie['trailer']:
                        trailer_button_html = f"""
                            <a href="{movie['trailer']}" target="_blank">
                                <button style="
                                    background-color: #E50914;
                                    color: white;
                                    padding: 8px 16px;
                                    border: none;
                                    border-radius: 5px;
                                    font-size: 14px;
                                    cursor: pointer;
                                    margin-top: 10px;
                                ">
                                    🎥 Watch Trailer
                                </button>
                            </a>
                        """
                        st.markdown(trailer_button_html, unsafe_allow_html=True)
