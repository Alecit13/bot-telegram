"""Configuracion y claves. No importa nada del proyecto."""
import os
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

CUENTA_DEFAULT = "BCP Latam Pass"
LINK_POWER_BI = "https://app.powerbi.com/view?r=eyJrIjoi..."  # TODO: link real


def get_key(key_name):
    val = os.environ.get(key_name)
    if val:
        return val
    try:
        import env
        return getattr(env, key_name)
    except Exception:
        logging.warning(f"No se encontro la clave {key_name}")
        return None


GOOGLE_API_KEY = get_key("GOOGLE_API_KEY")
TELEGRAM_TOKEN = get_key("TELEGRAM_TOKEN")
SUPABASE_URL = get_key("SUPABASE_URL")
SUPABASE_KEY = get_key("SUPABASE_KEY")

_raw_user_id = get_key("MY_USER_ID")
if not _raw_user_id:
    raise RuntimeError("Falta MY_USER_ID")
MY_USER_ID = int(_raw_user_id)

MODEL_NAME = "gemini-3.8-flash"