# This code is used to demonstrate the Spotify API. It login to specific Spotify account,
# and get the top musical tracks of the profile. Then, it creates a playlist and add
# those tracks into the new playlist.

from spotify_handler import SpotifyHandle
from user_inout_handler import UserIOHandle

# Initialize the application.
io = UserIOHandle()
sp = SpotifyHandle()
top_tracks = None
playlists = None

def main():
    '''The main application.'''

    global top_tracks, playlists

    while io.get_choice() != 5:
        # Show Application Menu.
        io.show_menu()

        if io.get_choice() == 1:
            handle_track_details()

        elif io.get_choice() == 2:
            if top_tracks == None:
                handle_track_details()    
            create_playlist()
            
        elif io.get_choice() == 3:
            show_playlists()
            input('\nPress any key to continue... ')
            # Clear screen
            io.clear_screen()

        elif io.get_choice() == 4:
            show_playlists()
            playlist_choice = int(input('\nPlease enter the playlist number to delete: '))
            if playlist_choice < 0 or playlist_choice > len(playlists):
                input('ERROR: Invalid playlist choice!')
            else:
                id = playlists[playlist_choice - 1]['id']
                sp.delete_playlist(id)

        else:
            print('\n\tThanks for using Spotify App!')
            

def handle_track_details():
    '''This function handles track details.'''

    global top_tracks

    io.show_track_menu()
    track_choice = io.get_track_choice()
    limit = track_choice['limit']
    time_range = track_choice['time_range']

    # Get top tracks.
    top_tracks = sp.get_top_tracks(limit=limit, time_range=time_range)

    io.show_track_details(top_tracks)


def create_playlist():
    '''This function creates playlist.'''
    global top_tracks
    
    playlist_info = io.get_playlist_info()
    sp.create_new_playlist(playlist_info[0], playlist_info[1], top_tracks)

    input('\nPress any key to continue... ')
    # Clear screen
    io.clear_screen()

def show_playlists():
    '''This method displays current user's playlists.'''

    global playlists
    playlists = sp.get_playlists()
    io.show_playlists_info(playlists)
    
    

if __name__ == '__main__':
    main()