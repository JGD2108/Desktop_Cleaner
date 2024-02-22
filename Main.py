import os 
import shutil 
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEvent, FileSystemEventHandler
from pathlib import Path

class Handler_Desktop(FileSystemEventHandler):
    def __init__(self,desktop_path, downloads_path) -> None:
        self.desktop_path = desktop_path
        self.downloads_path = downloads_path
        self.images = ['png','jpg','jpeg','gif','svg']
        self.media = ['mp3','mp4','mkv','avi','mov','flv','wmv']
        self.documents = ['pdf','doc','docx','xls','xlsx','ppt','pptx','txt']
        self.others = ['zip','rar','exe','msi','apk','iso']

    def on_modified(self, event: FileSystemEvent) -> None:
        if not event.is_directory:
            file_name = os.path.basename(event.src_path)
            self.move_files(file_name)

    def obtain_suffix(self, file_name):
        return file_name.split('.')[-1]
    
    def create_folders(self):
        folders = ['Imagenes','Media','Documentos','Otros', "shortcuts"]
        for folder in folders:
            if not os.path.exists(f'{self.desktop_path}/{folder}'):
                os.mkdir(f'{self.desktop_path}/{folder}')

    def move_files(self, file_name):
        if os.path.exists(os.path.join(self.desktop_path, file_name)):
            src = f'{self.desktop_path}/{file_name}'
            if not os.path.exists(src):
                print(f'File {src} does not exist')
                return
            suffix = self.obtain_suffix(file_name)
            if suffix in self.images:
                dst = f'{self.desktop_path}/Imagenes/{file_name}'
            elif suffix in self.media:
                dst = f'{self.desktop_path}/Media/{file_name}'
            elif suffix in self.documents:
                dst = f'{self.desktop_path}/Documentos/{file_name}'
            elif suffix in self.others:
                dst = f'{self.desktop_path}/Otros/{file_name}'
            else:
                return

            shutil.move(src, dst)
        else: 
            src = f'{self.downloads_path}/{file_name}'
            if not os.path.exists(src):
                print(f'File {src} does not exist')
                return
            suffix = self.obtain_suffix(file_name)
            if suffix in self.images:
                dst = f'{self.desktop_path}/Imagenes/{file_name}'
            elif suffix in self.media:
                dst = f'{self.desktop_path}/Media/{file_name}'
            elif suffix in self.documents:
                dst = f'{self.desktop_path}/Documentos/{file_name}'
            elif suffix in self.others:
                dst = f'{self.desktop_path}/Otros/{file_name}'
            else:
                return

            shutil.move(src, dst)




if __name__ == "__main__":
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    downloads_folder = str(Path.home() / "Downloads")
    event_handler = Handler_Desktop(desktop_path, downloads_folder)
    
    observer = Observer()
    observer.schedule(event_handler, downloads_folder, recursive=True)
    observer.schedule(event_handler, desktop_path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

    



