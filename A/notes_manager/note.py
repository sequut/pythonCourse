import os

class NoteFileManager:
    def __init__(self, directory="notes"):
        self.directory = directory
        if not os.path.exists(directory):
            os.makedirs(directory)

    def save(self, note):
        with open(os.path.join(self.directory, f"{note.title}.txt"), "w", encoding="utf-8") as file:
            file.write(note.content)

    def load(self, title):
        path = os.path.join(self.directory, f"{title}.txt")
        if not os.path.exists(path):
            raise FileNotFoundError
        with open(path, "r", encoding="utf-8") as file:
            content = file.read()
        return content

    def delete(self, title):
        path = os.path.join(self.directory, f"{title}.txt")
        if os.path.exists(path):
            os.remove(path)


class Note:
    def __init__(self, title: str, content: str):
        self.__title = title
        self.__content = content
        self.__file_manager = NoteFileManager()

    @property
    def title(self):
        return self.__title

    @property
    def content(self):
        return self.__content

    def save_to_file(self):
        self.__file_manager.save(self)

    @staticmethod
    def load_from_file(title: str):
        content = NoteFileManager().load(title)
        return Note(title, content)

    def delete_file(self):
        self.__file_manager.delete(self.__title)
