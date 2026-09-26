from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import time
from ingest import ingest_file
from config import KNOWLEDGE_BASE

class MyFileSystemEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        self.process_file(event.src_path)

    def on_modified(self, event):
        if event.is_directory:
            return
        self.process_file(event.src_path)

    def on_deleted(self, event):
        if event.is_directory:
            return
    def process_file(self,file_path):
        ingest_file(file_path)

def start_watcher():
    event_handler=MyFileSystemEventHandler()
    observer=Observer()
    observer.schedule(event_handler,str(KNOWLEDGE_BASE),recursive=True)
    observer.start()
    try:
        while True:
            #print("watching")
            time.sleep(1)
    except Exception as e:
        print(f"exception as {e}")
        observer.stop()
    observer.join()

if __name__ =='__main__':
    start_watcher()

