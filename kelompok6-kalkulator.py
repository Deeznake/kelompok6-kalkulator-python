# Bagian Gerry: Desain UI, konfigurasi window, tampilan label

import tkinter

button_values = [
    ["AC", "+/-", "%", "÷"], 
    ["7", "8", "9", "×"], 
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]

row_count = len(button_values)
column_count = len(button_values[0])

color_light_gray = "#D4D4D2"
color_black = "#1C1C1C"
color_dark_gray = "#505050"
color_orange = "#FF9500"
color_white = "white"

window = tkinter.Tk()
window.title("Calculator")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text="0", font=("Arial", 45),
                      background=color_black, foreground=color_white,
                      anchor="e", width=column_count)
label.grid(row=0, column=0, columnspan=column_count, sticky="we")

# Bagian Kenzo: Variabel data global & fungsi utilitas

A = "0"
operator = None
B = None

def clear_all():
    """Menghapus semua input dan mengatur ulang kalkulator"""
    global A, B, operator
    A = "0"
    operator = None
    B = None

def remove_zero_decimal(num):
    """Menghapus .0 di angka seperti 12.0 menjadi 12"""
    if num % 1 == 0:
        num = int(num)
    return str(num)
