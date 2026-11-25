# Path Traversal Lab (local)

Site simples para estudo de Path Traversal, com um endpoint intencionalmente vulnerável e outro com validação de caminho.


## Requisitos
- Python 3.9+
- Flask

## Executar
```bash
cd path_traversal_lab
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```
Abra `http://127.0.0.1:5000` no navegador.

## Endpoints
- `/view?file=welcome.txt`: demonstração intencionalmente vulnerável (somente laboratório local).
- `/view-safe?file=welcome.txt`: exemplo de correção que limita os caminhos à pasta `public_files`.

O servidor escuta apenas em `127.0.0.1`. Não exponha esse laboratório à rede ou à internet.
