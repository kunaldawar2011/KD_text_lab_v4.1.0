# KD Text Lab v4.1.0

A terminal text editor and text-tools app written in Python. It has animated loading bars, colored menus, and a set of text tools like counting, case conversion, reversing, splitting, and searching.

Made by **Kunal Dawar** (GitHub: `kunaldawar2011`)

---

## Table of Contents

1. [Features](#features)
2. [Requirements](#requirements)
3. [Dependencies](#dependencies)
4. [Installation](#installation)
   - [Linux / Ubuntu / Debian](#linux--ubuntu--debian)
   - [macOS](#macos)
   - [Windows](#windows)
   - [Android (Termux)](#android-termux)
5. [How to Run](#how-to-run)
6. [How to Use](#how-to-use)
7. [Menu Reference](#menu-reference)
8. [Troubleshooting](#troubleshooting)
9. [What's New in v4.1.0](#whats-new-in-v410)
10. [Author](#author)

---

## Features

- Name-based welcome screen
- Animated loading bar before the editor starts
- Colored terminal output using `colorama`
- 14 text tools (count, upper/lower case, reverse, split, swap case, title case, find, and more)
- Shows how long you have used the app in seconds
- Runs on Linux | macOS | Windows | Android (Termux)

---

## Requirements

| Requirement | Version / Notes |
|---|---|
| Python | **3.10 or above** (required because the script uses `match` statements) |
| pip | Comes with most Python installs |
| Git | Needed only to clone the repo |
| Terminal | Any terminal with ANSI color support |

---

## Dependencies

| Module | Type | Purpose |
|---|---|---|
| `time` | Built-in | Delays for animations, and measuring how long the app was used |
| `random` | Built-in | Picks a random length for the loading bar |
| `colorama` | External (pip) | Colored text in the terminal |

Only `colorama` needs to be installed manually.

---

## Installation

### Linux / Ubuntu / Debian

```bash
# 1. Install Python, pip and Git
sudo apt update
sudo apt install python3 python3-pip git -y

# 2. Clone the repository
git clone https://github.com/kunaldawar2011/KD_text_lab.git
cd KD_text_lab

# 3. Install colorama
pip3 install colorama

# 4. Run the app
python3 KD_text_lab_v4.1.0.py
```

### macOS

```bash
# 1. Install Python and Git (requires Homebrew)
brew install python git

# 2. Clone the repository
git clone https://github.com/kunaldawar2011/KD_text_lab.git
cd KD_text_lab

# 3. Install colorama
pip3 install colorama

# 4. Run the app
python3 KD_text_lab_v4.1.0.py
```

### Windows

1. Install Python 3.10+ from [python.org](https://www.python.org/downloads/). On the first screen, tick **"Add Python to PATH"**.
2. Install Git from [git-scm.com](https://git-scm.com/downloads).
3. Open Command Prompt or PowerShell and run:

```powershell
git clone https://github.com/kunaldawar2011/KD_text_lab.git
cd KD_text_lab
pip install colorama
python KD_text_lab_v4.1.0.py
```

### Android (Termux)

```bash
# 1. Update Termux
pkg update && pkg upgrade -y

# 2. Install Python and Git
pkg install python git -y

# 3. Clone the repository
git clone https://github.com/kunaldawar2011/KD_text_lab.git
cd KD_text_lab

# 4. Install colorama
pip install colorama

# 5. Run the app
python KD_text_lab_v4.1.0.py
```

> **Tip:** If `pip` is not found in Termux, run `python -m pip install colorama`.

---

## How to Run

Go to the folder that has the script and run:

```bash
python KD_text_lab_v4.1.0.py
```

(Use `python3` instead of `python` on Linux and macOS if needed.)

---

## How to Use

1. **Enter your name** when asked. The app greets you with it.
2. **Choose an option** from the first menu:
   - `1` starts the editor.
   - `2` exits the app.
3. If you chose `1`, the app shows a loading bar, then asks you to **enter the text** you want to work on.
4. **Pick a tool number** from the text menu (see below). The result prints on screen, and the menu comes back.
5. Choose `14` to exit the text menu.

> **Note:** Enter numbers only where the app asks for a number. Letters will show an error message.

---

## Menu Reference

| No. | Option | What it does |
|---|---|---|
| 1 | Count text | Counts total characters |
| 2 | Capital all text | Converts everything to UPPERCASE |
| 3 | Uncapital all text | Converts everything to lowercase |
| 4 | Reverse text | Reverses the text |
| 5 | Count words | Counts the number of words |
| 6 | Alphabet test | Prints `True` if the text has only letters |
| 7 | Number test | Prints `True` if the text has only digits |
| 8 | Split test | Splits the text into a list of words |
| 9 | Swap case | Changes capitals to small and small to capitals |
| 10 | Title | Capitalizes the first letter of each word |
| 11 | Capitalize | Capitalizes only the first letter of the text |
| 12 | Find | Asks for a word or character and shows its position |
| 13 | Time used | Shows how many seconds you have used the app |
| 14 | Exit | Leaves the text menu |

---

## Troubleshooting

| Problem | Solution |
|---|---|
| `ModuleNotFoundError: No module named 'colorama'` | Run `pip install colorama` (or `pip3 install colorama`) |
| `python: command not found` | Use `python3` instead, or reinstall Python and add it to PATH |
| `pip: command not found` (Termux) | Run `pkg install python` again, then `python -m pip install colorama` |
| `SyntaxError` on `match` | Your Python is older than 3.10. Install a newer version |
| Colors look wrong | Use a terminal with ANSI color support |
| Animation is slow or choppy | Use a larger terminal window or a faster terminal app |

---

## What's New in v4.1.0

- Added animations (loading bar and delays between menu items)
- Small bug fixes

---

## Author

**Kunal Dawar**
GitHub: [@kunaldawar2011](https://github.com/kunaldawar2011)
