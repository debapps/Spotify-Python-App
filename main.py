# This code is used to demonstrate the Spotify API. It login to specific Spotify account,
# and get the top musical tracks of the profile. Then, it creates a playlist and add
# those tracks into the new playlist.

from spotify_handler import SpotifyHandle
from user_inout_handler import UserIOHandle

# Initialize the application.
io = UserIOHandle()
sp = SpotifyHandle()
top_tracks = None

def main():
    global top_tracks

    while io.get_choice() != 3:
        # Show Application Menu.
        io.show_menu()

        if io.get_choice() == 1:
            handle_track_details()

        elif io.get_choice() == 2:
            if top_tracks == None:
                handle_track_details()
            
            create_playlist()
            io.clear_screen()

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

    # Clear screen and display track details.
    io.clear_screen()
    io.show_track_details(top_tracks)


def create_playlist():
    global top_tracks
    
    playlist_info = io.get_playlist_info()
    sp.create_new_playlist(playlist_info[0], playlist_info[1], top_tracks)
    input('\nPress any key to continue... ')


if __name__ == '__main__':
    main()