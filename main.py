import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Крестики-нолики")
window.geometry("262x382")


buttons = []
click_cnt = 0
player_wins = {"X": 0, "O": 0}  # Счетчик побед для "X" и "O"
player_choice = tk.StringVar(value="X")  # Выбор символа (X или O)

def check_winner():
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return True
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return True

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True

    return False


def reset_board():
    global click_cnt, current_player
    current_player = player_choice.get()
    click_cnt = 0
    for row in range(3):
        for col in range(3):
            buttons[row][col]['text'] = ""


def on_click(row, col):
    global current_player, click_cnt

    if buttons[row][col]['text'] != "":
        return

    buttons[row][col]['text'] = current_player

    if check_winner():
        player_wins[current_player] += 1
        messagebox.showinfo("Игра окончена", f"Игрок {current_player} победил!")
        reset_board()

        if player_wins[current_player] == 3:
            messagebox.showinfo("Игра окончена", f"Игрок {current_player} выиграл игру!")
            window.quit()
    else:
        click_cnt += 1
        if click_cnt == 9:
            messagebox.showinfo("Игра окончена", "Ничья")
            reset_board()
        else:
          current_player = "O" if current_player == "X" else "X"


def start_game():
    global current_player
    current_player = player_choice.get()
    reset_board()

    # Активируем кнопки игрового поля
    for row in buttons:
        for btn in row:
            btn.config(state=tk.NORMAL)

    # Отключаем радиокнопки после начала игры
    for radio in radio_buttons:
        radio.config(state=tk.DISABLED)

    # Отключаем кнопку "Старт" после начала игры
    start_button.config(state=tk.DISABLED)

# Создание радиокнопок для выбора символа
choice_label = tk.Label(window, text="Выберите символ:", font=("Arial", 14))
choice_label.grid(row=0, column=0, columnspan=3)

radio_buttons = [
    tk.Radiobutton(window, text="Крестик (X)", variable=player_choice, value="X", font=("Arial", 12)),
    tk.Radiobutton(window, text="Нолик (O)", variable=player_choice, value="O", font=("Arial", 12))
]

for i, radio in enumerate(radio_buttons):
    radio.grid(row=1+i, column=0, columnspan=3)

start_button = tk.Button(window, text="Начать игру", command=start_game, font=("Arial", 14))
start_button.grid(row=3, column=0, columnspan=3)

# Создание игрового поля
for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(window, text="", font=("Arial", 20), width=5, height=2, command=lambda r=i, c=j: on_click(r, c))
        btn.grid(row=i+4, column=j)
        btn.config(state=tk.DISABLED)  # Делаем кнопки неактивными
        row.append(btn)
    buttons.append(row)

window.mainloop()
