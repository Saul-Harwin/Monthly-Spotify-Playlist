import spotipy
from spotipy.oauth2 import SpotifyOAuth
import constants as const
from helpers import *
from datetime import date, datetime
import sys
import time


def playlist(sp, results, create_playlist, name):
    try:
        playlist_name = create_playlist(sp, name)
    except SpotifyException as e:
        print(f'An error occurred: {e}')
        print('Program will try again in 5 mintues')
        print('waiting...')
        time.sleep(300)
        print('Rerunning create_playlist')
        try:
            playlist_name = create_playlist(sp, name)
        except SpotifyException as e:
            print("An error occurred:", e)
            print('Program Failed to Finish')
            return
        
    if playlist_name == "ERROR":
        print("Error")
        return

    trackIDs = get_track_ids(sp, results)
    add_songs_to_playlist(sp, trackIDs, playlist_name)


def run():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=const.SPOTIPY_CLIENT_ID, client_secret=const.SPOTIPY_CLIENT_SECRET, redirect_uri=const.SPOTIPY_REDIRECT_URI, scope=const.SCOPE, open_browser=True, cache_path=const.CACHE_PATH))
    month_results = sp.current_user_top_tracks(limit=25, offset=0, time_range="short_term")
    long_results  = sp.current_user_top_tracks(limit=50, offset=0, time_range="long_term")

    # Month Playlist
    playlist(sp, month_results, create_monthly_playlist, const.MONTHS)

    # Long Term 
    playlist(sp, long_results, create_long_playlist, "Favourites")
    
    send_email(sp, long_results)

if __name__ == "__main__":
    print("\n")
    print(datetime.now())
    run()
