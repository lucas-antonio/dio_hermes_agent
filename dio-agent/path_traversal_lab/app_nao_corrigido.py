from flask import Flask, request, render_template, send_file, abort
from pathlib import Path

app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent
PUBLIC_DIR = BASE_DIR / "public_files"
LAB_DIR = BASE_DIR / "lab_files"

# LAB: Intecionalmente vulnerável para aprendizado
@app.route("/view")
def view_file_vulnerable():
    name = request.args.get("file", "welcome.txt")
    # Vulnerability: caminho controlado por usuário é concatenado sem validação de contenção.
    target = PUBLIC_DIR / name
    try:
        return send_file(target, mimetype="text/plain")
    except (FileNotFoundError, IsADirectoryError):
        abort(404, "Arquivo não encontrado")

#Carrega a página inicial e lista os arquivos do public_files
@app.route("/")
def index():
    files = sorted(p.name for p in PUBLIC_DIR.glob("*.txt") if p.is_file())
    return render_template("index.html", files=files)

if __name__ == "__main__":
    # Bind only to loopback; do not expose this intentionally vulnerable lab.
    app.run(host="127.0.0.1", port=5000, debug=False)
