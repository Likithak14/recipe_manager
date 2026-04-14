import tkinter as tk
from PIL import Image, ImageTk
import os

class ViewRecipePage:
    def __init__(self, recipe):
        win = tk.Toplevel()
        win.title(recipe.name)
        win.geometry("500x600")

        try:
            path = os.path.join(os.getcwd(), recipe.image)
            img = Image.open(path).resize((200, 200))
            photo = ImageTk.PhotoImage(img)
            lbl = tk.Label(win, image=photo)
            lbl.image = photo
            lbl.pack()
        except:
            tk.Label(win, text="No Image").pack()

        tk.Label(win, text=recipe.name, font=("Arial", 16, "bold")).pack()
        tk.Label(win, text=f"{recipe.diet} ⭐ {recipe.rating}").pack()
        tk.Label(win, text=f"{recipe.time} mins | ₹{recipe.total_cost()}").pack()

        tk.Label(win, text="Ingredients:", font=("Arial", 12, "bold")).pack()

        for i in recipe.ingredients:
            tk.Label(win, text=f"- {i.name} ({i.amount}{i.unit})").pack()

        tk.Label(win, text="Steps:", font=("Arial", 12, "bold")).pack()

        for s in recipe.steps:
            tk.Label(win, text=s).pack()