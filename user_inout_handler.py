# This module is responsible for user input.

import os

class UserIOHandle:
    def __init__(self) -> None:
        self.menu_choice = None
        self.track_choice = None

    def clear_screen(self):
        '''This method clears the display screen.'''

        os.system('cls' if os.name == 'nt' else 'clear')

    def show_menu(self):
        '''This method shows application menu.'''

        self.clear_screen()
        print('\n\tSpotify Application')
        print('\t-------------------\n')
        print('\t1. Show Top Tracks.\n\t2. Create Playlist with Top Tracks.\n\t3. Show user\'s current playlists.\n\t4. Delete existing playlist.\n\t5. Exit.\n\n')
        self.menu_choice = int(input('\tEnter your Choice: '))

    def get_choice(self):
        '''This method returns the application menu choice.'''
        return self.menu_choice

    def show_track_menu(self):
        '''This method shows track related menu.'''

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
        '''This method returns the track related menu choice.'''
        return self.track_choice
    
    def show_track_details(self, track_list):
        '''This methods shows track details from the track list.'''

        self.clear_screen()
        print(f'\n\tTop {len(track_list)} Tracks in your Spotify.')
        print('\t-------------------------------\n')
        for idx, track in enumerate(track_list):
            print(f'{idx + 1}:: Track: {track['name']}, Artist: {track['artist']}')
        input('\nPress any key to continue... ')

    def get_playlist_info(self):
        '''This method takes input related to playlist creation.'''

        playlist_name = input('\n\tEnter the playlist name: ')
        playlist_desc = input('\tEnter the description of the playlist: ')
        return (playlist_name, playlist_desc)
    
    def show_playlists_info(self, playlists):
        '''This method shows playlist information on screen.'''
        
        self.clear_screen()
        print('\tYour Current Playlists:')
        print('\t-----------------------')
        for idx, playlist in enumerate(playlists):
            print(f'\t{idx + 1}. Title: {playlist['name']}, Info: {playlist['desc']}')
        
        