# Privacy Policy for YouTube Desktop Lyrics Overlay 🛡️

**Effective Date:** 2026-11-07  
**Last Updated:** 2026-11-07  

YouTube Desktop Lyrics Overlay ("the Extension", "the Companion", "we", "our") is designed with a **100% Local, Zero-Data-Collection Architecture**.

---

## 1. Zero Data Collection & Storage
- We do **NOT** collect, transmit, store, or sell any personal data, user credentials, browsing history, or analytical telemetry.
- All caption extraction and desktop transmission occurs strictly across your local computer via an isolated loopback WebSocket (`127.0.0.1`).
- No data is ever transmitted to external cloud servers, third-party services, or analytics providers.

---

## 2. Chrome Extension Permissions Justification

| Permission | Technical Purpose |
| :--- | :--- |
| `storage` | Saves user aesthetic preferences (font size, visual style, custom highlight color) and the local pairing token strictly on your machine. |
| `alarms` | Periodically pings the local loopback WebSocket server to restore the connection if the background worker was paused. |
| `*://*.youtube.com/*` | Required solely to extract closed captions from YouTube video playback in real time and forward them to your desktop overlay. |

---

## 3. Communication Security
The desktop bridge binds exclusively to the local IPv4 loopback address (`127.0.0.1`). The server validates the browser origin to ensure only Chrome extensions can communicate with the overlay, guarded by cryptographic constant-time token comparison.

---

## 4. Contact & Inquiries
For questions regarding this Privacy Policy or the security architecture of the extension, please open an issue on our official GitHub repository:  
[https://github.com/Prajwalkumar2005/EXTENSION](https://github.com/Prajwalkumar2005/EXTENSION)
