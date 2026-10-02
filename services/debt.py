"""Calculo de deuda del ciclo. Llama a la funcion deuda_tarjeta en Postgres."""
import logging

from clients import supabase


def deuda_del_ciclo(nombre_cuenta):
    """Devuelve dict con desde/hasta/total, o None si no hay datos."""
    try:
        resp = supabase.rpc('deuda_tarjeta',
                            {'nombre_cuenta': nombre_cuenta}).execute()
        return resp.data[0] if resp.data else None
    except Exception as e:
        logging.error(f"Error deuda: {e}")
        return None