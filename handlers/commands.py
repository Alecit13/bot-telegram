"""Comandos con /. Se registran ANTES que el catch-all."""
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from clients import bot
from config import CUENTA_DEFAULT
from handlers.auth import es_dueno
from services.debt import deuda_del_ciclo


@bot.message_handler(commands=['start', 'menu', 'help'])
def enviar_menu(message):
    if not es_dueno(message):
        return

    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(
        InlineKeyboardButton("Registrar gasto", callback_data='btn_registrar'),
        InlineKeyboardButton("Tablero Power BI", callback_data='btn_graficos'),
    )
    markup.add(
        InlineKeyboardButton("Anadir ingreso", callback_data='btn_ingreso'),
        InlineKeyboardButton("Presupuestos", callback_data='btn_presupuesto'),
    )
    markup.add(InlineKeyboardButton("Preguntar al Pato", callback_data='btn_asesor'))

    texto = (
        "*PatoFinanzas*\n\n"
        "Escribe tu gasto directamente (ej: `taxi 15 con la qore`)\n"
        "o usa /deuda para ver cuanto debes pagar."
    )
    bot.reply_to(message, texto, reply_markup=markup, parse_mode="Markdown")


@bot.message_handler(commands=['deuda'])
def ver_deuda(m):
    if not es_dueno(m):
        return

    r = deuda_del_ciclo(CUENTA_DEFAULT)
    if r is None:
        return bot.reply_to(m, "No pude calcular la deuda.")

    bot.reply_to(
        m,
        f"*{CUENTA_DEFAULT}*\n"
        f"Ciclo {r['desde']} a {r['hasta']}\n"
        f"Debes pagar: *S/ {r['total']}*",
        parse_mode="Markdown",
    )