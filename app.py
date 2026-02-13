import os
import requests

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def generar_texto():
    return "🍅 Consejo gastronómico del día: añade sal al tomate 10 min antes de servir para potenciar sabor."

def enviar_mensaje(texto):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": texto
    }
    requests.post(url, json=payload)

if __name__ == "__main__":
    mensaje = generar_texto()
    enviar_mensaje(mensaje)
