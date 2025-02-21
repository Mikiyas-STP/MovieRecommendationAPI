# Movie Recommendation System
## *Introduction*  
This **Movie Recommendation System** project is built using **Streamlit and The Movie Database (TMDB) API**. It allows users to search for a movie and get recommendations based on similar titles. The goal of this project is to explore API integration and basic data handling in Python.
## How Does It Work  
Enter a movie name in the search bar.  
Then app fetches details about the movie including its title,release year,rating and an overview.  
It also provides a list of similar movies based on the TMDB recommendation system.  

## What You Need to Run This Project  
- Python3
- A TMDB API Key from https://www.themoviedb.org/

## *Setting Up the Project* 

1. Download the project
2. Install the required libraries
   pip install -r requirements.txt
3. Customise by adding your TMDB API key in `app.py`  
   API_KEY = "your_api_key_here"
4. Run the application  
streamlit run app.py   
   
## *Features*  
- Search for any movie and get its details.
- See a list of recommended movies based on the one you searched.
- Get real-time movie data using TMDB API.

## *Future Improvements* 
- Allow users to filter recommendations by genre.  

👤  Mikiyas Gebremichael  
    mikiyasgebremichaell@gmail.com