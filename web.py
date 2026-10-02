"""Servidor keep-alive. Independiente del bot."""
import os
from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET', 'HEAD'])
def index():
    return "PatoFinanzas activo.", 200


def run_flask():
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)