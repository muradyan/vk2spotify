# vk2spotify

Scripting to help exporting your Vkontakte playlist into Spotify

This is still in early development (PoC), however it works.

## Installing prerequisites 

Requirements:
```
pip install vk_api pyspotify
```

## Authentication

You need to set the following environment variables:

```
export SPOTIPY_CLIENT_ID='your-spotify-client-id'
export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
export SPOTIPY_REDIRECT_URI='your-app-redirect-url'
```

Get your credentials at https://developer.spotify.com/my-applications
*NOTE*: You may need to create application, if you haven't so far.

Then set the following variables in the **run.py**:

* spotify_user - if you're using Facebook for login, don't put the e-mail, more info here: https://community.spotify.com/t5/Accounts-and-Subscriptions/How-do-i-find-my-username-when-using-Facebook-login/td-p/859795
* vk_email - this is your vkontakte e-mail address
* vk_pass - vkontakte password
* vk_id - you can get the vkontakte id when you login to your account in the
browser. Then you go to your profile and get the id from the browser URL
(only the numbers, without 'id')

