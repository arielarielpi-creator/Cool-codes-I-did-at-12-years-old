import tkinter as tk
import random
import winsound

lobby_music_file = "Hackaton/sounds/MainTheme.wav"
battle_music_file = "Hackaton/sounds/BattleTheme.wav"
feedback_short_file = "Hackaton/sounds/XP.wav"
feedback_final_file = "Hackaton/sounds/FeedBack.wav"


def stop_all_sounds():
    winsound.PlaySound(None, winsound.SND_PURGE)

def play_lobby():
    stop_all_sounds()
    winsound.PlaySound(
        lobby_music_file,
        winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP
    )

def play_battle():
    stop_all_sounds()
    winsound.PlaySound(
        battle_music_file,
        winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP
    )

def play_feedback_short():
    winsound.PlaySound(
        feedback_short_file,
        winsound.SND_FILENAME | winsound.SND_ASYNC
    )

def play_feedback_final():
    winsound.PlaySound(
        feedback_final_file,
        winsound.SND_FILENAME | winsound.SND_ASYNC
    )

root = tk.Tk()
root.title("Mind Hero")
root.attributes("-fullscreen", True)

try:
    root.iconbitmap("sounds/icon.ico")
except:
    print("לא נמצא קובץ איקון")

root.configure(bg="#0f172a")
root.geometry("800x600")

def exit_game(event=None):
    stop_all_sounds()
    root.destroy()

root.bind("<Escape>", exit_game)

exit_button = tk.Button(
    root,
    text="X",
    font=("Arial", 14, "bold"),
    bg="red",
    fg="white",
    command=exit_game
)
exit_button.place(relx=0.0, rely=0.0, anchor="nw")

player_xp = 0
player_level = 1
round_number = 0
max_rounds = 5
battle_history = []
current_mode = ""
current_questions = []

negative_thoughts = {
    "חוסר ביטחון": [
        "אני לא מספיק טוב",
        "כולם יותר מוכשרים ממני",
        "אין לי מה להציע",
        "אני תמיד טועה",
        "אני לא מעניין",
        "אף אחד לא מקשיב לי",
        "אני איטי מדי",
        "אני לא מיוחד"
    ],
    "לחץ חברתי": [
        "כולם שופטים אותי",
        "אם אדבר יצחקו עלי",
        "אני חייב להרשים",
        "אסור לי לטעות",
        "כולם שמים לב אלי",
        "אם אגיד לא – לא יאהבו אותי",
        "אני חייב להסכים עם כולם",
        "אני לא מתאים לקבוצה"
    ],
    "פחד מכישלון": [
        "אני אכשל בכל מקרה",
        "אין טעם לנסות",
        "טעויות זה מביך",
        "אם אני נכשל – זה הסוף",
        "עדיף לא להתחיל",
        "אחרים מצליחים יותר ממני",
        "אני לא בנוי לזה",
        "זה גדול עלי"
    ],
    "עייפות ולחץ": [
        "אני לא מסוגל להתרכז",
        "כלום לא מתקדם כמו שאני רוצה",
        "אני מרגיש מותש",
        "אני חייב להשלים הכל מהר",
        "אין לי זמן לעצמי"
    ],
    "ביישנות": [
        "אני לא מצליח לדבר מול אנשים",
        "כולם יותר קולניים ממני",
        "אני מפחד להביע דעה",
        "אני נעלם בקבוצה",
        "אני תמיד שקט מדי"
    ]
}

response_options = [
    "להתעלם מהמחשבה",
    "לענות במחשבה מחזקת",
    "לכתוב תשובה משלך"
]

def clear_screen():
    for widget in root.winfo_children():
        if widget != exit_button:
            widget.destroy()

def start_game(mode):
    global current_mode, round_number, battle_history, current_questions
    current_mode = mode
    round_number = 0
    battle_history = []

    current_questions = random.sample(
        negative_thoughts[mode],
        min(max_rounds, len(negative_thoughts[mode]))
    )

    random.shuffle(current_questions)
    play_battle()
    next_round()

def show_main_menu():
    stop_all_sounds()
    play_lobby()
    clear_screen()

    tk.Label(root, text="Mind Hero Arena",
             font=("Arial", 34, "bold"),
             bg="#0f172a", fg="white").pack(pady=20)

    tk.Label(root, text="בחר מצב",
             font=("Arial", 16),
             bg="#0f172a", fg="#94a3b8").pack(pady=10)

    for mode in negative_thoughts:
        tk.Button(root, text=mode,
                  font=("Arial", 14), width=25,
                  bg="#3b82f6", fg="white",
                  command=lambda m=mode: start_game(m)).pack(pady=8)

    tk.Label(root, text=f"רמה: {player_level} | XP: {player_xp}",
             font=("Arial", 12),
             bg="#0f172a", fg="#22c55e").pack(pady=20)

def next_round():
    global round_number
    if round_number >= max_rounds:
        show_summary()
        return

    thought = current_questions[round_number]
    show_battle(thought)
    round_number += 1

def show_battle(thought):
    clear_screen()

    tk.Label(root, text=f"סיבוב {round_number} מתוך {max_rounds}",
             font=("Arial", 12),
             bg="#0f172a", fg="#94a3b8").pack()

    tk.Label(root, text=f"\"{thought}\"",
             font=("Arial", 20, "bold"),
             bg="#0f172a", fg="#f87171",
             wraplength=700).pack(pady=20)

    for r in response_options:
        tk.Button(root, text=r,
                  font=("Arial", 13), width=40,
                  bg="#1e293b", fg="white",
                  command=lambda resp=r, th=thought: handle_response(resp, th)
                  ).pack(pady=6)

def handle_response(response, thought):
    global player_xp, player_level

    player_xp += 15
    if player_xp >= 100:
        player_xp -= 100
        player_level += 1

    battle_history.append((thought, response))
    show_feedback()

def show_feedback():
    clear_screen()
    play_feedback_short()

    tk.Label(root, text="פידבק קצר",
             font=("Arial", 24, "bold"),
             bg="#0f172a", fg="white").pack(pady=20)

    last_thought, last_response = battle_history[-1]

    if last_response == "לענות במחשבה מחזקת":
        feedback = "נכון מאוד! זו התגובה החזקה ביותר במצב זה."
    elif last_response == "להתעלם מהמחשבה":
        feedback = f"נכון, אבל אפשר היה לענות במחשבה מחזקת כדי להתמודד עם: \"{last_thought}\""
    else:
        feedback = f"תשובתך נרשמה: \"{last_response}\"."

    tk.Label(root, text=feedback,
             font=("Arial", 16),
             bg="#0f172a", fg="#22c55e",
             wraplength=600).pack(pady=30)

    tk.Button(root,
              text="לחץ כאן כדי להמשיך",
              font=("Arial", 14),
              bg="#3b82f6",
              fg="white",
              command=continue_to_next).pack(pady=20)

def continue_to_next(event=None):
    next_round()

def show_summary():
    clear_screen()
    play_feedback_final()

    tk.Label(root, text="סיכום הקרב",
             font=("Arial", 26, "bold"),
             bg="#0f172a", fg="white").pack(pady=20)

    strong = sum(1 for _, r in battle_history if r == "לענות במחשבה מחזקת")
    total = len(battle_history)

    tk.Label(root,
             text=f"הצלחת ב-{strong} מתוך {total} סיבובים",
             font=("Arial", 14),
             bg="#0f172a",
             fg="#94a3b8").pack(pady=20)

    tk.Label(root,
             text=f"XP: {player_xp} | רמה: {player_level}",
             font=("Arial", 14),
             bg="#0f172a",
             fg="#22c55e").pack(pady=10)

    tk.Button(root,
              text="חזרה לתפריט",
              font=("Arial", 14),
              bg="#3b82f6",
              fg="white",
              command=show_main_menu).pack(pady=20)

play_lobby()
show_main_menu()
root.mainloop()