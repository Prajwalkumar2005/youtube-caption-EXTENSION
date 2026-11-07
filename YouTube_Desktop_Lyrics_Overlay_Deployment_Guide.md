# YouTube Desktop Lyrics Overlay - Deployment Guide 🚀

This document is the official, authoritative deployment guide for **YouTube Desktop Lyrics Overlay**, detailing end-to-end procedures for Chrome Web Store distribution, GitHub Releases packaging, and automated continuous delivery.

---

## 1. System Architecture Overview

```
┌──────────────────────────────────────────────┐
│           Google Chrome (MV3)                │
│  ┌────────────────────────────────────────┐  │
│  │ content.js (Dual-Engine Caption Sync)  │  │
│  └───────────────────┬────────────────────┘  │
│                      │ postMessage / runtime │
│  ┌───────────────────▼────────────────────┐  │
│  │ background.js (WebSocket Client Relay) │  │
│  └───────────────────┬────────────────────┘  │
└──────────────────────┼───────────────────────┘
                       │ ws://127.0.0.1:48123/?token=...
┌──────────────────────▼───────────────────────┐
│     Desktop Companion (Python / Win32)       │
│  ┌────────────────────────────────────────┐  │
│  │ bridge_server.py (Async WebSocket Srv) │  │
│  └───────────────────┬────────────────────┘  │
│                      │ Queue / Callback      │
│  ┌───────────────────▼────────────────────┐  │
│  │ main_overlay.py (Transparent Overlay)  │  │
│  └────────────────────────────────────────┘  │
└──────────────────────────────────────────────┘
```

---

## 2. Chrome Web Store Packaging & Submission

### 2.1 Package Verification
Run the automated packager to construct a clean, production-ready `.zip` archive:
```cmd
.\package_extension.bat
```
This produces `dist\yt-lyrics-overlay-extension.zip` containing strictly:
- `manifest.json` (MV3)
- `background.js`
- `content.js`
- `popup.html`
- `popup.js`
- `icons\icon16.png`, `icon32.png`, `icon48.png`, `icon128.png`

### 2.2 Submission Checklist
- [x] Manifest V3 compliance verified
- [x] Least-privilege permissions: `storage` and `alarms` only
- [x] Host permissions: bounded strictly to `*://*.youtube.com/*`
- [x] Zero external scripts or remote CDN execution
- [x] Privacy policy hosted publicly (see `PRIVACY_POLICY.md`)
- [x] Detailed permission justifications prepared (see `CHROME_STORE_LISTING.md`)

---

## 3. Windows Standalone Executable Packaging

### 3.1 PyInstaller Build
Compile the standalone zero-dependency executable:
```cmd
.\build_exe.bat
```
Output:
```
overlay_app\dist\YT_Lyrics_Overlay.exe (~13 MB)
```

### 3.2 Key Bundling Capabilities
- **Frozen Runtime Configuration**: Detects PyInstaller runtime and maps persistent configuration to `%APPDATA%\YTLyricsOverlay\config.json`.
- **True Desktop Transparency**: Preserves Win32 `WS_EX_LAYERED` and `WS_EX_TRANSPARENT` keying.
- **DPI Scaling**: Automatically configures Per-Monitor V2 DPI awareness.

---

## 4. Continuous Integration & Release Pipelines

- **CI Pipeline (`.github/workflows/ci.yml`)**: Runs on every pull request and push to `main`:
  1. Validates `manifest.json` against Chrome MV3 schemas.
  2. Executes standard library test suite (`overlay_app/run_all_tests.py`).
  3. Verifies PyInstaller compilation readiness.
  4. Generates release artifact `.zip`.
- **Release Pipeline (`.github/workflows/release.yml`)**: Triggers on Git version tags (`v*.*.*`) to publish production assets to GitHub Releases.

---

## 5. Security & Isolation Standard

- **Loopback Enforcement**: WebSocket server binds exclusively to `127.0.0.1`.
- **Timing-Safe Auth**: Constant-time token verification using `secrets.compare_digest`.
- **Origin Validation**: Rejects all incoming requests not originating from `chrome-extension://`.
- **Sliding-Window Rate Limiting**: Caps incoming messages at 30/sec per client.
