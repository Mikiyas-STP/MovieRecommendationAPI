#First i imported the streamlit for building the web app, PIL for handling images, requests to make API calls
#pandas for data handling and visualization and matplotlib charts for plotting charts
import streamlit as st
from PIL import Image
import requests
import pandas as pd
import matplotlib.pyplot as plt

#This are my TMDB API configurations including my API key for TMDB, base URL for TMDB API endpoints and fetching movie poster.
API_KEY = "2b3f8afa26414702391d4b79abba9ffb"
BASE_URL = "https://api.themoviedb.org/3"
IMAGE_URL = "https://image.tmdb.org/t/p/w500"

#Here i write my Function to search for a movie based on user input.
def search_movie(movie_name):
    url = f"{BASE_URL}/search/movie?api_key={API_KEY}&query={movie_name}"
    response = requests.get(url)
    if response.status_code != 200:
        st.error("Failed to retrieve data from TMDB API.")
        return None
    data = response.json()
    return data["results"][0] if data["results"] else None

#This is the Function to get movie recommendations based on a given movie ID
def get_recommendations(movie_id):
    url = f"{BASE_URL}/movie/{movie_id}/recommendations?api_key={API_KEY}"
    response = requests.get(url)
    if response.status_code != 200:
        st.error("Failed to fetch recommendations.")
        return []
    data = response.json()
    return data.get("results", [])

#Streamlit UI setup
st.title("🎬 Movie Recommendation & Analysis System")

#User input for movie search
movie_name = st.text_input("Enter a movie name:")
if movie_name:
    movie = search_movie(movie_name)
    if movie:
        #This code displays movie details
        st.subheader(f"📽 {movie['title']} ({movie['release_date'][:4] if 'release_date' in movie else 'N/A'})")
        if movie.get("poster_path"):
            st.image(IMAGE_URL + movie["poster_path"], caption=movie["title"], width=300)
        st.write("⭐ Rating:", movie.get("vote_average", "N/A"))
        st.write("📝 Overview:", movie.get("overview", "No description available."))      
        #This code fetch recommendations for the selected movie
        recommendations = get_recommendations(movie["id"])
        if recommendations:
            st.subheader("🎞 Recommended Movies:")
            movie_data = []
            for rec in recommendations[:5]:  #This limits to 5 recommendations.
                st.write(f"🎥 {rec['title']} ({rec.get('release_date', 'N/A')[:4]})")
                movie_data.append({
                    "Title": rec["title"],
                    "Release Year": rec.get("release_date", "N/A")[:4]
                })
            #This converts recommendations into a dataframe.
            df = pd.DataFrame(movie_data)
            df["Release Year"] = pd.to_numeric(df["Release Year"], errors='coerce')
            #This is the visualization for movies released over the years
            st.subheader("📈 Movie Releases Over the Years")
            fig, ax = plt.subplots()
            df.dropna(subset=["Release Year"], inplace=True)
            df["Release Year"].value_counts().sort_index().plot(kind="line", marker="o", ax=ax)
            plt.xlabel("Year")
            plt.ylabel("Number of Movies")
            plt.title("Number of Recommended Movies Over the Years")
            st.pyplot(fig)
        else:
            st.write("No recommendations found.")
    else:
        st.error("Movie not found! Please try another movie.")