from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

from core import mover_arquivo


class MeuHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            mover_arquivo(Path(event.src_path))

    def on_moved(self, event):
        if not event.is_directory:
            mover_arquivo(Path(event.dest_path))


if __name__ == "__main__":
    caminho_digitado = input("Digite o caminho da pasta a observar (Enter = ~/TESTE): ").strip()
    diretorio = Path(caminho_digitado).expanduser() if caminho_digitado else Path.home() / "TESTE"

    if not diretorio.is_dir():
        print("Erro: esse caminho não existe ou não é uma pasta.")
        exit(1)

    observer = Observer()
    observer.schedule(MeuHandler(), str(diretorio), recursive=False)
    observer.start()
    print(f"Observando: {diretorio}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\nParando...")

    observer.join()