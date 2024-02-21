import os 
import shutil 
import time
class Handler():
    def __init__(self,desktop_path) -> None:
        self.desktop_path = desktop_path
        self.images = ['png','jpg','jpeg','gif','svg']
        self.media = ['mp3','mp4','mkv','avi','mov','flv','wmv']
        self.documents = ['pdf','doc','docx','xls','xlsx','ppt','pptx','txt']
        self.others = ['zip','rar','exe','msi','apk','iso']

    def check_files(self):
        for filename in os.listdir(self.desktop_path):
            self.move_files(filename)

    def obtain_suffix(self, file_name):
        return file_name.split('.')[-1]
    
    def create_folders(self):
        folders = ['Imagenes','Media','Documentos','Otros', "shortcuts"]
        for folder in folders:
            if not os.path.exists(f'{self.desktop_path}/{folder}'):
                os.mkdir(f'{self.desktop_path}/{folder}')

    def move_files(self, file_name):
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

if __name__ == "__main__":
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    handler = Handler(desktop_path)
    while True:
        handler.check_files()
        time.sleep(50)
    



