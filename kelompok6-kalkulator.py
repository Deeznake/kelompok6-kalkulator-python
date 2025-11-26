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

# Bagian Mark: Logika tombol & proses hitung

def button_clicked(value):
    """Mengatur perilaku ketika tombol ditekan"""
    global right_symbols, top_symbols, label, A, B, operator

    # Tombol operator: + - × ÷ dan =
    if value in right_symbols:
        if value == "=":
            if A is not None and operator is not None:
                B = label["text"]
                numA = float(A)
                numB = float(B)

                # Hitung hasil
                if operator == "+":
                    label["text"] = remove_zero_decimal(numA + numB)
                elif operator == "-":
                    label["text"] = remove_zero_decimal(numA - numB)
                elif operator == "×":
                    label["text"] = remove_zero_decimal(numA * numB)
                elif operator == "÷":
                    label["text"] = remove_zero_decimal(numA / numB)

                clear_all()

        elif value in "+-×÷":
            if operator is None:
                A = label["text"]
                label["text"] = "0"
                B = "0"

            operator = value

    # Tombol bagian atas: AC, +/-, %
    elif value in top_symbols:
        if value == "AC":
            clear_all()
            label["text"] = "0"

        elif value == "+/-":
            result = float(label["text"]) * -1
            label["text"] = remove_zero_decimal(result)

        elif value == "%":
            result = float(label["text"]) / 100
            label["text"] = remove_zero_decimal(result)

    # Tombol angka dan titik desimal
    else:
        if value == ".":
            if "." not in label["text"]:
                label["text"] += value

        elif value in "0123456789":
            if label["text"] == "0":
                label["text"] = value
            else:
                label["text"] += value
