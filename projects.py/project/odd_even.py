import player
import random
import tkinter as tk
from tkinter import messagebox
import json
import os
from datetime import datetime

# ==================== USER SYSTEM ====================
USERS_FILE = "users_data.json"

def load_users():
    """טוען את נתוני המשתמשים מהקובץ"""
    if os.path.exists(USERS_FILE):
        try:
            with open(USERS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_users(users_data):
    """שומר את נתוני המשתמשים לקובץ"""
    with open(USERS_FILE, 'w', encoding='utf-8') as f:
        json.dump(users_data, f, ensure_ascii=False, indent=2)

def create_or_login_user(username):
    """יוצר משתמש חדש או מתחבר למשתמש קיים"""
    users = load_users()
    
    if username in users:
        # משתמש קיים - מתחבר
        users[username]["last_login"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        save_users(users)
        return True, users[username]
    else:
        # משתמש חדש - יוצר
        users[username] = {
            "gold": 150,
            "chests_opened": 0,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "last_login": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        save_users(users)
        return True, users[username]

def update_user_gold(username, new_gold):
    users = load_users()
    if username in users:
        users[username]["gold"] = new_gold
        save_users(users)
        return True
    return False

def update_user_chests(username, chests_opened):
    users = load_users()
    if username in users:
        users[username]["chests_opened"] = chests_opened
        save_users(users)
        return True
    return False

def get_leaderboard():
    users = load_users()
    leaderboard = []
    for username, data in users.items():
        leaderboard.append({
            "username": username,
            "gold": data["gold"],
            "chests_opened": data["chests_opened"]
        })
    leaderboard.sort(key=lambda x: x["gold"], reverse=True)
    return leaderboard[:10]

# ==================== GAME CLASS ====================
class GambleGame:
    def __init__(self, root):
        self.root = root
        self.current_user = None
        self.current_loot = 0
        self.chest_loot = 0
        self.animation_running = False
        self.animation_id = None
        self.selected_choice = None
        
        self.setup_main_window()
        self.show_login_screen()
    
    def setup_main_window(self):
        self.root.title("Gamble Game")
        self.root.attributes("-fullscreen", True)
        self.root.configure(bg="#0f172a")
        
        def exit_game():
            self.root.destroy()
        
        self.root.bind("<Escape>", exit_game)
        
        # כפתור יציאה בפינה שמאלית עליונה
        exit_button = tk.Button(self.root, text="X", font=("Arial", 14, "bold"),
                                bg="red", fg="white", command=exit_game)
        exit_button.place(relx=0.0, rely=0.0, anchor="nw")
        
        # כפתור Leaderboard בפינה ימנית עליונה
        leaderboard_button = tk.Button(self.root, text="🏆 LEADERBOARD", font=("Arial", 14, "bold"),
                                       bg="#8b5cf6", fg="white", command=self.show_leaderboard)
        leaderboard_button.place(relx=1.0, rely=0.0, anchor="ne", x=-10, y=10)
        
        self.title_label = tk.Label(self.root, text="Gamble Game",
                                    font=("Arial", 34, "bold"),
                                    bg="#0f172a", fg="white")
        self.title_label.pack(pady=20)
        
        self.subtitle_label = tk.Label(self.root, text="by Ariel Pinkas",
                                       font=("Arial", 16),
                                       bg="#0f172a", fg="#94a3b8")
        self.subtitle_label.pack(pady=10)
        
        self.user_label = tk.Label(self.root, text="", font=("Arial", 14),
                                   bg="#0f172a", fg="#3b82f6")
        self.user_label.pack(pady=5)
        
        self.gold_label = tk.Label(self.root, text="", font=("Arial", 18),
                                   bg="#0f172a", fg="white")
        self.gold_label.pack(pady=10)
        
        self.result_label = tk.Label(self.root, text="", font=("Arial", 16),
                                     bg="#0f172a", fg="#22c55e")
        self.result_label.pack(pady=10)
        
        self.loot_label = tk.Label(self.root, text="", font=("Arial", 16),
                                   bg="#0f172a", fg="#fbbf24")
        self.loot_label.pack(pady=5)
        
        self.dice_animation_label = tk.Label(self.root, text="", font=("Arial", 72, "bold"),
                                             bg="#0f172a", fg="#f59e0b")
        self.dice_animation_label.pack(pady=20)
        
        self.game_frame = tk.Frame(self.root, bg="#0f172a")
        
        # כפתור Open Chest
        tk.Button(self.game_frame, text="📦 OPEN CHEST (30 Gold)", font=("Arial", 16),
                 command=self.open_chest, bg="#3b82f6", fg="white").pack(pady=10)
        
        # כפתורי הימור
        gamble_frame = tk.Frame(self.game_frame, bg="#0f172a")
        gamble_frame.pack(pady=10)
        
        self.gamble_even_btn = tk.Button(gamble_frame, text="🎲 GAMBLE ON EVEN", font=("Arial", 14), 
                                        bg="#22c55e", fg="white", width=15, command=self.gamble_even)
        self.gamble_even_btn.pack(side=tk.LEFT, padx=10)
        
        self.gamble_odd_btn = tk.Button(gamble_frame, text="🎲 GAMBLE ON ODD", font=("Arial", 14), 
                                       bg="#eab308", fg="white", width=15, command=self.gamble_odd)
        self.gamble_odd_btn.pack(side=tk.LEFT, padx=10)
        
        # כפתור Collect
        tk.Button(self.game_frame, text="💰 COLLECT", font=("Arial", 16),
                 command=self.collect, bg="#f97316", fg="white").pack(pady=10)
        
        # כפתור Logout
        tk.Button(self.game_frame, text="🚪 LOGOUT", font=("Arial", 12),
                 command=self.logout, bg="#64748b", fg="white").pack(pady=5)
    
    def show_login_screen(self):
        self.game_frame.pack_forget()
        
        login_frame = tk.Frame(self.root, bg="#0f172a")
        login_frame.pack(expand=True)
        
        tk.Label(login_frame, text="Gamble Game", font=("Arial", 40, "bold"),
                bg="#0f172a", fg="white").pack(pady=30)
        
        tk.Label(login_frame, text="Enter your username to start playing",
                font=("Arial", 16), bg="#0f172a", fg="#94a3b8").pack(pady=10)
        
        # מסגרת לשם המשתמש
        username_frame = tk.Frame(login_frame, bg="#0f172a")
        username_frame.pack(pady=20)
        
        tk.Label(username_frame, text="Username:", font=("Arial", 18),
                bg="#0f172a", fg="white").pack(side=tk.LEFT, padx=10)
        
        self.username_entry = tk.Entry(username_frame, font=("Arial", 18), width=20)
        self.username_entry.pack(side=tk.LEFT, padx=10)
        self.username_entry.focus_set()
        
        # כפתור Play
        tk.Button(login_frame, text="▶ PLAY", font=("Arial", 20, "bold"), width=15,
                 bg="#22c55e", fg="white", command=self.login_with_username).pack(pady=20)
        
        tk.Button(login_frame, text="❌ EXIT", font=("Arial", 14), width=15,
                 bg="#ef4444", fg="white", command=self.root.destroy).pack(pady=10)
        
        self.login_frame = login_frame
        
        # קישור מקש Enter
        self.username_entry.bind('<Return>', lambda e: self.login_with_username())
    
    def login_with_username(self):
        """מתחבר עם שם המשתמש שהוזן"""
        username = self.username_entry.get().strip()
        
        if not username:
            messagebox.showerror("Error", "Please enter a username!")
            return
        
        success, user_data = create_or_login_user(username)
        
        if success:
            self.current_user = username
            self.user_data = user_data
            player.player_gold = user_data["gold"]
            player.chests_opened = user_data["chests_opened"]
            
            self.login_frame.pack_forget()
            self.game_frame.pack(pady=20)
            self.user_label.config(text=f"👤 Welcome, {username}!")
            self.update_gold()
            self.update_loot_display()
            self.result_label.config(text="📦 Open a chest to start gambling!")
            self.dice_animation_label.config(text="")
        else:
            messagebox.showerror("Error", "Something went wrong!")
    
    def show_leaderboard(self):
        leaderboard = get_leaderboard()
        
        leaderboard_text = "🏆 TOP 10 PLAYERS 🏆\n\n"
        for i, player_data in enumerate(leaderboard, 1):
            leaderboard_text += f"{i}. {player_data['username']}: {player_data['gold']} Gold (Chests: {player_data['chests_opened']})\n"
        
        if not leaderboard:
            leaderboard_text = "No players yet. Be the first!"
        
        messagebox.showinfo("Leaderboard", leaderboard_text)
    
    def logout(self):
        self.current_user = None
        self.game_frame.pack_forget()
        self.username_entry.delete(0, tk.END)
        self.show_login_screen()
        self.result_label.config(text="")
        self.dice_animation_label.config(text="")
    
    def save_user_data(self):
        if self.current_user:
            update_user_gold(self.current_user, player.player_gold)
            update_user_chests(self.current_user, player.chests_opened)
    
    def update_gold(self):
        self.gold_label.config(text=f"💰 Gold: {player.player_gold}")
        self.save_user_data()
    
    def update_loot_display(self):
        if self.current_loot > 0:
            self.loot_label.config(text=f"🎁 Current loot to gamble: {self.current_loot} gold")
        else:
            self.loot_label.config(text="❌ No loot to gamble! Open a chest first.")
    
    def animate_dice(self, counter, target_number, choice):
        if counter <= 30:
            random_num = random.randint(0, 99)
            self.dice_animation_label.config(text=str(random_num))
            self.animation_id = self.root.after(100, self.animate_dice, counter + 1, target_number, choice)
        else:
            self.animation_running = False
            self.dice_animation_label.config(text=str(target_number))
            self.process_gamble_result(target_number, choice)
    
    def start_animation(self, choice):
        if self.animation_running:
            self.result_label.config(text="Wait for the animation to finish!")
            return
        
        if self.current_loot == 0:
            self.result_label.config(text="No loot to gamble!")
            return
        
        self.hide_gamble_buttons()
        self.animation_running = True
        self.selected_choice = choice
        self.dice_animation_label.config(text="")
        self.result_label.config(text="🎲 Rolling dice...")
        real_roll = random.randint(0, 99)
        self.animate_dice(0, real_roll, choice)
    
    def process_gamble_result(self, roll, choice):
        if roll == 67:
            player.player_gold = 6700
            self.result_label.config(text=f"🎰 JACKPOT! 🎰\nYou got 67! Your gold is now 6700!")
            self.dice_animation_label.config(fg="#fbbf24")
            self.current_loot = 0
            self.update_gold()
            self.update_loot_display()
            self.hide_gamble_buttons()
            self.root.after(3000, lambda: self.dice_animation_label.config(fg="#f59e0b"))
            self.animation_running = False
            return
        
        is_even = (roll % 2 == 0)
        
        if (choice == "even" and is_even) or (choice == "odd" and not is_even):
            self.current_loot *= 2
            self.result_label.config(text=f"🎉 YOU WON! 🎉\nThe number showed {roll} ({'Even' if is_even else 'Odd'})!\nLoot doubled to: {self.current_loot}")
            self.dice_animation_label.config(fg="#22c55e")
        else:
            self.result_label.config(text=f"💀 YOU LOST! 💀\nThe number showed {roll} ({'Even' if is_even else 'Odd'}).\nYou lost {self.current_loot} gold!")
            self.dice_animation_label.config(fg="#ef4444")
            self.current_loot = 0
        
        self.update_loot_display()
        self.root.after(2000, lambda: self.dice_animation_label.config(fg="#f59e0b"))
        
        if self.current_loot > 0:
            self.result_label.config(text=f"You have {self.current_loot} gold!\nWant to gamble again? Choose Even or Odd")
            self.show_gamble_buttons()
        else:
            self.result_label.config(text="You have no loot left.\nOpen a new chest to continue!")
            self.hide_gamble_buttons()
        
        self.animation_running = False
    
    def open_chest(self):
        if self.animation_running:
            self.result_label.config(text="Wait for the animation to finish!")
            return
        
        if player.player_gold < player.chest_cost:
            self.result_label.config(text="Not enough gold! Open chests cost 30 gold.")
            return
        
        player.player_gold -= player.chest_cost
        self.chest_loot = player.buy_chest()
        self.current_loot = self.chest_loot
        
        self.result_label.config(text=f"You opened a chest and got {self.chest_loot} gold!\n(Cost: 30 gold deducted)")
        self.update_gold()
        self.update_loot_display()
        self.dice_animation_label.config(text="")
        self.dice_animation_label.config(fg="#f59e0b")
        
        if self.current_loot > 0:
            self.result_label.config(text=f"You have {self.current_loot} gold to gamble!\nChoose Even or Odd")
            self.show_gamble_buttons()
    
    def show_gamble_buttons(self):
        self.gamble_even_btn.pack(side=tk.LEFT, padx=10)
        self.gamble_odd_btn.pack(side=tk.LEFT, padx=10)
    
    def hide_gamble_buttons(self):
        self.gamble_even_btn.pack_forget()
        self.gamble_odd_btn.pack_forget()
    
    def gamble_even(self):
        self.start_animation("even")
    
    def gamble_odd(self):
        self.start_animation("odd")
    
    def collect(self):
        if self.animation_running:
            self.result_label.config(text="Wait for the animation to finish!")
            return
        
        if self.current_loot > 0:
            player.player_gold += self.current_loot
            self.result_label.config(text=f"💰 COLLECTED {self.current_loot} GOLD! 💰")
            self.current_loot = 0
            self.chest_loot = 0
            self.update_gold()
            self.update_loot_display()
            self.hide_gamble_buttons()
            self.dice_animation_label.config(text="")
            self.dice_animation_label.config(fg="#f59e0b")
        else:
            self.result_label.config(text="Nothing to collect! Open a chest first.")

if __name__ == "__main__":
    root = tk.Tk()
    game = GambleGame(root)
    root.mainloop()