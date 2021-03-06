#!/usr/bin/env python

import sys
import pprint
import vk_api

import spotipy
import spotipy.util as util

# Python 2 and 3
from builtins import input

# provide Spotify user name here
spotify_user = ''

# Provide vkontakte email/pass here
vk_email = ''
vk_pass = ''

# when you sign-in to your vkontakte account in browser and go to your profile,
# it shows you the id in the URL. 
vk_id = ''

def get_sms_code():
    code = input('input code from sms\n')
    print('code received: {}'.format(code))
    return code

vk_session = vk_api.VkApi(vk_email, vk_pass, auth_handler=get_sms_code)
try:
    vk_session.authorization()
except vk_api.AuthorizationError as error_msg:
    print(error_msg)
    quit()
vk = vk_session.get_api()
songs = vk.audio.get(owner_id=vk_id)['items']

print('You have {} songs'.format(len(songs)))

scope = 'playlist-modify-private'
token = util.prompt_for_user_token(spotify_user, scope)

if token:
    print("Got token for {}".format(spotify_user))
else:
    print("Can't get token for {}".format(spotify_user))
    quit()

sp = spotipy.Spotify(auth=token)
sp.trace = False

playlists = sp.user_playlists(spotify_user)

# TODO search the required playlist instead of taking the first one
playlist = playlists['items'][0]

for i, song in enumerate(songs):
    for string_template in [u'{} {}', u'\'{}\' OR \'{}\'', u'{}']:
        search_str = string_template.format(song['title'], song['artist'])
        print(u'Searching {}/{} - {}'.format(i, len(songs), search_str))
        result = sp.search(search_str)
        items = result['tracks']['items']
        if len(items) > 0:
            print(u"Found: \"{}\", adding to {}".format(items[0]['name'], playlist['name']))
            sp.user_playlist_add_tracks(spotify_user, playlist['uri'], [items[0]['id']])
            break
        else:
            print(u"Not found")

