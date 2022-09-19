import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# from_dir = "DIGITE O CAMINHO DA PASTA DE DOWNLOAD (USE " / ") no VSC"
# to_dir = "DIGITE A PASTA DE CAMINHO DE DESTINO (USE " / ") no VSC"

from_dir = "C:/Users/fcmar/Downloads"
to_dir = "C:/Users/fcmar/Downloads"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

# Classe Gerenciadora de Eventos

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(event)
        print(event.src_path)
        nome, extensao = os.path.splitext(event.src_path)
        for key, money in dir_tree.items():
            if extensao in money:
                nameOfArq = os.path.basename(event.src_path)
                origem = from_dir + "/" + nameOfArq
                destino = to_dir + "/" + key
                arqfinal = to_dir + "/" + key + "/" + nameOfArq
                time.sleep(3)
                if os.path.exists(destino):
                    print(nameOfArq + " em movimento...")
                    shutil.move(origem, arqfinal)
                    time.sleep(1)
                else:
                    os.makedirs(destino)
                    print(nameOfArq + " em movimento...")
                    shutil.move(origem, arqfinal)
                    time.sleep(1)

# Inicialize a Classe Gerenciadora de Eventos
event_handler = FileMovementHandler()

# Inicialize o Observer
observer = Observer()

# Agende o Observer
observer.schedule(event_handler, from_dir, recursive=True)

# Inicie o Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("executando...")
    
except KeyboardInterrupt:
    print("acabou")
    observer.stop()
