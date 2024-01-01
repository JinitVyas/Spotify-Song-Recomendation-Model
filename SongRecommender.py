import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify API credentials
client_id = 'e0631cf7e9ce4c228e729bde04dfcd69'
client_secret = 'c5c1178eb39540d5933580f67653be06'
redirect_uri = 'http://127.0.0.1:8000/'
scope = 'user-library-read playlist-modify-private playlist-modify-public'
# *****************************************************************
'''set up done'''
# *****************************************************************

# authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))

#start the process of interation
# Step 0: username
username = input("Enter your Spotify username: ")

# Step 1: Get user input for the song name
song_name = input("Enter the name of a song: ")

# Step 2: Search for the song on Spotify
results = sp.search(q=song_name, type='track', limit=1)
if not results['tracks']['items']:
    print("Song not found on Spotify.")
    exit()

# print(results['tracks']['next'])

# Step 3: Extract relevant information about the found track
track_info = results['tracks']['items'][0]
track_name = track_info['name']
track_artist = track_info['artists'][0]['name']
track_id = track_info['id']
# print(f"{track_info} , {track_name} , {track_artist} , {track_id}")
print(f"Found track: {track_name} by {track_artist}")


# Step 4: Implementing recommendation algorithm
# For demonstration purposes, let's recommend a random playlist
# Replace this logic with your own recommendation algorithm
import random

# Get a list of the user's playlists
try:
    user_playlists = sp.current_user_playlists()
except spotipy.SpotifyException as e:
    # Handle the case when the token is not provided or invalid
    if 'No token provided' in str(e):
        print("Authentication token is missing or invalid. Please check your authentication process.")
        exit()
    else:
        # Handle other exceptions
        print(f"An error occurred: {e}")
        exit()

print(user_playlists)
if not user_playlists['items']:
    print("User has no playlists.")
    exit()
else:
    # Recommend a random playlist from the user's playlists
    random_playlist = random.choice(user_playlists['items'])
    recommendation_playlist_id = random_playlist['id']
    recommendation_playlist_name = random_playlist['name']

    print(f"Recommended playlist: {recommendation_playlist_name}")

# Recommend a random playlist from the user's playlists
