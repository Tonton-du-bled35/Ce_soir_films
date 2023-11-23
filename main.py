import requests

url = 'https://api.themoviedb.org/3/movie/11'
params = {
    'api_key': '0600b7eb309eab604656515827689e1b'
}

response = requests.get(url, params=params)

if response.status_code == 200:
    movie_data = response.json()
    # Utilisez movie_data pour traiter les données du film
    # print(movie_data)
else:
    print(f"La requête a échoué avec le code d'état {response.status_code}")

print(movie_data["poster_path"])

image=movie_data["poster_path"]