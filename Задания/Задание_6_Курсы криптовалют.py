import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

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


result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=5)


root.mainloop()