````markdown
# Pepper Scanner

Minimal TCP port scanner written in Python.  
Scans a target host for open TCP ports and prints results to the console.

> **Warning:** Only run this tool on systems you own or have explicit permission to test.

---

## Repository contents

- `pepper.py` — main scanner script

---

## Features

- TCP connect scanning (reports open ports)
- ASCII banner via `pyfiglet`
- Simple, single-file implementation for learning and quick lab use

---

## Requirements

- Python 3.7 or newer
- `pyfiglet`

Install dependency:
```bash
python -m venv venv
source venv/bin/activate     # Windows: venv\Scripts\activate
pip install pyfiglet
````

Or use:

```bash
pip install -r requirements.txt
```

(If `requirements.txt` is added to the repo, include `pyfiglet`.)

---

## Usage

```bash
python3 pepper.py <target>
```

Examples:

```bash
python3 pepper.py example.com
python3 pepper.py 192.168.1.10
```

Sample output:

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

## Notes / Known behavior

* The script expects a single positional argument (target hostname or IP).
* Current default port loop uses `range(1, 65535)` (scans ports 1 through 65534). Modify to `range(1, 65536)` to include port 65535.
* The script uses `socket.setdefaulttimeout(1)`; consider per-socket timeouts if refactoring.
* The scanner is sequential (one port at a time) and intended for small lab scans or learning purposes.

---

## License

Add a `LICENSE` file to the repo with your chosen license (e.g., MIT). If no license is present, the repository defaults to “all rights reserved.”

---

## Contact

Include your preferred contact (GitHub profile link or email) in the repo if you want others to reach you.

```

Want me to drop that file into a generated repo structure (LICENSE, requirements.txt, .gitignore) next?
```

