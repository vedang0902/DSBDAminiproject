import streamlit as st
import h5py
import random

def load_h5_file(filepath):
    try:
        with h5py.File(filepath, 'r') as file:
            for key in file.keys():
                print(f" - {key}")
            return list(file.keys())
    except Exception as e:
        st.error(f"Error loading H5 file: {e}")
        return []

# Movie database with genre classifications and mood associations
movie_database = {
    "Action": {
        "Any mood": ["The Bourne Identity", "Die Hard", "John Wick"],
        "Feel like laughing": ["Deadpool", "The Nice Guys", "Rush Hour"],
        "Feel like crying": ["Gladiator", "Logan", "Braveheart"],
        "Feel like thinking": ["Inception", "The Matrix", "Edge of Tomorrow"],
        "Feel like an adventure": ["Mission Impossible", "Mad Max: Fury Road", "Raiders of the Lost Ark"],
        "Feel like being scared": ["Predator", "Aliens", "The Descent"]
    },
    "Adventure": {
        "Any mood": ["Indiana Jones", "Jurassic Park", "The Mummy"],
        "Feel like laughing": ["Pirates of the Caribbean", "Jumanji", "The Goonies"],
        "Feel like crying": ["Up", "Life of Pi", "The Revenant"],
        "Feel like thinking": ["Interstellar", "Contact", "Avatar"],
        "Feel like an adventure": ["Lord of the Rings", "The Hobbit", "National Treasure"],
        "Feel like being scared": ["Jurassic Park", "Kong: Skull Island", "Prometheus"]
    },
    "Comedy": {
        "Any mood": ["The Hangover", "Superbad", "Bridesmaids"],
        "Feel like laughing": ["Dumb and Dumber", "Anchorman", "The 40-Year-Old Virgin"],
        "Feel like crying": ["50/50", "The Farewell", "Little Miss Sunshine"],
        "Feel like thinking": ["The Grand Budapest Hotel", "Being John Malkovich", "Jojo Rabbit"],
        "Feel like an adventure": ["The Secret Life of Walter Mitty", "Pineapple Express", "Game Night"],
        "Feel like being scared": ["Shaun of the Dead", "Zombieland", "Tucker and Dale vs Evil"]
    },
    "Drama": {
        "Any mood": ["The Shawshank Redemption", "Forrest Gump", "The Green Mile"],
        "Feel like laughing": ["Silver Linings Playbook", "The Intouchables", "The Full Monty"],
        "Feel like crying": ["The Pursuit of Happyness", "A Star is Born", "Marriage Story"],
        "Feel like thinking": ["The Social Network", "Spotlight", "The Imitation Game"],
        "Feel like an adventure": ["Into the Wild", "127 Hours", "Wild"],
        "Feel like being scared": ["Black Swan", "Whiplash", "Nocturnal Animals"]
    },
    "Fantasy": {
        "Any mood": ["Harry Potter", "The Lord of the Rings", "Chronicles of Narnia"],
        "Feel like laughing": ["Shrek", "Enchanted", "Stardust"],
        "Feel like crying": ["Pan's Labyrinth", "Bridge to Terabithia", "The Green Mile"],
        "Feel like thinking": ["The Shape of Water", "Being John Malkovich", "Life of Pi"],
        "Feel like an adventure": ["The Princess Bride", "The Witcher", "The NeverEnding Story"],
        "Feel like being scared": ["Crimson Peak", "The Witches", "Coraline"]
    },
    "Horror": {
        "Any mood": ["The Shining", "Hereditary", "Get Out"],
        "Feel like laughing": ["Cabin in the Woods", "Happy Death Day", "Ready or Not"],
        "Feel like crying": ["Pet Sematary", "The Mist", "Hereditary"],
        "Feel like thinking": ["The Sixth Sense", "Get Out", "The Others"],
        "Feel like an adventure": ["The Descent", "A Quiet Place", "Bird Box"],
        "Feel like being scared": ["The Conjuring", "Sinister", "Insidious"]
    },
    "Mystery": {
        "Any mood": ["Knives Out", "Gone Girl", "Shutter Island"],
        "Feel like laughing": ["Murder Mystery", "Game Night", "Clue"],
        "Feel like crying": ["Mystic River", "Prisoners", "Wind River"],
        "Feel like thinking": ["Memento", "Seven", "The Prestige"],
        "Feel like an adventure": ["National Treasure", "The Da Vinci Code", "Sherlock Holmes"],
        "Feel like being scared": ["The Silence of the Lambs", "The Girl with the Dragon Tattoo", "Zodiac"]
    },
    "Romance": {
        "Any mood": ["The Notebook", "Pride & Prejudice", "500 Days of Summer"],
        "Feel like laughing": ["Crazy Rich Asians", "10 Things I Hate About You", "The Proposal"],
        "Feel like crying": ["The Fault in Our Stars", "Me Before You", "A Walk to Remember"],
        "Feel like thinking": ["Eternal Sunshine of the Spotless Mind", "Her", "Call Me By Your Name"],
        "Feel like an adventure": ["The Tourist", "The Secret Life of Walter Mitty", "Midnight in Paris"],
        "Feel like being scared": ["Warm Bodies", "Crimson Peak", "Spring"]
    },
    "Sci-Fi": {
        "Any mood": ["Star Wars", "Blade Runner", "The Martian"],
        "Feel like laughing": ["Back to the Future", "Men in Black", "Guardians of the Galaxy"],
        "Feel like crying": ["E.T.", "Arrival", "WALL-E"],
        "Feel like thinking": ["Arrival", "Ex Machina", "Blade Runner 2049"],
        "Feel like an adventure": ["Star Wars", "Ready Player One", "Tron: Legacy"],
        "Feel like being scared": ["Alien", "The Thing", "A Quiet Place"]
    },
    "Thriller": {
        "Any mood": ["The Silence of the Lambs", "Gone Girl", "No Country for Old Men"],
        "Feel like laughing": ["Game Night", "Bad Times at the El Royale", "Lock, Stock and Two Smoking Barrels"],
        "Feel like crying": ["Prisoners", "Wind River", "Gone Baby Gone"],
        "Feel like thinking": ["Shutter Island", "Inception", "Fight Club"],
        "Feel like an adventure": ["Source Code", "The Bourne Identity", "North by Northwest"],
        "Feel like being scared": ["Get Out", "Split", "Don't Breathe"]
    },
    "Animation": {
        "Any mood": ["Toy Story", "Finding Nemo", "The Lion King"],
        "Feel like laughing": ["The Lego Movie", "Shrek", "Despicable Me"],
        "Feel like crying": ["Up", "Coco", "Inside Out"],
        "Feel like thinking": ["Inside Out", "WALL-E", "Zootopia"],
        "Feel like an adventure": ["How to Train Your Dragon", "Moana", "Frozen"],
        "Feel like being scared": ["Coraline", "ParaNorman", "Corpse Bride"]
    },
    "Biography": {
        "Any mood": ["The Social Network", "The Theory of Everything", "A Beautiful Mind"],
        "Feel like laughing": ["The Wolf of Wall Street", "The Disaster Artist", "Eddie the Eagle"],
        "Feel like crying": ["The Pursuit of Happyness", "Schindler's List", "12 Years a Slave"],
        "Feel like thinking": ["The Imitation Game", "Hidden Figures", "Spotlight"],
        "Feel like an adventure": ["127 Hours", "Into the Wild", "The Walk"],
        "Feel like being scared": ["Zodiac", "Catch Me If You Can", "American Psycho"]
    }
}

# Duration-based movie recommendations
duration_filters = {
    "Under 90 minutes": ["Toy Story", "Shrek", "The Lion King", "Back to the Future", "A Quiet Place", 
                      "Ready or Not", "Get Out", "Shaun of the Dead", "Zombieland"],
    "90-120 minutes": ["Star Wars", "The Matrix", "Inception", "The Social Network", "The Shawshank Redemption",
                      "Die Hard", "John Wick", "Knives Out", "The Silence of the Lambs"],
    "Over 2 hours": ["The Lord of the Rings", "The Dark Knight", "Interstellar", "Titanic", "Avatar",
                    "Avengers: Endgame", "The Irishman", "Schindler's List", "The Godfather"]
}

def recommend_movies(selected_genres, disliked_genres, mood, duration, favorite_movies=None):
    # Start with an empty list of recommendations
    recommendations = []
    
    # Filter out disliked genres
    filtered_genres = [genre for genre in selected_genres if genre not in disliked_genres]
    
    # If no genres are left after filtering, use defaults
    if not filtered_genres:
        filtered_genres = ["Action", "Comedy", "Drama"]
    
    # Get movies from each selected genre that match the mood
    for genre in filtered_genres:
        if genre in movie_database:
            # If the specific mood exists, use it; otherwise use "Any mood"
            if mood in movie_database[genre]:
                genre_mood_movies = movie_database[genre][mood]
            else:
                genre_mood_movies = movie_database[genre]["Any mood"]
            
            # Add up to 2 random movies from this genre/mood combination
            random_picks = random.sample(genre_mood_movies, min(2, len(genre_mood_movies)))
            recommendations.extend(random_picks)
    
    # Remove duplicates while maintaining order
    unique_recommendations = []
    for movie in recommendations:
        if movie not in unique_recommendations:
            unique_recommendations.append(movie)
    
    # Apply duration filter if specified
    if duration != "Any duration" and duration in duration_filters:
        duration_movies = duration_filters[duration]
        # Filter recommendations to include only those matching the duration
        duration_filtered = [movie for movie in unique_recommendations if movie in duration_movies]
        # If we have matches, use them; otherwise keep original recommendations
        if duration_filtered:
            unique_recommendations = duration_filtered
    
    # If we have favorite movies, use them to boost similar genres (simplified approach)
    if favorite_movies and len(favorite_movies) > 0:
        # This would be where a real recommendation system would use collaborative filtering
        # For now, we'll just ensure we have enough recommendations
        pass
    
    # Shuffle the recommendations for variety
    random.shuffle(unique_recommendations)
    
    # Return top 5 recommendations (or less if we don't have 5)
    return unique_recommendations[:5]

def main():
    st.set_page_config(page_title="Movie Recommendation System", layout="centered")
    
    # Set a seed for reproducible results
    random.seed(42)
    
    # Custom CSS to style the app similar to the HTML version
    st.markdown("""
    <style>
    .main {
        background-color: #f3f4f6;
        color: #1f2937;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .stApp {
        max-width: 800px;
        margin: 0 auto;
    }
    h1 {
        color: #4f46e5;
        text-align: center;
        margin-bottom: 30px;
    }
    .stButton>button {
        background-color: #4f46e5;
        color: white;
        font-weight: 600;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #4338ca;
    }
    .add-movie {
        background-color: #10b981 !important;
    }
    .profile-type {
        text-align: center;
        padding: 10px;
        margin-bottom: 20px;
        background-color: #f0f9ff;
        border-radius: 5px;
        font-weight: 500;
    }
    .movie-card {
        background-color: white;
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 15px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    .movie-title {
        font-weight: bold;
        font-size: 18px;
        margin-bottom: 5px;
    }
    .movie-details {
        color: #6b7280;
        font-size: 14px;
    }
    .recommendation-header {
        margin-top: 30px;
        margin-bottom: 20px;
        color: #4f46e5;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

    st.title("Find Your Perfect Movie")
    
    # Initialize session state for movies
    if 'num_movies' not in st.session_state:
        st.session_state.num_movies = 1
    
    # Profile type selection
    st.markdown('<div class="profile-type">Select your movie personality or customize your preferences below</div>', 
               unsafe_allow_html=True)
    
    # Create a variable for storing profile defaults
    profile_defaults = {
        "Action Lover": ["Action", "Adventure", "Thriller"],
        "Drama Enthusiast": ["Drama", "Romance", "Biography"],
        "Comedy Fan": ["Comedy", "Animation", "Romance"],
        "Sci-Fi Geek": ["Sci-Fi", "Fantasy", "Adventure"],
        "Horror Buff": ["Horror", "Thriller", "Mystery"]
    }
    
    # Use a callback for profile selection
    def on_profile_change():
        profile = st.session_state.profile_select
        if profile in profile_defaults:
            st.session_state.profile_genres = profile_defaults[profile]
        else:
            st.session_state.profile_genres = []
    
    if 'profile_genres' not in st.session_state:
        st.session_state.profile_genres = []
        
    profile_options = ["-- Choose a movie personality --", "Action Lover", "Drama Enthusiast", 
                       "Comedy Fan", "Sci-Fi Geek", "Horror Buff", "Custom Preferences"]
    
    st.selectbox(
        label="",
        options=profile_options,
        key="profile_select",
        on_change=on_profile_change
    )
    
    # User info
    user_id = st.text_input("User ID (leave blank if you're new)")
    name = st.text_input("Your Name", placeholder="What should we call you?")
    
    # Genre preferences section
    st.subheader("What genres do you enjoy? (Select at least 2)")
    
    # Create a 3-column layout for genres
    col1, col2, col3 = st.columns(3)
    
    # Define all genres
    all_genres = {
        "action": "Action", 
        "adventure": "Adventure", 
        "comedy": "Comedy",
        "drama": "Drama", 
        "fantasy": "Fantasy", 
        "horror": "Horror",
        "mystery": "Mystery", 
        "romance": "Romance", 
        "scifi": "Sci-Fi",
        "thriller": "Thriller", 
        "animation": "Animation", 
        "biography": "Biography"
    }
    
    # Group genres by column
    genre_columns = [
        ["action", "drama", "horror", "mystery"],
        ["adventure", "fantasy", "romance", "scifi"],
        ["comedy", "animation", "thriller", "biography"]
    ]
    
    # Display genres in columns
    selected_genres = []
    for i, column in enumerate([col1, col2, col3]):
        with column:
            for genre_key in genre_columns[i]:
                # Check if this genre should be pre-selected based on profile
                default_value = all_genres[genre_key] in st.session_state.profile_genres
                if st.checkbox(all_genres[genre_key], value=default_value, key=f"genre_{genre_key}"):
                    selected_genres.append(all_genres[genre_key])
    
    # Disliked genres
    st.subheader("Are there any genres you dislike? (Optional)")
    
    dislike_col1, dislike_col2, dislike_col3 = st.columns(3)
    
    disliked_genres = []
    with dislike_col1:
        if st.checkbox("Action", key="dislike_action"):
            disliked_genres.append("Action")
    
    with dislike_col2:
        if st.checkbox("Horror", key="dislike_horror"):
            disliked_genres.append("Horror")
    
    with dislike_col3:
        if st.checkbox("Romance", key="dislike_romance"):
            disliked_genres.append("Romance")
    
    # Favorite movies section
    st.subheader("Tell us about movies you've enjoyed (up to 3)")
    
    # Function to add another movie entry
    def add_movie():
        st.session_state.num_movies += 1
    
    # Movie inputs
    favorite_movies = []
    for i in range(st.session_state.num_movies):
        col1, col2 = st.columns([3, 1])
        with col1:
            movie = st.text_input(f"Movie {i+1}", key=f"movie_{i}")
        with col2:
            rating = st.selectbox(
                "Rating", 
                ["★★★★★", "★★★★☆", "★★★☆☆", "★★☆☆☆", "★☆☆☆☆"], 
                key=f"rating_{i}"
            )
        if movie:
            favorite_movies.append({"title": movie, "rating": rating})
    
    # Add more movies button
    if st.session_state.num_movies < 3:
        st.button("+ Add Another Movie", on_click=add_movie, type="primary")
    
    # Mood selection
    mood = st.selectbox(
        "What's your mood today?",
        ["Any mood", "Feel like laughing", "Feel like crying", "Feel like thinking", 
         "Feel like an adventure", "Feel like being scared"]
    )
    
    # Duration selection
    duration = st.selectbox(
        "How much time do you have?",
        ["Any duration", "Under 90 minutes", "90-120 minutes", "Over 2 hours"]
    )
    
    # Submit button
    if st.button("Get Recommendations", type="primary"):
        # Make sure at least one genre is selected
        if not selected_genres:
            st.error("Please select at least one genre you enjoy.")
            return
        
        # Check if H5 file exists and load model data
        try:
            h5_keys = load_h5_file('model_bundle.h5')
            st.success(f"Successfully loaded model with keys: {', '.join(h5_keys)}")
        except:
            st.warning("Model file not found. Using built-in recommendation algorithm instead.")
        
        # Display captured preferences
        st.subheader("Your preferences:")
        st.write(f"User: {name} (ID: {user_id if user_id else 'New user'})")
        st.write(f"Genres you like: {', '.join(selected_genres)}")
        if disliked_genres:
            st.write(f"Genres you dislike: {', '.join(disliked_genres)}")
        st.write(f"Mood: {mood}")
        st.write(f"Duration preference: {duration}")
        
        if favorite_movies:
            st.write("Your favorite movies:")
            for movie in favorite_movies:
                st.write(f"- {movie['title']} ({movie['rating']})")
        
        # Get movie recommendations based on preferences
        recommended_movies = recommend_movies(selected_genres, disliked_genres, mood, duration, favorite_movies)
        
        # Display recommendations
        st.markdown('<h2 class="recommendation-header">🍿 Your Movie Recommendations 🍿</h2>', unsafe_allow_html=True)
        
        if recommended_movies:
            for i, movie in enumerate(recommended_movies):
                st.markdown(f"""
                <div class="movie-card">
                    <div class="movie-title">#{i+1}: {movie}</div>
                    <div class="movie-details">
                        This movie matches your preferences for {', '.join(selected_genres[:2])} and your {mood.lower()} mood.
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
            st.success("Enjoy your movie night! 🎬")
        else:
            st.error("Sorry, we couldn't find any movies matching your preferences. Try adjusting your selections.")

if __name__ == "__main__":
    main()
    
    # This would be used to load the model at startup
    try:
        h5_path = 'model_bundle.h5'
        load_h5_file(h5_path)
    except:
        print("Model file not found. Using built-in recommendation algorithm instead.")