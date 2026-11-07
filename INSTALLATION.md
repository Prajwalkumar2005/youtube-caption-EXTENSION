# Installation Handbook 📖

This guide provides end-to-end instructions for installing **YouTube Desktop Lyrics Overlay** on Windows 10 & 11 systems.

---

## Prerequisites
- **Operating System:** Windows 10 (Build 1809+) or Windows 11
- **Browser:** Google Chrome (Version 102+ or any Chromium-based browser supporting MV3)
- **Optional Runtime:** Python 3.8+ (only needed if running from source; not required if using the standalone `.exe`)

---

## 1. Quick Installation (No Python Needed)
1. Download the latest release `.zip` from GitHub Releases.
2. Extract the archive to any folder on your PC.
3. Open Google Chrome, go to `chrome://extensions`, toggle **Developer mode**, click **Load unpacked**, and select the `extension` folder.
4. Launch `overlay_app\dist\YT_Lyrics_Overlay.exe`.
5. Open any YouTube video with captions!

---

## 2. Developer Installation (From Source)
1. Clone the repository:
   ```cmd
   git clone https://github.com/Prajwalkumar2005/EXTENSION.git
   cd EXTENSION
   ```
2. Install Python dependencies:
   ```cmd
   pip install -r overlay_app\requirements.txt
   ```
3. Launch the desktop companion:
   ```cmd
   python overlay_app\main_overlay.py
   ```
4. Load the `extension` folder into Chrome as an unpacked extension.
