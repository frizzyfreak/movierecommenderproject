import pickle
import streamlit as st
import requests as re
import pandas as pd
from streamlit_lottie import st_lottie

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = re.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def load_lottieurl(url: str):
    r = re.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_animation1 = load_lottieurl(r"https://lottie.host/89d4a0c7-3098-438a-9b19-9b6421cb8751/5bOb6fMRs5.json")
lottie_animation2 = load_lottieurl(r"https://lottie.host/119f3d04-4529-40b4-8824-d6d03c70a455/VmDN7sHTXR.json")

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters


st.header('Movie Recommender System')
movies = pickle.load(open(r'movies.pkl','rb'))
movies=pd.DataFrame(movies)
similarity = pickle.load(open(r'similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])

col1, col2 = st.columns(2)

with col1:
    st_lottie(lottie_animation1, height=200, width=200)

with col2:
    st_lottie(lottie_animation2, height=200, width=200)




