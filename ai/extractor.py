"""Llama al modelo y devuelve datos estructurados."""
import json
import logging

from clients import model
from ai.prompts import prompt_gasto


def extraer_gasto(texto, mapa_cat, mapa_acc):
    """Devuelve dict con los datos del gasto, o None si fallo."""
    try:
        res = model.generate_content(prompt_gasto(texto, mapa_cat, mapa_acc))
        limpio = res.text.replace('```json', '').replace('```', '').strip()
        return json.loads(limpio)
    except Exception as e:
        logging.error(f"Error extrayendo gasto: {e}")
        return None