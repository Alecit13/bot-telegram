# 🤖 Bot de Telegram

Bot personal construido con Python que responde comandos en tiempo real con información útil — tipo de cambio, clima y noticias tech.

## ¿Qué hace?

| Comando | Descripción |
|---|---|
| `/start` | Saludo inicial |
| `/dolar` | Tipo de cambio USD/PEN en tiempo real |
| `/clima` | Clima actual de Lima |
| `/noticias` | Top 10 noticias de Hacker News |

## Tecnologías

- `python-telegram-bot` — manejo del bot
- `requests` — consumo de APIs
- `BeautifulSoup` — scraping de noticias
- `python-dotenv` — manejo seguro del token

## Instalación

```bash
# 1. Clona el repositorio
git clone https://github.com/Alecit13/bot-telegram.git
cd bot-telegram

# 2. Instala las dependencias
pip install python-telegram-bot requests beautifulsoup4 python-dotenv

# 3. Crea tu archivo .env
echo "TELEGRAM_TOKEN=tu_token_aquí" > .env

# 4. Corre el bot
python bot.py
```

## Configuración

1. Crea tu bot en Telegram con [@BotFather](https://t.me/botfather)
2. Copia el token que te da
3. Pégalo en el archivo `.env`:

```
TELEGRAM_TOKEN=tu_token_aquí
```

## Estructura del proyecto

```
bot-telegram/
├── bot.py          # código principal
├── .env            # token (no se sube a GitHub)
├── .gitignore      # archivos ignorados
└── README.md
```

## Aprendizajes

- Programación asíncrona con `async/await`
- Consumo de APIs REST con `requests`
- Web scraping con `BeautifulSoup`
- Manejo seguro de credenciales con variables de entorno

## Autor

Alejandro Cuadros — [GitHub](https://github.com/Alecit13)
