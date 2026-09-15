# TYSON Atlantis Player App (myT5S)

> **Official Standalone Web Audio DSP Station, Ambient Cinema & Speed Engine for TYSON Atlantis.**

Repository: `player-atlantis-tysonmediagroup-org-myt5s-app`

---

## ⚡ Core Features

- **T5S Boot Sequence**: High-contrast black boot screen with pure T5S logo followed by smooth crossfade into `New Background "myT5S.jpg"`.
- **Sped Up / Slowed DSP Engine**: Real-time Web Audio API node graph offering instant presets (`0.70x`, `0.80x`, `0.85x`, `1.00x`, `1.15x`, `1.25x`, `1.40x`), continuous speed slider (`0.50x`–`1.75x`), pitch preservation toggles, submerged low-pass filters, 432Hz harmonic tuning, and cathedral reverb.
- **Custom Playlists & Like System**: Create custom playlists, heart favorite songs, and explore curated stations (Slowed, Nightcore, 432Hz Submerged, PS2/2010 Archival, Liquid DnB).
- **Fullscreen Cinema Mode**: Real-time reactive visual backdrops, animated loops, and custom media switcher with synced playback HUD.
- **Real OAuth Integration**: Pre-configured for Google Identity Services (GIS) and Discord OAuth2.

---

## 🚀 Running the Standalone Player Locally

1. Start the included HTTP server:
   ```bash
   python3 server.py
   ```
2. Open your browser:
   ```
   http://localhost/
   ```
   *(or `http://localhost:8080/`)*

---

## 📁 Repository Structure

```
player-atlantis-tysonmediagroup-org-myt5s-app/
├── index.html                   # Standalone Player App
├── styles.css                   # Theme styles (Noir Midnight, Wii, Frutiger Aero, Botanical)
├── app.js                       # Audio DSP Engine, Visualizers, Playlists & OAuth
├── server.py                    # Standalone HTTP Server
└── assets/
    ├── audio/                   # 14 Full-Length MP3 Tracks & Soundscapes
    └── images/                  # Backdrops, Boot Logos & Official Banners
```

---

&copy; 2026 TYSON Media Group & Atlantis. All rights reserved.
