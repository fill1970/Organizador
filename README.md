# Organizador de Arquivos           

Script em Python que organiza arquivos automaticamente em pastas por categoria
(imagens, documentos, vídeos, músicas, slides, outros), com base na extensão.

## Estrutura

- `core.py` — lógica principal: categorias, renomeio de duplicatas e movimentação de arquivos
- `main.py` — organiza os arquivos existentes na pasta uma única vez
- `observador.py` — fica rodando e organiza novos arquivos em tempo real (usa `watchdog`)

## Requisitos

- Python 3.8+
- Biblioteca `watchdog`

Instalar dependência:
```bash
pip install watchdog
```

## Como usar

### Organizar uma vez
```bash
python main.py
```
Vai pedir o caminho da pasta (Enter usa `~/TESTE` como padrão).

### Observar em tempo real
```bash
python observador.py
```
Também pede o caminho da pasta. Fica rodando até `Ctrl+C`.

## Categorias

| Extensão | Categoria |
|---|---|
| .jpg, .jpeg, .png, .gif | imagens |
| .pdf, .docx, .txt, .odt | documentos |
| .mp4, .mkv | videos |
| .mp3 | musicas |
| .pptx | slides |
| outras | outros |

Arquivos duplicados não são sobrescritos — recebem sufixo `_1`, `_2`, etc.

## Status

Projeto pessoal, em desenvolvimento. Sem logs em arquivo ainda (só terminal).