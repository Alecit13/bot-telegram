"""Lectura de catalogos: categorias y cuentas."""
from clients import supabase


def obtener_catalogos():
    """Devuelve (mapa_categorias, mapa_cuentas) como nombre -> id."""
    cats = supabase.table('categories').select('name, id_category').execute().data
    accs = supabase.table('accounts').select('name, id_account').execute().data
    return (
        {c['name']: c['id_category'] for c in cats},
        {a['name']: a['id_account'] for a in accs},
    )