import db

def add_recipe(title, notes, ingredients, instructions, user_id):
    sql = "INSERT INTO recipes (title, notes, ingredients, instructions, user_id) VALUES (?, ?, ?, ?, ?)"
    db.execute(sql, [title, notes, ingredients, instructions, user_id])

def get_recipes():
    sql = "SELECT id, title FROM recipes ORDER BY id DESC"
    return db.query(sql)

def get_recipe(recipe_id):
    sql = """SELECT recipes.title,
                    recipes.notes,
                    recipes.ingredients,
                    recipes.instructions,
                    users.username
             FROM recipes, users
             WHERE recipes.user_id = users.id AND
                   recipes.id = ?"""
    return db.query(sql, [recipe_id])[0]