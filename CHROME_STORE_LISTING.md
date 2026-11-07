# Chrome Web Store Publication Package 🛍️

This document contains metadata, permission justifications, and reviewer instructions for submitting to the Google Chrome Web Store.

---

## 1. Store Metadata

- **Extension Name:** YouTube Desktop Lyrics Overlay
- **Short Description (Max 132 chars):** Stream live YouTube closed captions & lyrics directly to a sleek, transparent, always-on-top desktop overlay.
- **Category:** Accessibility & Entertainment
- **Language:** English

---

## 2. Detailed Store Description

Stream live YouTube closed-captions and song lyrics directly to a beautiful, borderless, always-on-top desktop overlay in real time!

Whether you are singing karaoke, learning a new language, watching lectures while coding, or gaming while following video walkthroughs, YouTube Desktop Lyrics Overlay provides sub-second synchronized subtitle rendering directly over your screen.

✨ KEY FEATURES:
• 🎨 13 Cinematic Visual Styles — from Hollywood movie typography to Cyberpunk neon glow
• 🪟 True Desktop Transparency — borderless rendering floating directly over your wallpaper or active games
• 🖱️ Click-Through Mode — mouse clicks pass completely through the overlay to windows underneath
• ⚡ Dual-Engine Accuracy — combines YouTube TimedText sub-second API with real-time DOM mutation fallback
• 📱 Shorts & Live Support — seamless operation on standard YouTube videos, Shorts, and Live streams
• 🔒 100% Local & Private — zero cloud telemetry; all communication runs strictly via isolated loopback WebSocket (127.0.0.1)

---

## 3. Permission Justifications (For Reviewers)

- **`storage`**: Used to persist user UI styling preferences (selected visual theme, font size, custom highlight color) and the local pairing key across browser sessions.
- **`alarms`**: Used to maintain periodic heartbeat checks that reconnect the background service worker to the local desktop overlay if it enters idle mode.
- **`*://*.youtube.com/*` (Host Permission)**: Required to extract closed-caption timed text from YouTube video playback and mirror subtitle updates to the desktop overlay.

---

## 4. Single-Purpose Statement
The sole purpose of this extension is to extract closed captions and lyrics from YouTube videos in the browser and stream them to the companion desktop overlay for floating accessibility display.
