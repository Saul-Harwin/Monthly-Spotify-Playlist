from datetime import date, datetime
from constants import MONTHS, USERNAME
import smtplib, ssl


def get_date(MONTHS):
    dateNum = date.today().strftime("%m")
    year = date.today().strftime("%y")
    print(dateNum)
    return f"{MONTHS.get(str(int(dateNum)))} {year}"

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

def create_monthly_playlist(sp, MONTHS):
    date = get_date(MONTHS)
    print(date)
    playlist_name = f"Songs of {date}"
    playlists = sp.user_playlists(USERNAME)

    for playlist in playlists["items"]:
        if playlist["name"] == playlist_name:
            sp.playlist_change_details(playlist_id=playlist["id"], description=f"This is my playlist of top songs this month automatically populated by my Rpi. Last Updated: {datetime.now().day}/{datetime.now().month}/{datetime.now().year} at {datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}")
            print("Playlist with the same name already exist. Skipping playlist creation.")
            return playlist_name
        else:
            continue

    if len(playlists["items"]) > 0:
        sp.user_playlist_create(USERNAME, playlist_name, public=True, collaborative=False, description=f"This is my playlist of top songs this month automatically populated by my Rpi. Last Updated: {datetime.now().day}/{datetime.now().month}/{datetime.now().year} at {datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}")
        print(f"Successfully created playlist ({playlist_name})")
        return playlist_name
    else:
        return "ERROR"

def create_long_playlist(sp, playlist_name):
    playlists = sp.user_playlists(USERNAME)

    for playlist in playlists["items"]:
        if playlist["name"] == playlist_name:
            sp.playlist_change_details(playlist_id=playlist["id"], description=f"This is my playlist of top songs this month automatically populated by my Rpi. Last Updated: {datetime.now().day}/{datetime.now().month}/{datetime.now().year} at {datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}")
            print("Playlist with the same name already exist. Skipping playlist creation.")
            return playlist_name
        else:
            continue

    if len(playlists["items"]) > 0:
        sp.user_playlist_create(USERNAME, playlist_name, public=True, collaborative=False, description=f"This is my playlist of top songs this month automatically populated by my Rpi. Last Updated: {datetime.now().day}/{datetime.now().month}/{datetime.now().year} at {datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}")
        print(f"Successfully created playlist ({playlist_name})")
        return playlist_name
    else:
        return "ERROR"

def add_songs_to_playlist(sp, trackIDs, playlist_name):
    playlists = sp.user_playlists(USERNAME)
    for playlist in playlists['items']:
        if playlist['name'] == playlist_name:
            items = sp.playlist_items(playlist["id"])
            if items["total"] == 0:
                sp.playlist_add_items(playlist["id"], trackIDs, position=None)
            else:
                sp.playlist_replace_items(playlist["id"], trackIDs) 
            print("Successfully added songs to playlist")
            print("Songs:")
            for i in trackIDs:
                print(get_track_features(sp, i))
            return
        else:
            continue
    print("ERROR: Playlist hasn't been created yet.")
    return
    
def send_email(sp, tracks):
    print(tracks)
    sp.audio_features(tracks)
    
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "thisismytestemail71@gmail.com"  # Enter your address
    receiver_email = "saulharwin@gmail.com"  # Enter receiver address
    password = "TestyTestyTesty"
    message = """\
    Subject: Hi there

    This message is sent from Python."""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        
