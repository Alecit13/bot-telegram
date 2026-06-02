from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests, time
from bs4 import BeautifulSoup
import os 

TOKEN=os.environ.get("TELEGRAM_TOKEN")

# Un comando  /Start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hola, Wasa")

async def dolar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        answer=requests.get('https://open.er-api.com/v6/latest/USD')
        if answer.status_code == 200:
            datos=answer.json()
            pen=datos["rates"]["PEN"]
            await update.message.reply_text(pen)
        else:
            return
    except requests.exceptions.ConnectionError:
        await update.message.reply_text('No se logro conectar')

async def noticias(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get("https://news.ycombinator.com/", headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        items = soup.find_all('span', class_='titleline')[:10]
        texto = "📰 Top Noticias HN:\n\n"
        for i, item in enumerate(items, 1):
            texto += f"{i}. {item.get_text()}\n"
        
        await update.message.reply_text(texto)
    except Exception as e:
        await update.message.reply_text(f"Error: {e}")


async def clima(update: Update,context: ContextTypes.DEFAULT_TYPE):
    try:
        # ✅ Mejor usar una API gratuita de clima — más confiable que scraping
        response = requests.get(
            "https://wttr.in/Lima?format=%t+%C",  # API gratuita, no necesita key
            headers={'User-Agent': 'curl/7.0'}
        )
        await update.message.reply_text(f"🌤 Lima, Surco: {response.text.strip()}")
    except Exception as e:
        await update.message.reply_text(f"Error: {e}")


app=ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler('start',start))
app.add_handler(CommandHandler('dolar',dolar))
app.add_handler(CommandHandler('clima',clima))
app.add_handler(CommandHandler('noticias',noticias))

app.run_polling()

# https://www.clima.com/peru/lima/surco  
# https://news.ycombinator.com/
# https://open.er-api.com/v6/latest/USD