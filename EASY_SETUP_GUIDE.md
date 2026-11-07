# Universal Easy Setup Guide ⚡

Set up **YouTube Desktop Lyrics Overlay** on **any Windows PC** in under 60 seconds!

---

## 🚀 3 Simple Steps to Get Started

### Step 1: Install the Chrome Extension (30 Seconds)
1. Open Google Chrome and type in the address bar:
   ```text
   chrome://extensions
   ```
2. Turn on the **Developer mode** toggle in the top-right corner.
3. Click the **Load unpacked** button in the top-left corner.
4. Select the `extension` folder located inside this project folder.
5. Click the puzzle icon 🧩 in Chrome's toolbar and pin **YouTube Desktop Lyrics Overlay**.

---

### Step 2: Start the Desktop Overlay (10 Seconds)
Choose the option that fits your setup:

#### Option A: Double-Click `run_overlay.bat` (Recommended)
Double-click `run_overlay.bat` in the project folder.
- Automatically detects Python (`python` or `py`).
- Installs necessary requirements (`websockets`) automatically if missing.
- Launches the overlay smoothly on your screen.

#### Option B: Standalone Pre-compiled App (No Python Required)
Navigate to:
```text
overlay_app\dist\YT_Lyrics_Overlay.exe
```
Double-click `YT_Lyrics_Overlay.exe` to run immediately! This single executable is fully portable and can be run directly from any USB flash drive or folder without administrator permissions.

---

### Step 3: Play Any YouTube Video! 🎵
1. Open [YouTube](https://www.youtube.com).
2. Play any music video, tutorial, or YouTube Short with Closed Captions (**CC**) enabled.
3. Watch the lyrics float gracefully over your desktop, games, or work applications!

---

## 🎛️ Quick Controls Reference

| Action | Shortcut / Click |
| :--- | :--- |
| **Move Overlay** | Click and drag the top header bar |
| **Resize Overlay** | Click and drag the bottom-right corner grip `⇲` |
| **Change Font Size** | `Ctrl + +` / `Ctrl + -` |
| **Switch Visual Theme** | `Ctrl + S` or select from the Chrome extension popup |
| **Toggle Click-Through** | `Ctrl + T` (allows mouse clicks to pass straight through) |
| **Hide / Unhide** | `Ctrl + H` |
| **Copy Pairing Token** | Click `[Token]` on the overlay header |

---

## ❓ Troubleshooting & FAQs

### The overlay says "Searching Bridge..."
1. Ensure the overlay is running on your desktop.
2. Click the extension icon in Chrome and check the status indicator.
3. Click `[Token]` on the desktop overlay to copy your pairing key, paste it into the Chrome popup, and click **Connect**.

### The video has no captions appearing
- Make sure Closed Captions are turned **ON** on the YouTube video player (press `C` on your keyboard while watching).
