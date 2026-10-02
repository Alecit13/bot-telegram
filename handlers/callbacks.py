"""Botones inline del menu."""
from clients import bot
from config import LINK_POWER_BI


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'btn_graficos':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id,
                         f"[Tu tablero financiero]({LINK_POWER_BI})",
                         parse_mode="Markdown")
    elif call.data == 'btn_registrar':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id,
                         "Escribe tu gasto. Ej: _almuerzo 15 con la latam_",
                         parse_mode="Markdown")
    else:
        bot.answer_callback_query(call.id, "En construccion")