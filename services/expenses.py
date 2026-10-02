"""Escritura de transacciones. Nunca responde por Telegram."""
import logging
from datetime import date

from clients import supabase
from config import MY_USER_ID, CUENTA_DEFAULT


def guardar_gasto(datos, mapa_cat, mapa_acc):
    """Devuelve (ok, mensaje_error)."""
    cat_id = mapa_cat.get(datos.get("categoria"))
    acc_id = mapa_acc.get(datos.get("cuenta")) or mapa_acc.get(CUENTA_DEFAULT)

    if cat_id is None:
        return False, f"No reconoci la categoria '{datos.get('categoria')}'"
    if acc_id is None:
        return False, "No reconoci la cuenta"

    fila = {
        "id_user": MY_USER_ID,
        "amount": datos["monto"],
        "transaction_date": datos.get("fecha") or date.today().isoformat(),
        "type": "gastos",
        "id_category": cat_id,
        "id_account": acc_id,
        "description": datos.get("descripcion"),
    }
    try:
        supabase.table("transactions").insert(fila).execute()
        return True, None
    except Exception as e:
        logging.error(f"Error BD: {e}")
        return False, "Error guardando en la base de datos"