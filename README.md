# Pepper Scanner

A minimal, no-frills TCP port scanner written in Python.  
Scans a target host for open TCP ports and prints results to the console.

> **Warning:** Run this only against systems you own or have explicit permission to test.

---

## Files

- `pepper.py` — scanner script

---

## Quick start

1. (Optional) Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
````

2. Install the single dependency:

```bash
pip install pyfiglet
```

3. Run the scanner:

```bash
python3 pepper.py <target>
```

Examples:

```bash
python3 pepper.py example.com
python3 pepper.py 192.168.1.10
```

---

## Output example

```
  ____                      _                    
 |  _ \ __ _ _ __ ___  _ __| | ___  _   _  ___   
 | |_) / _` | '_ ` _ \| '__| |/ _ \| | | |/ _ \  
 |  __/ (_| | | | | | | |  | | (_) | |_| |  __/  
 |_|   \__,_|_| |_| |_|_|  |_|\___/ \__, |\___|  
                                     |___/       

--------------------------------------------------
Scanning target: 93.184.216.34
Scanning started at: 2025-10-14 18:20:00.123456
--------------------------------------------------
Port 80 is open
Port 443 is open
...
```

---

## Behavior notes

* Expects **one** positional argument: the hostname or IPv4 address to scan.
* Default scanned port range in the script: `1` → `65534`. (Change to `1..65535` if you want to include `65535`.)
* Uses `socket.connect_ex()` so closed ports do **not** raise exceptions.
* Uses a sequential scan (one port at a time). Suitable for quick lab checks and learning.

---

## Troubleshooting

* `ModuleNotFoundError: No module named 'pyfiglet'` → run `pip install pyfiglet`.
* If DNS resolution fails, confirm the target and try an IP instead of a hostname.
* Long run time scanning many ports is expected — the script is sequential.

---
