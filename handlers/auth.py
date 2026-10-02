"""Verificacion de identidad."""
from config import MY_USER_ID


def es_dueno(m):
    return m.from_user.id == MY_USER_ID