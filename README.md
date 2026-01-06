<h1 align="center">
  Ìæß Spotify Playlist Creator
</h1>

<p align="center">
  <strong>Programmatically create curated Spotify playlists from your favorite artists</strong>
</p>

<p align="center">
  <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/python-3.7+-blue.svg" alt="Python 3.7+"></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License: MIT"></a>
  <a href="https://developer.spotify.com/documentation/web-api/"><img src="https://img.shields.io/badge/Spotify-API-1DB954?logo=spotify" alt="Spotify API"></a>
</p>

---

## ÌæØ What It Does

A lightweight Python CLI tool that creates Spotify playlists by fetching top tracks from a list of artists. Perfect for:

- Ìæµ **Discovering new music** from your favorite genres
- ‚ö° **Quickly creating themed playlists** (workout, focus, party)
- Ì¥Ñ **Automating playlist curation** for radio shows or events

## ‚ú® Features

| Feature | Description |
|---------|-------------|
| **Artist-based Generation** | Automatically fetches top tracks from multiple artists |
| **OAuth 2.0 Authentication** | Secure Spotify authorization flow |
| **Configurable** | Customize playlist name, description, and tracks per artist |
| **Batch Processing** | Handles 100+ tracks efficiently with API batching |

## Ìª†Ô∏è Tech Stack

- **Python 3.7+** - Core language
- **[Spotipy](https://spotipy.readthedocs.io/)** - Spotify Web API wrapper
- **OAuth 2.0** - Secure authentication

## Ì∫Ä Quick Start

### 1. Clone the Repository

\`\`\`bash
git clone https://github.com/lisardo-iniesta/spotify-playlist-creator.git
cd spotify-playlist-creator
\`\`\`

### 2. Set up Spotify API Credentials

1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Click **Create App**
   - Redirect URI: \`http://127.0.0.1:8888/callback\`
3. Copy your **Client ID** and **Client Secret**

### 3. Install & Configure

\`\`\`bash
# Install dependencies
pip install spotipy

# Set credentials (Linux/Mac)
export SPOTIPY_CLIENT_ID="your_client_id"
export SPOTIPY_CLIENT_SECRET="your_client_secret"

# Windows PowerShell
\$env:SPOTIPY_CLIENT_ID="your_client_id"
\$env:SPOTIPY_CLIENT_SECRET="your_client_secret"
\`\`\`

### 4. Run

\`\`\`bash
python create_spotify_playlist.py
\`\`\`

A browser window will open for authorization. Log in and click **Agree**.

## ‚öôÔ∏è Configuration

Edit \`create_spotify_playlist.py\` to customize your playlist:

\`\`\`python
# Artists to include
ARTISTS = [
    "Bonobo",
    "Four Tet",
    "Caribou",
    # Add more...
]

# Tracks per artist
TRACKS_PER_ARTIST = 3

# Playlist metadata
PLAYLIST_NAME = "My Custom Playlist Ìæß"
PLAYLIST_DESCRIPTION = "Created with Spotify Playlist Creator"
\`\`\`

## Ì≥∏ Example Output

\`\`\`
Ìæµ Spotify Playlist Creator - Electronic Discovery
==================================================

Ì¥ê Authenticating with Spotify...
‚úÖ Logged in as: Lisardo (lisardo-iniesta)

Ì≥ù Creating playlist: Electronic Discovery Ìæß
‚úÖ Playlist created!

Ì¥ç Searching for artists and their top tracks...
   ‚úÖ Bonobo: 3 tracks - From You, Kong, Cirrus...
   ‚úÖ Four Tet: 3 tracks - VOLVER, Baby again.., glow...
   ‚úÖ Caribou: 3 tracks - Can't Do Without You, Odessa...

Ìæ∂ Adding 30 tracks to playlist...
‚úÖ Tracks added successfully!

==================================================
Ìæâ Playlist created successfully!
   URL: https://open.spotify.com/playlist/...
\`\`\`

## Ì∑∫Ô∏è Roadmap

- [ ] Add CLI arguments for runtime configuration
- [ ] Support importing artists from CSV/JSON
- [ ] Add genre-based playlist generation
- [ ] Create web interface

## Ì≥Ñ License

MIT License - feel free to use this for personal or commercial projects.

---

<p align="center">
  Made with ‚ù§Ô∏è by <a href="https://github.com/lisardo-iniesta">Lisardo Iniesta</a>
</p>
