"""Punto de entrada."""
import logging
from threading import Thread

from clients import bot
from web import run_flask

# El ORDEN de estos imports define la precedencia de los handlers.
# messages va de ULTIMO: su handler matchea cualquier mensaje.
import handlers.commands    # noqa: F401
import handlers.callbacks   # noqa: F401
import handlers.messages    # noqa: F401

if __name__ == "__main__":
    Thread(target=run_flask, daemon=True).start()
    logging.info("PatoFinanzas iniciando...")
    bot.infinity_polling()