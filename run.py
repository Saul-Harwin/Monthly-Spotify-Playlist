import spotipy
from spotipy.oauth2 import SpotifyOAuth
import constants as const
from helpers import *
from datetime import date


def run():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=const.SPOTIPY_CLIENT_ID, client_secret=const.SPOTIPY_CLIENT_SECRET, redirect_uri=const.SPOTIPY_REDIRECT_URI, scope=const.SCOPE))
    results = sp.current_user_top_tracks(limit=20, offset=0, time_range="short_term")
    
    playlist_name = create_playlist(sp, const.MONTHS)
    trackIDs = get_track_ids(sp, results)
    add_songs_to_playlist(sp, trackIDs, playlist_name)

if __name__ == "__main__":
    run()