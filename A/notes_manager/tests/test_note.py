import unittest
from A.notes_manager.note import Note

class TestNote(unittest.TestCase):
    def test_save_and_load_note(self):
        note = Note("test_note", "Test content")
        note.save_to_file()
        loaded_note = Note.load_from_file("test_note")
        self.assertEqual(note.content, loaded_note.content)
        loaded_note.delete_file()

if __name__ == "__main__":
    unittest.main()
