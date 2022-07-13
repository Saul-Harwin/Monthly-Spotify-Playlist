from datetime import date

def get_date(MONTHS):
    dateNum = date.today().strftime("%m")
    year = date.today().strftime("%y")
    return f"{MONTHS.get(dateNum)} {year}"

def get_track_ids(sp, time_frame):
    track_ids = []
    for song in time_frame["items"]:
        track_ids.append(song["id"])
    print("Successfully got track IDs")
    return track_ids

def get_track_features(sp, id):
    meta = sp.track(id)
    # meta
    name = meta["name"]
    album = meta["album"]["name"]
    artist = meta["album"]["artists"][0]["name"]
    spotify_url = meta["external_urls"]["spotify"]
    album_cover = meta["album"]["images"][0]["url"]
    track_info = [name, album, artist, spotify_url, album_cover]
    return track_info

def create_playlist(sp, MONTHS):
    date = get_date(MONTHS)
    playlist_name = f"Songs of {date}"    
    sp.user_playlist_create("saulharwin", playlist_name, public=True, collaborative=False, description='')
    print(f"Successfully created playlist ({playlist_name})")
    return playlist_name

def add_songs_to_playlist(sp, trackIDs, playlist_name):
    playlists = sp.user_playlists("saulharwin")
    for playlist in playlists['items']:
        if playlist['name'] == playlist_name:
            sp.playlist_add_items(playlist["id"], trackIDs, position=None)
            break
        else:
            print("ERROR: Playlist hasn't been created yet.")
            return
    print("Successfully added songs to playlist")
    print("Songs:")
    for i in trackIDs:
        print(get_track_features(sp, i))