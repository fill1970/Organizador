from pathlib import Path
import shutil
import time

CATEGORIAS = {
    ".jpg": "imagens",
    ".jpeg": "imagens",
    ".png": "imagens",
    ".gif": "imagens",
    ".pdf": "documentos",
    ".docx": "documentos",
    ".txt": "documentos",
    ".odt": "documentos",
    ".mp4": "videos",
    ".mkv": "videos",
    ".mp3": "musicas",
    ".pptx": "slides",
}


def encontrar_destino(destino, nome):
    caminho = destino / nome
    if not caminho.exists():
        return caminho

    contador = 1
    while True:
        novo_nome = f"{caminho.stem}_{contador}{caminho.suffix}"
        novo_caminho = destino / novo_nome
        if not novo_caminho.exists():
            return novo_caminho
        contador += 1


def esperar_arquivo_estavel(caminho: Path, intervalo=0.5, tentativas=10):
    #Espera o tamanho do arquivo parar de mudar 
    tamanho_anterior = -1
    for _ in range(tentativas):
        try:
            tamanho_atual = caminho.stat().st_size
        except FileNotFoundError:
            return False

        if tamanho_atual == tamanho_anterior:
            return True

        tamanho_anterior = tamanho_atual
        time.sleep(intervalo)

    return True  
    #desiste de esperar e tenta mover mesmo assim


def mover_arquivo(caminho: Path):
    if not caminho.is_file():
        return

    if not esperar_arquivo_estavel(caminho):
        return

    extensao = caminho.suffix.lower()
    categoria = CATEGORIAS.get(extensao, "outros")

    destino = caminho.parent / categoria
    destino.mkdir(exist_ok=True)

    try:
        caminho_destino = encontrar_destino(destino, caminho.name)
        shutil.move(str(caminho), str(caminho_destino))
        print(f"Movido: {caminho.name} -> {categoria}/{caminho_destino.name}")
    except Exception as erro:
        print(f"Erro ao mover {caminho.name}: {erro}")


def organizar(diretorio: Path):
    for arquivo in diretorio.iterdir():
        mover_arquivo(arquivo)