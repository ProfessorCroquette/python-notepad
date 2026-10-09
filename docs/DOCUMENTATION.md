# Notepad Documentation

## Data format

Notes are stored in `notes.json` as a list of dictionaries:

    [
      {"id": 1, "title": "shopping", "text": "buy milk"},
      {"id": 2, "title": "homework", "text": "finish math"}
    ]

IDs are never reused. A new note gets the highest existing ID plus 1.

## notepad.py functions

| Function | Description |
|---|---|
| `load_notes()` | Reads `notes.json`; returns `[]` if the file doesn't exist |
| `save_notes()` | Writes the `notes` list to `notes.json` |
| `get_next_id()` | Returns the highest ID plus 1 |
| `find_note(note_id)` | Returns the note with that ID, or `None` |
| `add_note(title, text)` | Adds a note and saves |
| `remove_note(note_id)` | Removes a note and saves; returns `True` or `False` |

## ui.py

`NotepadWindow` loads `notepad.ui` and connects the widgets:

| Widget | objectName | Action |
|---|---|---|
| List | `listWidget` | double-click opens a note |
| Title box | `titleEdit` | note title |
| Text box | `textEdit` | note body |
| Add button | `addButton` | `add_clicked` |
| Update button | `updateButton` | `update_clicked` |
| Delete button | `deleteButton` | `delete_clicked` |

`self.current_id` remembers which note is open for Update and Delete.

## Design notes

- Logic and interface are in separate files, so the logic can be
  reused in the terminal or the window
- Notes are found by ID, not list position, so deleting a note
  never changes another note's ID
