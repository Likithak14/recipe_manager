import os
from models.recipe import Recipe
from models.ingredient import Ingredient

class RecipeDatabase:
    def load(self):
        image_folder = "images"
        files = os.listdir(image_folder)

        recipes = []

        for file in files:
            if file.endswith(".jpg") or file.endswith(".png"):
                name = file.replace(".jpg", "").replace(".png", "")

                # AUTO CATEGORY LOGIC
                nonveg_keywords = ["Chicken", "Fish", "Egg"]
                if any(word in name for word in nonveg_keywords):
                    diet = "non-veg"
                else:
                    diet = "vegetarian"

                # SAMPLE INGREDIENTS & STEPS
                ingredients = [
                    Ingredient("Main Ingredient", 1, "plate", 100)
                ]

                steps = [
                    f"Prepare {name}",
                    "Cook properly",
                    "Serve hot"
                ]

                recipes.append(
                    Recipe(
                        name,
                        ingredients,
                        steps,
                        diet,
                        4.5,
                        20,
                        f"images/{file}"
                    )
                )

        return recipes