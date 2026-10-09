# Training Python: Making a Notepad

A personal notepad built while learning Python. It started as a
terminal program and grew into a desktop app with a Qt Designer
interface.

## Features

- Create, read, update, and delete notes (CRUD)
- Each note has a unique ID
- Notes are saved to a JSON file and survive restarts
- Desktop window: double-click a note to view and edit it

## Project structure

| File | Purpose |
|---|---|
| `notepad.py` | Logic: load, save, find, add, update, delete notes |
| `ui.py` | PyQt6 window, connects buttons to the logic |
| `notepad.ui` | Window layout designed in Qt Designer |
| `notes.json` | Saved notes (created automatically, not in git) |
| `requirements.txt` | Python dependencies |

## Setup

    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

## Run

    python3 ui.py

Run it from the project folder, because `notepad.ui` is loaded
from the current directory.

## How to use

1. Type a title and text, then click **Add**
2. Double-click a note in the list to open it
3. Edit it and click **Update**, or click **Delete** to remove it

## What I learned

- Lists, dictionaries, loops, and functions
- `try/except` for bad input and missing files
- Reading and writing JSON files
- Unique IDs and searching by ID
- Splitting logic (`notepad.py`) from interface (`ui.py`)
- Building a GUI with PyQt6 and Qt Designer

## Documentation

See [docs/DOCUMENTATION.md](docs/DOCUMENTATION.md) for how the code works.
