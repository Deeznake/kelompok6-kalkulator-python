# Bagian Meike: Pembuatan tombol dan pengaturan posisi

for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]

        button = tkinter.Button(frame, text=value, font=("Arial", 30),
                                width=column_count - 1, height=1,
                                command=lambda value=value: button_clicked(value))

        if value in top_symbols:
            button.config(foreground=color_black, background=color_light_gray)
        elif value in right_symbols:
            button.config(foreground=color_white, background=color_orange)
        else:
            button.config(foreground=color_white, background=color_dark_gray)

        button.grid(row=row + 1, column=column)

frame.pack()

# Posisi window di tengah layar
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()
