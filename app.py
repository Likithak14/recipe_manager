import tkinter as tk
from tkinter import ttk
from database.recipe_database import RecipeDatabase
from gui.recipe_card import RecipeCard

class RecipeApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Recipe Manager")
        self.root.geometry("700x700")
        self.root.config(bg="#f0f0f0")

        # Header
        tk.Label(self.root, text="🍽 Recipe Manager",
                 font=("Arial", 20, "bold"),
                 bg="#2ecc71", fg="white").pack(fill="x", pady=10)

        # Buttons
        frame = tk.Frame(self.root, bg="#f0f0f0")
        frame.pack(pady=10)

        tk.Button(frame, text="All", command=lambda: self.filter("all")).pack(side="left", padx=5)
        tk.Button(frame, text="Veg", command=lambda: self.filter("vegetarian")).pack(side="left", padx=5)
        tk.Button(frame, text="Non-Veg", command=lambda: self.filter("non-veg")).pack(side="left", padx=5)

        # Scroll
        self.canvas = tk.Canvas(self.root)
        self.canvas.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(self.root, command=self.canvas.yview)
        scrollbar.pack(side="right", fill="y")

        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")

        self.frame.bind("<Configure>", lambda e:
            self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.db = RecipeDatabase()
        self.recipes = self.db.load()

        self.show(self.recipes)

    def show(self, recipes):
        for w in self.frame.winfo_children():
            w.destroy()

        for r in recipes:
            RecipeCard(self.frame, r).pack(pady=10, padx=10, fill="x")

    def filter(self, diet):
        if diet == "all":
            self.show(self.recipes)
        else:
            self.show([r for r in self.recipes if r.diet == diet])

    def run(self):
        self.root.mainloop()