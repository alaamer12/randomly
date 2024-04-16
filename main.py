from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os

class FileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            print(f"File {event.src_path} has been modified")

directory = r"D:\ups\ideaProjects\the app\thanwyaIdea\ReactTests\projects"

observer = Observer()
observer.schedule(FileChangeHandler(), path=directory, recursive=True)
observer.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    observer.stop()

observer.join()
