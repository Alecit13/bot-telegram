"""Instancias de clientes externos. Solo importa config."""
import telebot
import google.generativeai as genai
from supabase import create_client

import config

genai.configure(api_key=config.GOOGLE_API_KEY)

generation_config = {
    "temperature": 0.2,
    "response_mime_type": "application/json",
}

model = genai.GenerativeModel(config.MODEL_NAME,
                              generation_config=generation_config)

bot = telebot.TeleBot(config.TELEGRAM_TOKEN)
supabase = create_client(config.SUPABASE_URL, config.SUPABASE_KEY)