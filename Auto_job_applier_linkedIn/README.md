# LinkedIn AI Auto Job Applier

**Author:** Venkat Manikanta

Automates LinkedIn job search and Easy Apply: applies filters, answers application questions, uploads your resume, and tracks applied jobs. Configure search preferences and personal details in the `config/` folder before running.

## Requirements

- Python 3.10+
- Google Chrome (latest)
- Packages: `undetected-chromedriver`, `pyautogui`, `setuptools`, `openai`, `flask`, `flask-cors`

```bash
pip install undetected-chromedriver pyautogui setuptools openai flask-cors flask
```

On Windows, you can run `setup/windows-setup.bat` to install ChromeDriver automatically.

## Quick start

1. Copy or edit config files under `config/`:
   - `personals.py` — name, phone, address
   - `questions.py` — resume path, salary, cover letter, AI profile text
   - `search.py` — job filters and search preferences
   - `secrets.py` — LinkedIn login and optional API keys
   - `settings.py` — bot behavior (stealth mode, delays, etc.)
2. Place your resume at the path set in `default_resume_path` inside `questions.py`.
3. Run the bot:

```bash
python runAiBot.py
```

4. Optional: view applied jobs history:

```bash
python app.py
```

Then open `http://localhost:5000` in your browser.

## Project layout

| Path | Purpose |
|------|---------|
| `runAiBot.py` | Main automation script |
| `app.py` | Local UI for applied jobs history |
| `config/` | Personal data, search filters, secrets, settings |
| `modules/` | Browser automation, AI helpers, validators |
| `setup/` | Windows/Linux setup scripts |

## Disclaimer

This tool is for **personal and educational use**. You are responsible for complying with LinkedIn’s Terms of Service and applicable laws. Use at your own risk. The author is not liable for misuse, account restrictions, or data loss.

## License

Copyright (C) 2026 Venkat Manikanta

This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License v3 or later. See [https://www.gnu.org/licenses/agpl-3.0.html](https://www.gnu.org/licenses/agpl-3.0.html).
