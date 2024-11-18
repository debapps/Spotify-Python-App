# This module is responsible for handling Spotify Web APIs.

from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
# import json

# Load Environment file.
load_dotenv()

# Environment Constants
CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
REDIRECT_URL = os.getenv('SPOTIFY_CALLBACK_URL')
SCOPES = 'playlist-modify-private user-top-read'

class SpotifyHandle:
    def __init__(self) -> None:
        # Create the spotify object.
        self.spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                                 client_secret=CLIENT_SECRET,
                                                                 redirect_uri=REDIRECT_URL,
                                                                 scope=SCOPES))
        # Get the current user id.
        user_data = self.spotify.me()
        self.user_id = user_data['id']

    def get_top_tracks(self, limit=20, time_range='medium_term'):
        '''This function gets top tracks of the user.'''

        raw_data = self.spotify.current_user_top_tracks(limit=limit, time_range=time_range)
        top_track_data = raw_data['items']
        top_track_list = [{'uri': track['uri'], 
            'name': track['name'],
            'artist': track['artists'][0]['name']} for track in top_track_data]
        
        # Get the track data in JSON file.
        # with open('track.json', 'w+') as json_data:
        #     json_data.write(json.dumps(top_track_data))

        return top_track_list
    
    def create_new_playlist(self, name, desc, track_list):
        # Create the playlist.
        playlist_data = self.spotify.user_playlist_create(user=self.user_id, 
                                                 name=name, 
                                                 description=desc,
                                                 public=False, 
                                                 collaborative=False)
        
        playlist_id = playlist_data['id']
        
        # Get the list of track uris.
        track_uri = [track['uri'] for track in track_list]

        # Add the tracks.
        self.spotify.playlist_add_items(playlist_id, track_uri, position=None)

        print(f'\n\tPlaylist created successfully.\n\tName - {name}, ID - {playlist_id}')
        print(f'\n\t{len(track_uri)} songs are added successfully.')

    def get_playlists(self):
        pass


        