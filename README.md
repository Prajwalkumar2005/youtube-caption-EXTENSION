# YouTube Desktop Lyrics Overlay 🎵

[![Chrome Extension MV3](https://img.shields.io/badge/Chrome_Extension-MV3-4285F4?logo=googlechrome&logoColor=white)](extension/manifest.json)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)](overlay_app/requirements.txt)
[![Platform Windows 10/11](https://img.shields.io/badge/Platform-Windows_10%20%7C%2011-0078D6?logo=windows&logoColor=white)](one_click_setup.bat)
[![Tests Passing](https://img.shields.io/badge/Tests-16%2F16%20Passed-brightgreen.svg)](overlay_app/run_all_tests.py)
[![License MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Privacy 100% Local](https://img.shields.io/badge/Privacy-100%25_Local_%26_Private-success)](PRIVACY_POLICY.md)

A sleek, lightweight, and completely private tool to stream **YouTube Closed-Captions & lyrics** directly to a beautiful, transparent, always-on-top desktop overlay in real time. Perfect for karaoke, singing along, language learning, or watching tutorials while working in other windows or playing games.

---

## 📸 Live Preview

![Demo Screenshot](demo_screenshot.png)

---

## ⚡ 60-Second Universal Setup (Any Windows PC)

### 1. Install Chrome Extension (30 Seconds)
1. Open Google Chrome and navigate to:
   ```text
   chrome://extensions
   ```
2. Toggle on **Developer mode** in the top-right corner.
3. Click the **Load unpacked** button in the top-left corner.
4. Select the `extension` folder inside this project.
5. Click the puzzle icon 🧩 in Chrome's toolbar and pin **YouTube Desktop Lyrics Overlay**.

### 2. Launch Desktop Overlay (10 Seconds)
Double-click **`one_click_setup.bat`** (or `run_overlay.bat`) in the project folder.
- *Automatic setup:* The script automatically checks your environment, installs dependencies, and launches the overlay.
- *No Python installed?* Run the standalone zero-dependency executable directly: `overlay_app\dist\YT_Lyrics_Overlay.exe`.

### 3. Play Any YouTube Video! 🎵
1. Open [YouTube](https://www.youtube.com) and play any video, music track, or YouTube Short with Closed Captions (**CC**) enabled.
2. The lyrics will float seamlessly over your desktop!

---

## ✨ Features

- **🎨 13 Cinematic Visual Styles:** Switch styles on the fly from the Chrome popup—from Hollywood movie posters to Cyberpunk neon.
- **🪟 True Desktop Transparency:** Text renders directly over your desktop wallpaper, browser, IDE, or games with zero window borders.
- **🖱️ Click-Through Mode:** Enable click-through (`Ctrl + T`) so your mouse clicks pass completely through the lyrics to windows beneath.
- **⚡ Dual-Engine Caption Sync:** Combines YouTube's TimedText sub-second API with real-time DOM mutation fallback for sub-frame accuracy.
- **📱 Shorts & Live Support:** Works seamlessly across standard YouTube videos, YouTube Shorts, and live streams.
- **🔒 100% Local & Private:** No cloud servers, no account required, no telemetry. Communication runs entirely through a local loopback WebSocket (`127.0.0.1`).

---

## 🎭 Visual Typography Styles

| Style Name | Description | Color Palette |
| :--- | :--- | :--- |
| **Cinematic Poster** *(Default)* | Dual-line movie title typography with bold drop-glow | Gold `#FBC02D` & Crisp White `#FFF` |
| **Neon Glow** | Vibrant synthwave glow with multi-pass blur | Neon Pink `#FF00FF` & Cyan `#00FFFF` |
| **Minimalist** | Clean modern aesthetic for focus and productivity | Crisp Studio White `#FFFFFF` |
| **Classic Subtitle (Yellow)** | Traditional broadcast yellow subtitles | High-contrast Yellow `#FFD700` |
| **Classic Subtitle (White)** | Classic cinema white subtitles with dark border | Clean White `#FFFFFF` |
| **Cyberpunk** | Monospace terminal aesthetic | Electric Cyan `#00FFFF` & Magenta `#FF00FF` |
| **Luxury Gold** | Elegant serif typeface with warm gold tones | Regal Gold `#FFDF00` |
| **Hacker Green** | Retro matrix phosphor glow | Terminal Green `#00FF00` |
| **Blood Red** | Aggressive bold high-impact red | Crimson Red `#FF0000` |
| **Ocean Blue** | Cool aquatic tones with navy outline | Azure Cyan `#00BFFF` |
| **Sunset Orange** | Warm dusk gradient styling | Deep Orange `#FF4500` & Violet `#800080` |
| **Ghost White** | Ethereal soft-shadow subtitle | Off-white `#F8F8FF` |
| **Vaporwave** | 80s retro aesthetic | Pastel Lavender `#FF66FF` & Cyan |

---

## ⚡ Keyboard Shortcuts (Global Desktop Hotkeys)

| Shortcut | Action |
| :--- | :--- |
| **`Ctrl` + `+`** or **`Ctrl` + `=`** | Increase Font Size (+2px) |
| **`Ctrl` + `-`** | Decrease Font Size (-2px) |
| **`Ctrl` + `S`** | Cycle to Next Visual Typography Style |
| **`Ctrl` + `L`** | Toggle Overlay Position Lock |
| **`Ctrl` + `T`** | Toggle Click-Through Mode (pass mouse clicks through) |
| **`Ctrl` + `H`** | Hide / Unhide Overlay Window |

---

## 🔒 Security Architecture

- **100% Local Loopback:** WebSocket bridge server binds strictly to `127.0.0.1`.
- **Cryptographic Token Verification:** Timing-attack safe token comparison using `secrets.compare_digest`.
- **Browser Origin Enforcement:** Strictly rejects any connection that does not originate from `chrome-extension://`.
- **Sliding-Window Rate Limiting:** Caps message ingress at 30 requests/second per client.

---

## 📚 Documentation Links

- [Universal Easy Setup Guide](EASY_SETUP_GUIDE.md)
- [Official Deployment Guide](YouTube_Desktop_Lyrics_Overlay_Deployment_Guide.md)
- [Production Verification & Sign-Off Report](PERFECT_DEPLOYMENT_VERIFICATION.md)
- [Full System Architecture & Viva Presentation Guide](PROJECT_ARCHITECTURE.md)
- [Privacy Policy](PRIVACY_POLICY.md)
- [Installation Handbook](INSTALLATION.md)
- [Security Policy](SECURITY.md)
- [Contribution Guidelines](CONTRIBUTING.md)
- [Chrome Web Store Submission Package](CHROME_STORE_LISTING.md)
- [Changelog](CHANGELOG.md)

---

## 📜 License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for full details.
