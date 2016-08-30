# shows artist info for a URN or URL

import sys
import pprint
import json

import spotipy
import spotipy.util as util

# provide the user name here
username = ""

songs = []
with open('songs.json', 'r') as f:
    songs = json.load(f)

scope = 'playlist-modify-private'
token = util.prompt_for_user_token(username, scope)

if token:
    print("Got token for {}".format(username))
else:
    print("Can't get token for {}".format(username))
    quit()

sp = spotipy.Spotify(auth=token)
sp.trace = False

playlists = sp.user_playlists(username)

print(playlists['items'][0])
print(playlists['items'][0]['uri'])
print(playlists['items'][0]['name'])
print(playlists['items'][0]['id'])

for i, song in enumerate(songs):
    search_str = '{} {}'.format(song['artist'], song['title'])
    print('Searching {}/{} - {}'.format(i, len(songs), search_str))
    result = sp.search(search_str)
    items = result['tracks']['items']
    if len(items) > 0:
        print("Found {}, adding to the playlist".format(items[0]['id']))
        results = sp.user_playlist_add_tracks(username, playlists['items'][0]['uri'], items[0]['id'])
        print(results)
