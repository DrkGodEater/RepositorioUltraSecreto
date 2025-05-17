
# main.py

"""
Pequeño gestor de recetas
Este script permite añadir, listar y buscar recetas simples.
"""

import json
import os

RECIPE_FILE = "recipes.json"

def load_recipes():
    if not os.path.exists(RECIPE_FILE):
        return {}
    with open(RECIPE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_recipes(recipes):
    with open(RECIPE_FILE, "w", encoding="utf-8") as f:
        json.dump(recipes, f, indent=2)

def add_recipe(name, ingredients):
    recipes = load_recipes()
    recipes[name] = ingredients
    save_recipes(recipes)
    print(f"Receta '{name}' guardada con éxito.")

def list_recipes():
    recipes = load_recipes()
    if not recipes:
        print("No hay recetas guardadas.")
        return
    for name, ingredients in recipes.items():
        print(f"\n🍽 {name}\nIngredientes: {', '.join(ingredients)}")

def find_recipe(name):
    recipes = load_recipes()
    recipe = recipes.get(name)
    if recipe:
        print(f"\n🔎 Receta encontrada: {name}")
        print("Ingredientes:", ", ".join(recipe))
    else:
        print("Receta no encontrada.")

def main():
    while True:
        print("\n== Gestor de Recetas ==")
        print("1. Añadir receta")
        print("2. Listar recetas")
        print("3. Buscar receta")
        print("4. Salir")
        option = input("Opción: ")

        if option == "1":
            name = input("Nombre de la receta: ")
            ingredients = input("Ingredientes (separados por coma): ").split(",")
            add_recipe(name.strip(), [i.strip() for i in ingredients])
        elif option == "2":
            list_recipes()
        elif option == "3":
            name = input("Nombre de la receta a buscar: ")
            find_recipe(name.strip())
        elif option == "4":
            print("Hasta luego.")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
