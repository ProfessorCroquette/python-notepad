
import json

FILENAME = "notes.json"



def save_notes():
  with open(FILENAME, "w") as f:
    json.dump(notes, f)

def load_notes():
  try:
    with open(FILENAME, 'r') as f:
      return json.load(f)
  except FileNotFoundError:
    return []

def read_notes():
  if len(notes) == 0:
    print("No notes yet.")
    return
  for note in notes:
    print(f"[{note['id']}] {note['title']}")
    print(f"   {note['text']}")

notes = load_notes()


def get_next_id():
  highest = 0
  for note in notes:
    if note["id"] > highest:
      highest = note["id"]
  return highest + 1

# ask the user for a note and save it in a variable called text
def create_notes():
  text = input("text: ")
  title = input("title: ")
  notes.append({"id": get_next_id(),"title": title, "text": text})
  save_notes()
  print("Note added.")

def find_note(note_id):
  for note in notes:
    if note["id"]== note_id:
      return note
  return None

def update_note():
  read_notes()
  try:
    note_id = int(input("Note ID: "))
  except ValueError:
    print("NOT A NUMBER")
    return
  note = find_note(note_id)
  if note is None:
    print("No Note With That ID found.")
    return
  note["text"]= input("New text: ")
  save_notes()
  print("Note Updated")

def delete_byID():
  read_notes()
  try:
     note_id = int(input("Note ID: "))
  except ValueError:
    print("NOT A NUMBER")
    return
  note = find_note(note_id)
  if note is None:
    print("No Note With that ID")
    return
  notes.remove(notes)
  save_notes()
  print("Note Deleted")

def add_note(title, text):
  notes.append({"id": get_next_id(), "title": title, "text": text})
  save_notes()


def remove_note(note_id):
  note = find_note(note_id)
  if note is None:
    return False
  notes.remove(note)
  save_notes()
  return True
