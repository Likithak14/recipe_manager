class Recipe:
    def __init__(self, name, ingredients, steps, diet, rating, time, image):
        self.name = name
        self.ingredients = ingredients
        self.steps = steps
        self.diet = diet
        self.rating = rating
        self.time = time
        self.image = image

    def total_cost(self):
        return sum(i.price for i in self.ingredients)