# This module is responsible for user input.

import os

class UserIOHandle:
    def __init__(self) -> None:
        self.menu_choice = None
        self.track_choice = None

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_menu(self):
        self.clear_screen()
        print('\n\tSpotify Application')
        print('\t-------------------\n')
        print('\t1. Show Top Tracks.\n\t2. Create Playlist with Top Tracks.\n\t3. Exit.\n\n')
        self.menu_choice = int(input('\tEnter your Choice: '))

    def get_choice(self):
        return self.menu_choice

    def show_track_menu(self):
        limit = int(input('\n\tEnter number of tracks: '))
        print('\n\tEnter Time range.\n')
        print('\t1. Short Term (approx. last 4 weeks data).\n\t2. Medium Term (approx. last 6 months data).\n\t3. Long Term (approx. last 1 year data).\n\n')
        choice = int(input('\tEnter your Choice: '))

        term = None
        if choice == 1:
            term = 'short_term'
        elif choice == 2:
            term = 'medium_term'
        elif choice == 3:
            term = 'long_term'

        self.track_choice = {
            'limit': limit,
            'time_range': term
        }

    def get_track_choice(self):
        return self.track_choice
    
    def show_track_details(self, track_list):
        print(f'\n\tTop {len(track_list)} Tracks in your Spotify.')
        print('\t-------------------------------\n')
        for idx, track in enumerate(track_list):
            print(f'{idx + 1}:: Track: {track['name']}, Artist: {track['artist']}')
        input('\nPress any key to continue... ')

    def get_playlist_info(self):
        playlist_name = input('\n\tEnter the playlist name: ')
        playlist_desc = input('\tEnter the description of the playlist: ')
        return (playlist_name, playlist_desc)
    