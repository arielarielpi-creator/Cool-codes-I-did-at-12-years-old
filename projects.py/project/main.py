import player
import random
import tkinter as tk


root = tk.Tk()
root.title("Gamble Game")
root.attributes("-fullscreen", True)
root.configure(bg="#0f172a")

def exit_game():
    root.destroy()

root.bind("<Escape>", exit_game)

exit_button = tk.Button(root, text="X", font=("Arial", 14, "bold"),
                        bg="red", fg="white", command=exit_game)
exit_button.place(relx=0.0, rely=0.0, anchor="nw")

tk.Label(root, text="Gamble Game",
         font=("Arial", 34, "bold"),
         bg="#0f172a", fg="white").pack(pady=20)

tk.Label(root, text="by Ariel Pinkas",
         font=("Arial", 16),
         bg="#0f172a", fg="#94a3b8").pack(pady=10)


gold_label = tk.Label(root, text="", font=("Arial", 18), bg="#0f172a", fg="white")
gold_label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 16), bg="#0f172a", fg="#22c55e")
result_label.pack(pady=10)

# תווית להצגת השלל הנוכחי להימור
loot_label = tk.Label(root, text="", font=("Arial", 16), bg="#0f172a", fg="#fbbf24")
loot_label.pack(pady=5)

# תווית להצגת האנימציה של המספרים
dice_animation_label = tk.Label(root, text="", font=("Arial", 72, "bold"), 
                                bg="#0f172a", fg="#f59e0b")
dice_animation_label.pack(pady=20)

current_loot = 0  # השלל הנוכחי מהתיבה (אחרי הימורים)
chest_loot = 0    # השלל המקורי מהתיבה (לפני הימורים)
animation_running = False
animation_id = None
selected_choice = None

def update_gold():
    gold_label.config(text=f"Gold: {player.player_gold}")

def update_loot_display():
    if current_loot > 0:
        loot_label.config(text=f"Current loot to gamble: {current_loot} gold")
    else:
        loot_label.config(text="No loot to gamble! Open a chest first.")

def animate_dice(counter, target_number, choice):
    """אנימציה של מספרים רצים"""
    global animation_id, animation_running
    
    if counter <= 30:  # 67 מספרים באנימציה
        # מציג מספר אקראי בין 0-99
        random_num = random.randint(0, 99)
        dice_animation_label.config(text=str(random_num))
        
        # ממשיך את האנימציה - 100ms בין כל מספר
        animation_id = root.after(100, animate_dice, counter + 1, target_number, choice)
    else:
        # מסיימים את האנימציה ומציגים את התוצאה הסופית
        animation_running = False
        dice_animation_label.config(text=str(target_number))
        
        # מפעילים את לוגיקת ההימור עם התוצאה האמיתית
        process_gamble_result(target_number, choice)

def start_animation(choice):
    """מתחילה את האנימציה של המספרים"""
    global animation_running, selected_choice, animation_id
    
    if animation_running:
        result_label.config(text="Wait for the animation to finish!")
        return
    
    # מאפשרים למשתמש לבחור שוב
    if current_loot == 0:
        result_label.config(text="No loot to gamble!")
        return
    
    # מסתירים את כפתורי ההימור בזמן האנימציה
    hide_gamble_buttons()
    
    animation_running = True
    selected_choice = choice
    
    # מנקים תוויות
    dice_animation_label.config(text="")
    result_label.config(text="Rolling dice...")
    
    # מגלגלים את המספר האמיתי שיקבע את התוצאה (0-99)
    real_roll = random.randint(0, 99)
    
    # מתחילים אנימציה שתסתיים עם המספר האמיתי
    animate_dice(0, real_roll, choice)

def process_gamble_result(roll, choice):
    """מעבדת את תוצאת ההימור אחרי האנימציה"""
    global current_loot, animation_running, player
    
    # בדיקה מיוחדת למספר 67
    if roll == 67:
        # איפוס הזהב ל-6700
        player.player_gold = 6700
        result_label.config(text=f"JACKPOT! You got 67! Your gold reset to 6700! you gamble doesnt matter!")
        dice_animation_label.config(fg="#fbbf24")  # צבע זהוב לג'קפוט
        current_loot = 0  # מאפסים את השלל
        update_gold()
        update_loot_display()
        hide_gamble_buttons()
        
        # מחזירים את הצבע אחרי 2 שניות
        root.after(2000, lambda: dice_animation_label.config(fg="#f59e0b"))
        animation_running = False
        return
    
    is_even = (roll % 2 == 0)
    
    # בדיקה אם המשתמש ניחש נכון
    if (choice == "even" and is_even) or (choice == "odd" and not is_even):
        # זכייה - הכפלת השלל
        current_loot *= 2
        result_label.config(text=f"You WON! The number showed {roll} ({'Even' if is_even else 'Odd'})! Loot doubled to: {current_loot}")
        dice_animation_label.config(fg="#22c55e")  # ירוק לזכייה
    else:
        # הפסד - מאבדים את כל השלל
        result_label.config(text=f"You LOST! The number showed {roll} ({'Even' if is_even else 'Odd'}). You lost {current_loot} gold!")
        dice_animation_label.config(fg="#ef4444")  # אדום להפסד
        
        current_loot = 0
    
    update_loot_display()
    
    # מחזירים את הצבע של תווית המספרים לצבע רגיל אחרי 2 שניות
    root.after(2000, lambda: dice_animation_label.config(fg="#f59e0b"))
    
    # מציגה שוב את כפתורי ההימור אם יש שלל, אחרת מנקה ומראה הודעה
    if current_loot > 0:
        result_label.config(text=f"You have {current_loot} gold! Want to gamble again? Choose Even or Odd")
        show_gamble_buttons()
    else:
        result_label.config(text="You have no loot left. Open a new chest to continue!")
        # מוודאים שהכפתורים מוסתרים כשנגמר השלל
        hide_gamble_buttons()
    
    animation_running = False

def open_chest():
    global current_loot, chest_loot, animation_running

    if animation_running:
        result_label.config(text="Wait for the animation to finish!")
        return

    if player.player_gold < player.chest_cost:
        result_label.config(text="Not enough gold!")
        return

    # מורידים את עלות התיבה מיד
    player.player_gold -= player.chest_cost
    
    # פותחים תיבה ומקבלים שלל
    chest_loot = player.buy_chest()  # הפונקציה מחזירה את השלל אבל לא מוסיפה לזהב
    current_loot = chest_loot

    result_label.config(text=f"You opened a chest and got {chest_loot} gold! (Cost: 30 gold deducted)")
    update_gold()
    update_loot_display()
    
    # נקה את תווית האנימציה
    dice_animation_label.config(text="")
    dice_animation_label.config(fg="#f59e0b")  # מחזירים צבע רגיל
    
    # הפעלה אוטומטית של בחירת הימור
    if current_loot > 0:
        result_label.config(text=f"You have {current_loot} gold to gamble! Choose Even or Odd")
        show_gamble_buttons()

def show_gamble_buttons():
    """מציגה את כפתורי הבחירה להימור"""
    gamble_even_btn.pack(pady=5)
    gamble_odd_btn.pack(pady=5)

def hide_gamble_buttons():
    """מסתירה את כפתורי הבחירה להימור"""
    gamble_even_btn.pack_forget()
    gamble_odd_btn.pack_forget()

def gamble_even():
    """פונקציה להימור על מספר זוגי"""
    start_animation("even")

def gamble_odd():
    """פונקציה להימור על מספר אי-זוגי"""
    start_animation("odd")

def collect():
    global current_loot, chest_loot, animation_running

    if animation_running:
        result_label.config(text="Wait for the animation to finish!")
        return

    if current_loot > 0:
        # מוסיפים את השלל לזהב
        player.player_gold += current_loot
        
        result_label.config(text=f"Collected {current_loot} gold!")
        
        # איפוס משתנים
        current_loot = 0
        chest_loot = 0
        
        update_gold()
        update_loot_display()
        hide_gamble_buttons()
        dice_animation_label.config(text="")  # מנקה את תווית האנימציה
        dice_animation_label.config(fg="#f59e0b")  # מחזירים צבע רגיל
    else:
        result_label.config(text="Nothing to collect!")

# כפתורים ראשיים
tk.Button(root, text="Open Chest", font=("Arial", 16), command=open_chest).pack(pady=10)

# מסגרת להימור
gamble_frame = tk.Frame(root, bg="#0f172a")
gamble_frame.pack(pady=10)

# כפתורי בחירה להימור
gamble_even_btn = tk.Button(gamble_frame, text="Gamble on EVEN", font=("Arial", 14), 
                           bg="#3b82f6", fg="white", command=gamble_even)
gamble_odd_btn = tk.Button(gamble_frame, text="Gamble on ODD", font=("Arial", 14), 
                          bg="#ef4444", fg="white", command=gamble_odd)

tk.Button(root, text="Collect", font=("Arial", 16), command=collect).pack(pady=10)

# אתחול התצוגה
update_gold()
update_loot_display()

root.mainloop()