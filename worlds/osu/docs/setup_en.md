# Setup Guide for osu! for MultiworldGG

## Account Setup

* Go to your account settings at [https://osu.ppy.sh/home/account/edit](https://osu.ppy.sh/home/account/edit), you will need to make an account if you don't have one
* Scroll down to "OAuth" and Click 'New OAuth Application'
* Name it something informative, Such as (Name) osu!MWGG Client
* In Application Callback URLs, type http://localhost:3914 (It shouldn't matter in theory, but it could in the future)
* Click Register Application
* You should now have an OAuth App. Copy the Client ID and Client Secret for later. Do Not Share Your Client Secret. You can always reset it though, so don't panic if a mistake happens. You will also need your user ID, which can be found in your profile link (i.e.: If the URL is https://osu.ppy.sh/users/10794430 the ID is 10794430)

## Join a MultiworldGG Session
* Launch The usu! Client through the MultiworldGG Launcher. 
* You will need to input your Client ID, Client Secret, and Player ID. You can enter these with the commands. /set_client_id, /set_api_key, and /set_player_id respectfully. 
* Afterwards use /save_keys to store them to a file, and use /load_keys on future launches.

### Commands for Play
* To See What Songs you have in Logic, use /songs. You may use /download with a Song # to download that song (The Number before the :, not the Id.) or simply "next" to grab the next song in logic. 
* All Songs will show their Name and Beatmapset IDs, to make sure you have the exact right version.

### Auto Tracking
* After Loading your Keys, use /Auto_Track [mode] to track a given mode. The Valid Modes are Osu, Taiko, Fruits, Mania. 
* osu!ap will check for new scores every 4 seconds, so please wait a moment before a song will send its items. Converts will count as the mode they are played in. 
* Other useful commands include /auto_download which will download the next song after a clear, and /download_type which can let you switch to osu!direct downloads. 
* All of these settings can be saved and loaded with /save_settings and /load_settings respectively. Once both settings and keys have been saved, you can also use /load_all to immedietely jump back into playing.
* If the Score you set correlates to a song you have received/started with, it will send when you use /update, or every 4(ish) seconds with auto track.
* After Obtaining the Correct Amount of "Preformance Points" (Music Sheets) Your Goal Song will Show in /songs. Clearing it and getting your last scores will goal your game.