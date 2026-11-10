import tkinter as tk
from tkinter import ttk, messagebox
import requests
import threading
from datetime import datetime


def fetch_crypto_price():

    selected_coin = coin_combobox.get()
    coin_id = coins[selected_coin]

    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"

    try:

        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()
        price = data[coin_id]['usd']

        root.after(0, update_ui_success, selected_coin, price)


    except requests.exceptions.RequestException as e:
        root.after(0, update_ui_error, f"Ошибка сети: {e}")
    except KeyError:
        root.after(0, update_ui_error, "Ошибка: Неверный формат данных от API")
    except Exception as e:
        root.after(0, update_ui_error, f"Неизвестная ошибка: {e}")


def start_fetching():

    get_btn.config(state="disabled", text="Загрузка...")
    result_label.config(text="Получение данных...", fg="black")

    thread = threading.Thread(target=fetch_crypto_price)
    thread.start()


def update_ui_success(coin_name, price):
    get_btn.config(state="normal", text="Узнать курс в USD")
    formatted_price = f"{price:,.2f}".replace(',', ' ')
    result_label.config(text=f"1 {coin_name} = {formatted_price} USD", fg="green")

def update_ui_error(error_msg):
    get_btn.config(state="normal", text="Узнать курс в USD")
    result_label.config(text="Не удалось загрузить данные", fg="red")
    messagebox.showerror("Ошибка", error_msg)


coins = {
    "Bitcoin (BTC)": "bitcoin",
    "Ethereum (ETH)": "ethereum",
    "Binance Coin (BNB)": "binancecoin",
    "Solana (SOL)": "solana",
    "Ripple (XRP)": "ripple",
    "Cardano (ADA)": "cardano",
    "Dogecoin (DOGE)": "dogecoin"
}


root = tk.Tk()
root.title("Курсы криптовалют")
root.geometry("450x320")

current_date = datetime.now().strftime("%d.%m.%Y")

title_label = tk.Label(root, text=f"Курсы криптовалют на {current_date}", font=("Arial", 14, "bold"))
title_label.pack(pady=15)

tk.Label(root, text="Выберите криптовалюту:", font=("Arial", 12)).pack(pady=5)

coin_combobox = ttk.Combobox(root, values=list(coins.keys()), state="readonly", width=25, font=("Arial", 12))
coin_combobox.current(0)
coin_combobox.pack(pady=5)

get_btn = tk.Button(root, text="Узнать курс в USD", command=start_fetching, bg="#4CAF50", fg="white",
                    font=("Arial", 10, "bold"))
get_btn.pack(pady=15)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=5)


root.mainloop()