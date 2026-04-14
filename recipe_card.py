import tkinter as tk
from PIL import Image, ImageTk
import os

class RecipeCard(tk.Frame):
    def __init__(self, parent, recipe):
        super().__init__(parent, bg="white", bd=1, relief="solid")

        self.recipe = recipe

        try:
            path = os.path.join(os.getcwd(), recipe.image)
            img = Image.open(path).resize((100, 100))
            self.photo = ImageTk.PhotoImage(img)
        except:
            self.photo = None

        tk.Label(self, image=self.photo, bg="white").pack(side="left", padx=10)

        info = tk.Frame(self, bg="white")
        info.pack(side="left")

        tk.Label(info, text=recipe.name, font=("Arial", 14, "bold"), bg="white").pack(anchor="w")
        tk.Label(info, text=f"{recipe.diet} ⭐ {recipe.rating}", bg="white").pack(anchor="w")
        tk.Label(info, text=f"{recipe.time} mins | ₹{recipe.total_cost()}", bg="white").pack(anchor="w")

        tk.Button(self, text="View", command=self.open).pack(side="right", padx=10)

    def open(self):
        from gui.view_recipe import ViewRecipePage
        ViewRecipePage(self.recipe)