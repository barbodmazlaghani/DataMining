from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory and os.path.basename(event.src_path) == "data_file.csv":
            print("Data file has been updated. Recalculating metrics...")

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, path='/dataset/directory', recursive=False)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()
