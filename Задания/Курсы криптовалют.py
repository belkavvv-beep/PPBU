import tkinter as tk
from tkinter import ttk, messagebox
import requests
import threading
from datetime import datetime


# --- ФУНКЦИИ ЛОГИКИ ---

def fetch_crypto_price():
    """
    Отправляет запрос к API CoinGecko и получает текущий курс выбранной криптовалюты.
    Выполняется в отдельном потоке, чтобы не блокировать главное окно.
    """

    selected_coin = coin_combobox.get()   # Получаем выбранную криптовалюту
    coin_id = coins[selected_coin]

    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"   # Формируем URL для запроса к API

    try:

        response = requests.get(url, timeout=10)   # Отправляем GET-запрос с таймаутом 10 секунд
        response.raise_for_status()   # Проверяем, не вернул ли сервер ошибку

        data = response.json()   # Получаем JSON-ответ
        price = data[coin_id]['usd']   # Извлекаем цену в долларах
        root.after(0, update_ui_success, selected_coin, price)   # Передаем результат в главный поток для обновления интерфейса

    # Обработки ошибок
    except requests.exceptions.RequestException as e:
        root.after(0, update_ui_error, f"Ошибка сети: {e}")
    except KeyError:
        root.after(0, update_ui_error, "Ошибка: Неверный формат данных от API")
    except Exception as e:
        root.after(0, update_ui_error, f"Неизвестная ошибка: {e}")


def start_fetching():
    """
    Запускает процесс загрузки данных.
    Блокирует кнопку и запускает фоновый поток.
    """

    get_btn.config(state="disabled", text="Загрузка...")   # Блокируем кнопку, чтобы предотвратить повторные нажатия
    result_label.config(text="Получение данных...", fg="black")

    thread = threading.Thread(target=fetch_crypto_price)   # Создаем и запускаем отдельный поток для запроса
    thread.start()


def update_ui_success(coin_name, price):
    """
    Обновляет интерфейс при успешном получении данных.
    """

    get_btn.config(state="normal", text="Узнать курс в USD")   # Разблокируем кнопку и возвращаем исходный текст
    formatted_price = f"{price:,.2f}".replace(',', ' ')   # Форматируем цену: добавляем пробел для тысяч и оставляем 2 знака после запятой
    result_label.config(text=f"1 {coin_name} = {formatted_price} USD", fg="green")   # Выводим результат в метку зеленым цветом


def update_ui_error(error_msg):
    """
    Обновляет интерфейс при возникновении ошибки.
    """

    get_btn.config(state="normal", text="Узнать курс в USD")     # Разблокируем кнопку
    result_label.config(text="Не удалось загрузить данные", fg="red")       # Выводим сообщение об ошибке в метку красным цветом
    messagebox.showerror("Ошибка", error_msg)   # Показываем всплывающее окно с деталями ошибки


# --- ДАННЫЕ ---

# Словарь популярных криптовалют
coins = {
    "Bitcoin (BTC)": "bitcoin",
    "Ethereum (ETH)": "ethereum",
    "Binance Coin (BNB)": "binancecoin",
    "Solana (SOL)": "solana",
    "Ripple (XRP)": "ripple",
    "Cardano (ADA)": "cardano",
    "Dogecoin (DOGE)": "dogecoin"
}

# --- ГРАФИЧЕСКИЙ ИНТЕРФЕЙС ---

# Создаем окно приложения
root = tk.Tk()
root.title("Курсы криптовалют")
root.geometry("450x320")

current_date = datetime.now().strftime("%d.%m.%Y")   # Получаем текущую дату для заголовка

title_label = tk.Label(root, text=f"Курсы криптовалют на {current_date}", font=("Arial", 14, "bold"))   # Заголовок окна с датой
title_label.pack(pady=15)

tk.Label(root, text="Выберите криптовалюту:", font=("Arial", 14)).pack(pady=10)   # Надпись для выбора валюты

# Выпадающий список с валютами
coin_combobox = ttk.Combobox(root, values=list(coins.keys()), state="readonly", width=25, font=("Arial", 12))
coin_combobox.current(0)   # Устанавливаем Bitcoin по умолчанию
coin_combobox.pack(pady=10)

# Кнопка для получения курса
get_btn = tk.Button(root, text="Узнать курс в USD", command=start_fetching, bg="#4CAF50", fg="white",
                    font=("Arial", 14, "bold"))
get_btn.pack(pady=15)

# Вывод результата (изначально пустая)
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=10)

# Запуск главного цикла обработки событий
root.mainloop()