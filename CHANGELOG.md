# Changelog 📝

All notable changes to **YouTube Desktop Lyrics Overlay** will be documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.2.0] - 2026-11-07

### Added
- **Dynamic 128-Bit Cryptographic Pairing Tokens**: Zero-config auto-generation of unique per-installation pairing tokens on first run using Python `secrets.token_hex(16)`.
- **AppData Configuration Path**: Support for frozen PyInstaller executable runtime mapping to `%APPDATA%\YTLyricsOverlay\config.json`.
- **Comprehensive Automated Test Suite**: Standard-library unit tests covering token entropy, constant-time comparison, caption binary search, configuration persistence, Win32 style bitmasks, and Manifest V3 schema validation (`run_all_tests.py`).
- **Live Preview Support**: Expanded Chrome extension popup to support full live preview typography for all 13 styles, including `minimal`, `classic_white`, and `ghost`.
- **Equalizer Animation Toggle**: Added desktop configuration toggle and settings checkbox for audio equalizer bar animation.
- **WebSocket Port Conflict Feedback**: Desktop overlay now surfaces visible error notifications when ports 48123-48128 are blocked by other applications.
- **Universal 1-Click Setup Script**: Created `one_click_setup.bat` with automatic Python detection, dependency installation, and extension loading guidance.
- **Production Documentation**: Added `YouTube_Desktop_Lyrics_Overlay_Deployment_Guide.md`, `PERFECT_DEPLOYMENT_VERIFICATION.md`, `EASY_SETUP_GUIDE.md`, `DEPLOYMENT.md`, `PRIVACY_POLICY.md`, `INSTALLATION.md`, `SECURITY.md`, `CONTRIBUTING.md`, and `CHROME_STORE_LISTING.md`.

### Fixed
- **Multi-pass Neon Blur**: Fixed loop offset rendering bug in `neon` typography style for authentic multi-pass glow.
- **Caption Deduplication**: Implemented timestamp debouncing to prevent collision between TimedText and DOM mutation observer caption streams.
- **PostMessage Security**: Restricted `window.postMessage` target origin to `window.location.origin` preventing arbitrary iframe interception.
- **Stale Caption Pruning**: Cleared background service worker message buffer upon YouTube video navigation (`video_navigated`).

---

## [1.1.0] - 2026-09-17

### Added
- Global desktop hotkeys (`Ctrl + +`, `Ctrl + -`, `Ctrl + S`, `Ctrl + L`, `Ctrl + T`, `Ctrl + H`).
- 5-bar animated audio equalizer visualizer simulation.
- Real-time highlight color picker with presets.
- Smooth crossfade text animation on lyrics change.
- Automated system health check script (`diagnostics.py`).

---

## [1.0.0] - 2026-09-01

### Added
- Initial public release of YouTube Desktop Lyrics Overlay.
- Chrome MV3 extension with dual-engine caption capture (TimedText API + DOM MutationObserver).
- Borderless transparent desktop window keyed to `#000001` via Win32.
- 13 typography themes (Cinematic Poster, Neon Glow, Cyberpunk, Luxury Gold, Hacker Green, etc.).
- WebSocket bridge server with port fallback cascade (48123-48128).
