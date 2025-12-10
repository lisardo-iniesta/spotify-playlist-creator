#!/usr/bin/env python3
"""
Spotify Playlist Creator - Electronic Discovery
Creates a playlist with tracks from selected electronic/ambient artists.

Setup Instructions:
1. Go to https://developer.spotify.com/dashboard
2. Create a new app (any name, set redirect URI to http://localhost:8888/callback)
3. Copy your Client ID and Client Secret
4. Set environment variables or update the script below:
   - SPOTIPY_CLIENT_ID
   - SPOTIPY_CLIENT_SECRET
   - SPOTIPY_REDIRECT_URI (default: http://localhost:8888/callback)
5. Run: pip install spotipy
6. Run this script
"""

import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Configuration - Set these as environment variables or replace with your credentials
CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID", "")
CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET", "")
REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI", "http://127.0.0.1:8888/callback")

# Artists to include in the playlist
ARTISTS = [
    "Bonobo",
    "Sofia Kourtesis",
    "Bicep",
    "Barry Can't Swim",
    "Moby",
    "Catching Flies",
    "Jamie xx",
    "Moderat",
    "Caribou",
    "Four Tet",
]

# Number of top tracks to add per artist
TRACKS_PER_ARTIST = 3

# Playlist configuration
PLAYLIST_NAME = "Electronic Discovery 🎧"
PLAYLIST_DESCRIPTION = "A curated selection of electronic/ambient music featuring Bonobo, Sofia Kourtesis, Bicep, Barry Can't Swim, Moby, Catching Flies, Jamie XX, Moderat, Caribou, and Four Tet."


def create_spotify_client():
    """Create and authenticate Spotify client."""
    scope = "playlist-modify-public playlist-modify-private"

    return spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            redirect_uri=REDIRECT_URI,
            scope=scope,
            open_browser=True,
        )
    )


def search_artist(sp, artist_name):
    """Search for an artist and return their Spotify ID."""
    results = sp.search(q=f"artist:{artist_name}", type="artist", limit=1)
    artists = results.get("artists", {}).get("items", [])

    if artists:
        return artists[0]["id"], artists[0]["name"]
    return None, None


def get_top_tracks(sp, artist_id, limit=3):
    """Get top tracks for an artist."""
    results = sp.artist_top_tracks(artist_id, country="US")
    tracks = results.get("tracks", [])[:limit]
    return [(t["id"], t["name"]) for t in tracks]


def create_playlist(sp, user_id, name, description):
    """Create a new playlist."""
    playlist = sp.user_playlist_create(
        user=user_id, name=name, public=True, description=description
    )
    return playlist["id"], playlist["external_urls"]["spotify"]


def add_tracks_to_playlist(sp, playlist_id, track_ids):
    """Add tracks to a playlist."""
    # Spotify API limits to 100 tracks per request
    for i in range(0, len(track_ids), 100):
        batch = track_ids[i : i + 100]
        sp.playlist_add_items(playlist_id, batch)


def main():
    print("🎵 Spotify Playlist Creator - Electronic Discovery")
    print("=" * 50)

    # Check credentials
    if not CLIENT_ID or not CLIENT_SECRET:
        print("\n❌ Error: Please set your Spotify API credentials!")
        print("\nInstructions:")
        print("1. Go to https://developer.spotify.com/dashboard")
        print("2. Create a new app")
        print("3. Set redirect URI to: http://localhost:8888/callback")
        print("4. Copy your Client ID and Client Secret")
        print("5. Either:")
        print(
            "   - Set environment variables: SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET"
        )
        print(
            "   - Or edit this script and replace YOUR_CLIENT_ID_HERE and YOUR_CLIENT_SECRET_HERE"
        )
        return

    # Authenticate
    print("\n🔐 Authenticating with Spotify...")
    print("   (A browser window will open for authorization)")
    sp = create_spotify_client()

    # Get current user
    user = sp.current_user()
    user_id = user["id"]
    print(f"✅ Logged in as: {user['display_name']} ({user_id})")

    # Create playlist
    print(f"\n📝 Creating playlist: {PLAYLIST_NAME}")
    playlist_id, playlist_url = create_playlist(
        sp, user_id, PLAYLIST_NAME, PLAYLIST_DESCRIPTION
    )
    print(f"✅ Playlist created!")

    # Collect tracks from all artists
    all_track_ids = []
    print(f"\n🔍 Searching for artists and their top tracks...")

    for artist_name in ARTISTS:
        artist_id, found_name = search_artist(sp, artist_name)

        if artist_id:
            tracks = get_top_tracks(sp, artist_id, TRACKS_PER_ARTIST)
            all_track_ids.extend([t[0] for t in tracks])
            track_names = ", ".join([t[1] for t in tracks])
            print(f"   ✅ {found_name}: {len(tracks)} tracks - {track_names[:60]}...")
        else:
            print(f"   ❌ Could not find: {artist_name}")

    # Add tracks to playlist
    if all_track_ids:
        print(f"\n🎶 Adding {len(all_track_ids)} tracks to playlist...")
        add_tracks_to_playlist(sp, playlist_id, all_track_ids)
        print("✅ Tracks added successfully!")

    # Summary
    print("\n" + "=" * 50)
    print("🎉 Playlist created successfully!")
    print(f"   Name: {PLAYLIST_NAME}")
    print(f"   Total tracks: {len(all_track_ids)}")
    print(f"   URL: {playlist_url}")
    print("\nOpen Spotify and enjoy your new playlist! 🎧")


if __name__ == "__main__":
    main()
