function loadList() {
    const params = new URLSearchParams(window.location.search);
    const category = params.get("cat");

    let filtered = Object.values(recipes);

    if (category === "veg") {
        filtered = filtered.filter(r => r.diet === "vegetarian");
        document.getElementById("page-title").innerText = "Vegetarian Recipes";
    }

    if (category === "vegan") {
        filtered = filtered.filter(r => r.diet === "vegan");
        document.getElementById("page-title").innerText = "Vegan Recipes";
    }

    if (category === "quick") {
        filtered = filtered.filter(r => r.time <= 20);
        document.getElementById("page-title").innerText = "Quick Meals";
    }

    const list = document.getElementById("recipe-list");
    list.innerHTML = "";

    filtered.forEach(r => {
        list.innerHTML += `
            <div class="recipe-card" onclick="go('recipe.html?item=${r.name}')">
                <img src="${r.image}">
                <h3>${r.name}</h3>
                <p>${r.time} mins • ₹${r.cost} • ⭐ ${r.rating}</p>
            </div>
        `;
    });
}
