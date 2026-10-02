"""Construccion de prompts. Texto puro, sin llamadas."""
from datetime import date

from config import CUENTA_DEFAULT


def prompt_gasto(texto, mapa_cat, mapa_acc):
    return f"""
Eres un asistente contable. Hoy es {date.today().isoformat()}.
CATEGORIAS VALIDAS: {list(mapa_cat.keys())}
CUENTAS VALIDAS: {list(mapa_acc.keys())}

Reglas:
- "categoria" y "cuenta" deben ser EXACTAMENTE un string de las listas.
- Si no se menciona cuenta, usa "{CUENTA_DEFAULT}".
- "fecha" en formato YYYY-MM-DD. Si no se menciona, usa hoy.

Mensaje: "{texto}"

Responde solo JSON:
{{"monto": 0.0, "categoria": "", "cuenta": "", "fecha": "", "descripcion": ""}}
"""