# Security Policy & Threat Model 🔒

## Supported Versions

| Version | Supported | Security Maintenance |
| :--- | :--- | :--- |
| `1.2.x` | :white_check_mark: | Active support & continuous auditing |
| `< 1.2.0` | :x: | Deprecated |

---

## 1. Threat Model & Protections

### 1.1 Local IPv4 Binding
The WebSocket server binds exclusively to `127.0.0.1`. It never listens on `0.0.0.0` or external network adapters, preventing remote LAN/WAN access.

### 1.2 Constant-Time Authentication & Cryptographic Pairing
All pairing tokens are 128-bit cryptographically secure pseudorandom numbers generated via `secrets.token_hex(16)` on first initialization. Token comparisons strictly utilize Python's standard `secrets.compare_digest()` function, neutralizing side-channel timing analysis. In addition, users can cycle or rotate their pairing keys anytime from the interactive desktop settings panel.

### 1.3 Origin Verification
The WebSocket handshake strictly enforces that incoming requests must originate from `chrome-extension://`. Any web browser page or non-extension client attempting to connect is immediately rejected with HTTP 403 Forbidden.

### 1.4 Rate Limiting & DoS Protection
A sliding-window rate limiter restricts each connected client to a maximum of 30 messages per second, safeguarding the Tkinter rendering loop from denial-of-service.

### 1.5 Frame & String Bounds
Incoming frame sizes are limited to 64 KB (`MAX_PAYLOAD_BYTES`), and caption strings are bounded to 1,000 characters to prevent memory exhaustion.

---

## 2. Reporting a Vulnerability
If you discover a security vulnerability in this project, please open a private GitHub Advisory or contact the maintainer directly via GitHub rather than opening a public issue.
