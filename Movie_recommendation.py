import pandas as pd

# Sample movie data
movies = {
    'movie': ['The Matrix', 'Inception', 'Interstellar', 'Avengers', 'Avatar', 'Jurassic Park', 'Terminator', 'Gladiator'],
    'genre': ['Sci-fi', 'Sci-fi', 'Sci-fi', 'Superhero', 'Sci-fi', 'Adventure', 'Sci-fi', 'Drama']
}

df = pd.DataFrame(movies)

def recommend_movies(genre):
    """Recommend all movies of the given genre."""
    recommendations = df[df['genre'].str.lower() == genre.lower()]
    return recommendations

print("We have following genres: Sci-fi, Superhero, Adventure, Drama.")
user_genre = input("Enter a genre you like: ")
result = recommend_movies(user_genre)

if not result.empty:
    print(f"Movies you might like in {user_genre} genre:")
    print(result)
else:
    print("Sorry, we don't have any movies in this genre.")
