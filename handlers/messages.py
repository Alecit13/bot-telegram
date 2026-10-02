"""Catch-all: registro de gastos con IA.
IMPORTANTE: este modulo se importa DE ULTIMO en main.py.
Telebot evalua los handlers en orden de registro, y este matchea todo."""
from datetime import date

from clients import bot
from config import CUENTA_DEFAULT
from handlers.auth import es_dueno
from services.catalogs import obtener_catalogos
from services.expenses import guardar_gasto
from ai.extractor import extraer_gasto


@bot.message_handler(func=lambda m: True)
def recibir_gasto(m):
    if not es_dueno(m) or not m.text or m.text.startswith('/'):
        return

    bot.send_chat_action(m.chat.id, 'typing')

    mapa_cat, mapa_acc = obtener_catalogos()
    datos = extraer_gasto(m.text, mapa_cat, mapa_acc)

    if not datos or not datos.get('monto'):
        return bot.reply_to(m, "No entendi eso como un gasto.")

    ok, error = guardar_gasto(datos, mapa_cat, mapa_acc)
    if not ok:
        return bot.reply_to(m, error)

    bot.reply_to(
        m,
        f"Registrado: S/ {datos['monto']} - {datos.get('categoria')}\n"
        f"{datos.get('cuenta') or CUENTA_DEFAULT} - "
        f"{datos.get('fecha') or date.today().isoformat()}"
    )