# Spotify Playlist Creator 🎧

A Python tool to programmatically create Spotify playlists from a curated list of artists. Perfect for discovering new music or creating themed playlists quickly.

## Features

- 🎵 **Artist-based playlist generation** - Add top tracks from multiple artists
- 🔐 **Secure OAuth authentication** - Uses Spotify's official authorization flow
- ⚙️ **Configurable** - Customize playlist name, description, and tracks per artist
- 🚀 **Simple to use** - One command to create a fully populated playlist

## Quick Start

### 1. Set up Spotify API Credentials

1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Click **Create App**
   - Name: `Playlist Creator` (or any name)
   - Description: anything
   - Redirect URI: `http://127.0.0.1:8888/callback`
3. Copy your **Client ID** and **Client Secret**

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Credentials

Either set environment variables:

```bash
export SPOTIPY_CLIENT_ID="your_client_id"
export SPOTIPY_CLIENT_SECRET="your_client_secret"
```

Or edit `create_spotify_playlist.py` directly and replace the placeholder values.

### 4. Run the Script

```bash
python create_spotify_playlist.py
```

A browser window will open for authorization. Log in to Spotify and click **Agree** to grant access.

## Configuration

Edit the constants in `create_spotify_playlist.py` to customize:

```python
# Artists to include
ARTISTS = [
    "Bonobo",
    "Four Tet",
    # Add more artists...
]

# Tracks per artist (default: 3)
TRACKS_PER_ARTIST = 3

# Playlist name and description
PLAYLIST_NAME = "My Custom Playlist 🎧"
PLAYLIST_DESCRIPTION = "Created with Spotify Playlist Creator"
```

## Example Output

```
🎵 Spotify Playlist Creator - Electronic Discovery
==================================================

🔐 Authenticating with Spotify...
✅ Logged in as: Your Name (username)

📝 Creating playlist: Electronic Discovery 🎧
✅ Playlist created!

🔍 Searching for artists and their top tracks...
   ✅ Bonobo: 3 tracks - From You, Kong, Cirrus...
   ✅ Four Tet: 3 tracks - VOLVER, Baby again.., glow...

🎶 Adding 30 tracks to playlist...
✅ Tracks added successfully!

==================================================
🎉 Playlist created successfully!
   URL: https://open.spotify.com/playlist/...

Open Spotify and enjoy your new playlist! 🎧
```

## Requirements

- Python 3.7+
- Spotify account (free or premium)
- Spotify Developer API credentials

## License

MIT License - feel free to use and modify!
