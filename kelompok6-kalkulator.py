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
