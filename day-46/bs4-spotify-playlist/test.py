import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID="c8a92eeb906943aaaf8621e7894df0e9"
CLIENT_SECRET="e4a0b7099f9d401cba8956c86efdc341"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri="http://example.com",
                                               scope="user-library-read"))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])