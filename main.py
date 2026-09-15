from pathlib import Path
from core import organizar


if __name__ == "__main__":
    caminho_digitado = input("Digite o caminho da pasta a organizar (Enter = ~/TESTE): ").strip()
    diretorio = Path(caminho_digitado).expanduser() if caminho_digitado else Path.home() / "TESTE"

    if not diretorio.is_dir():
        print("Erro: esse caminho não existe ou não é uma pasta.")
        exit(1)

    organizar(diretorio)

