import sys
from PyQt6 import QtWidgets, uic
import notepad


class NotepadWindow(QtWidgets.QMainWindow):
  def __init__(self):
    super().__init__()
    uic.loadUi("notepad.ui", self)
    self.current_id = None
    self.addButton.clicked.connect(self.add_clicked)
    self.updateButton.clicked.connect(self.update_clicked)
    self.deleteButton.clicked.connect(self.delete_clicked)
    self.listWidget.itemClicked.connect(self.note_opened)
    self.refresh_list()

  def refresh_list(self):
    self.listWidget.clear()
    for note in notepad.notes:
      self.listWidget.addItem(f"[{note['id']}] {note['title']}")

  def get_id(self, item):
    return int(item.text().split("]")[0].strip("["))

  def add_clicked(self):
    title = self.titleEdit.text()
    text = self.textEdit.toPlainText()
    if title == "":
      return
    notepad.add_note(title, text)
    self.current_id = None
    self.titleEdit.clear()
    self.textEdit.clear()
    self.refresh_list()

  def note_opened(self, item):
    note_id = self.get_id(item)
    note = notepad.find_note(note_id)
    if note is None:
      return
    self.current_id = note_id
    self.titleEdit.setText(note["title"])
    self.textEdit.setPlainText(note["text"])

  def update_clicked(self):
    if self.current_id is None:
      return
    note = notepad.find_note(self.current_id)
    if note is None:
      return
    note["title"] = self.titleEdit.text()
    note["text"] = self.textEdit.toPlainText()
    notepad.save_notes()
    self.refresh_list()

  def delete_clicked(self):
    if self.current_id is None:
      return
    notepad.remove_note(self.current_id)
    self.current_id = None
    self.titleEdit.clear()
    self.textEdit.clear()
    self.refresh_list()


app = QtWidgets.QApplication(sys.argv)
window = NotepadWindow()
window.show()
sys.exit(app.exec())
