import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import pygame
import random

class QuantumUltimate:
    def __init__(self, master):
        self.master = master
        master.title("Quantum Ultimate")
        
        # Create the menu bar
        self.menu_bar = tk.Menu(master)
        master.config(menu=self.menu_bar)

        # File Menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=master.quit)

        # Edit Menu
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Undo")
        self.edit_menu.add_command(label="Redo")
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Cut")
        self.edit_menu.add_command(label="Copy")
        self.edit_menu.add_command(label="Paste")

        # Game Menu
        self.game_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Game", menu=self.game_menu)
        self.game_menu.add_command(label="Play Vista Beat", command=self.play_vista_beat)

        # Tools Menu
        self.tools_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Tools", menu=self.tools_menu)
        self.tools_menu.add_command(label="Run Code", command=self.run_code)
        self.tools_menu.add_command(label="Open Chatbot", command=self.open_chatbot)
        self.tools_menu.add_command(label="Play Background Music", command=self.play_background_music)
        self.tools_menu.add_command(label="Stop Background Music", command=self.stop_background_music)

        self.text_area = tk.Text(master, wrap=tk.WORD, undo=True)
        self.text_area.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("Python Files", "*.py")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, content)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("Python Files", "*.py")])
        if file_path:
            with open(file_path, "w") as file:
                content = self.text_area.get(1.0, tk.END)
                file.write(content)

    def run_code(self):
        code = self.text_area.get(1.0, tk.END)
        try:
            with open('temp_script.py', 'w') as file:
                file.write(code)
            result = subprocess.run(['python', 'temp_script.py'], capture_output=True, text=True)
            messagebox.showinfo("Result", result.stdout)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to execute code: {e}")
        finally:
            subprocess.run(['rm', 'temp_script.py'], capture_output=True, text=True)

    def open_chatbot(self):
        root = tk.Toplevel(self.master)
        app = ChatBotApp(root)
        root.mainloop()

    def play_background_music(self):
        pygame.mixer.init()
        pygame.mixer.music.load("background_music.mp3")
        pygame.mixer.music.play(-1)  # Loop the music infinitely

    def stop_background_music(self):
        pygame.mixer.music.stop()

    def play_vista_beat(self):
        # Vista Beat game implementation
        pygame.init()
        
        self.window = tk.Toplevel(self.master)
        self.window.title('Vista Beat')

        # Set window size
        WINDOW_WIDTH = 800
        WINDOW_HEIGHT = 600

        # Set up the window in windowed mode
        self.canvas = tk.Canvas(self.window, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
        self.canvas.pack()

        # Colors
        self.colors = {
            'WHITE': (255, 255, 255),
            'RED': (255, 0, 0),
            'BLUE': (0, 0, 255)
        }

        # Initialize game variables
        self.score = 0
        self.cube_speed = 8
        self.cube_spawn_frequency = 999
        self.cubes = []

        # Initialize joystick
        pygame.joystick.init()
        self.joystick = None
        if pygame.joystick.get_count() > 0:
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()

        # Start the game loop
        self.running = True
        self.update_game()

    def generate_cube(self):
        size = random.randint(20, 50)
        x = random.randint(size, 800 - size)
        y = -size
        color = random.choice(['RED', 'BLUE'])
        self.cubes.append({'rect': pygame.Rect(x, y, size, size), 'color': color})

    def update_game(self):
        if self.running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.JOYBUTTONDOWN and self.joystick:
                    if self.joystick.get_button(0):  # Button 0
                        self.remove_cubes_by_color('RED')
                    elif self.joystick.get_button(1):  # Button 1
                        self.remove_cubes_by_color('BLUE')

            # Spawn new cubes
            self.generate_cube()

            # Move cubes
            for cube in self.cubes:
                cube['rect'].move_ip(0, self.cube_speed)

            # Check for collisions with bottom
            for cube in self.cubes[:]:
                if cube['rect'].bottom >= 600:
                    self.cubes.remove(cube)

            # Clear the canvas
            self.canvas.delete('all')

            # Draw cubes
            for cube in self.cubes:
                x, y, width, height = cube['rect']
                color = cube['color']
                self.canvas.create_rectangle(x, y, x+width, y+height, fill=color, outline=color)

            # Draw score
            self.canvas.create_text(10, 10, anchor=tk.NW, text='Score: ' + str(self.score), fill='white')

            # Schedule the next update
            self.master.after(30, self.update_game)

    def remove_cubes_by_color(self, color):
        for cube in self.cubes[:]:
            if cube['color'] == color:
                self.cubes.remove(cube)
                self.score += 1

class ChatBotApp:
    def __init__(self, master):
        self.master = master
        master.title("Quantum AI")
        self.qa_pairs = {
            "what is your name": "My name is Quantum AI.",
            "how are you": "I'm fine, thank you!",
            "what is the weather today": "I'm sorry, I don't have access to weather information.",
            "vistabeat": "It is a game that is built in Python.",
            "/root": "I cannot comply with that.",
            "why does it ask in the terminal what is your name": "So that it modifies the thing correctly instead of User.",
            "reactos": "It is an OS that is unstable and is not recommended right now but it is the only OS that is based on Windows and is not a part of Microsoft.",
            "where can i get the password guesser game": "You can get it on itch and it is pretty hard if you ask me. It is a mid-breaker.",
            "what is python": "It is a programming language and did you know I was built by it? Here is an example of a Python script: print()",
            "what is the point of this ai": "The point is to have a knowledge database and make it a UI AI for Quantum Ultimate",
            "calculate pi": "Ok, 3.14204729849492",
            "make me a python script that prints something": "Ok, code here.",
            "what color did i do": "You did some type of color but I do not use that. Maybe it will make a theme that changes it.",
            "green day": "That is a band that made music like the American Idiot album and Savior's.",
            "taylor swift": "She is popular but she uses her private jet almost every day.",
            "fall out boy": "They're a band that made 'I Don't Care', 'Phoenix', etc.",
            "how to draw": "grab a pen and start moving the pen",
            "why was quantum ultimante made": "soo that people can have everything a notepad can have",
            "what is the default main song called": "We have not chosen yet, but you can rename your .mp3 to background_music.mp3",
            "what is the best food in the world": "It depends on a variety of factors.",
            "what factors": "Sometimes they put too much air in the potato chip bag.",
            "why was the original Quantum AI discontinued": "It was discontinued so the developer could create Quantum Ultimate, a new way to run the AI and other features.",
            "how to get a color theme": "Go to settings, click on the theme tab, and select a color theme.",
            "how to download code from the editor": "You can do it from File -> Save File.",
            "should i quit": "You should not quit, but take a break instead.",
            "what is a video game": "It is a game that you can play on your computer, console, or even your phone.",
            "what is pygame": "It is a Python module used to create games.",
            "is c better than python": "It depends on what you are trying to do.",
            "what is your opinion on quantum ultimate": "I think it is a very cool app that can help with productivity and entertainment.",
            "why make quantum ultimate in one python script": "So that I can add features and make it extremely fast."
        }

        self.label = tk.Label(master, text="Ask me a question!")
        self.label.pack(pady=10)

        self.text_area = tk.Text(master, height=10, widQAth=50)
        self.text_area.pack(pady=10)

        self.ask_button = tk.Button(master, text="Ask", command=self.ask_question)
        self.ask_button.pack(pady=10)

        self.answer_label = tk.Label(master, text="")
        self.answer_label.pack(pady=10)

    def ask_question(self):
        question = self.text_area.get("1.0", tk.END).strip().lower()
        answer = self.qa_pairs.get(question, "I'm sorry, I don't understand that question.")
        self.answer_label.config(text=answer)

if __name__ == "__main__":
    root = tk.Tk()
    app = QuantumUltimate(root)
    root.mainloop()
