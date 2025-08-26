import db

def add_recipe(title, notes, ingredients, instructions, user_id):
    sql = "INSERT INTO recipes (title, notes, ingredients, instructions, user_id) VALUES (?, ?, ?, ?, ?)"
    db.execute(sql, [title, notes, ingredients, instructions, user_id])

def get_recipes():
    sql = "SELECT id, title FROM recipes ORDER BY id DESC"
    return db.query(sql)

def get_recipe(recipe_id):
    sql = """SELECT recipes.id,
                    recipes.title,
                    recipes.notes,
                    recipes.ingredients,
                    recipes.instructions,
                    users.id user_id,
                    users.username
             FROM recipes, users
             WHERE recipes.user_id = users.id AND
                   recipes.id = ?"""
    return db.query(sql, [recipe_id])[0]

def update_recipe(recipe_id, title, notes, ingredients, instructions):
    sql = """UPDATE recipes SET title = ?,
                                notes = ?,
                                ingredients = ?,
                                instructions = ?
                            WHERE id = ?"""
    db.execute(sql, [title, notes, ingredients, instructions, recipe_id])

def remove_recipe(recipe_id):
    sql = "DELETE FROM recipes WHERE id = ?"
    db.execute(sql, [recipe_id])

def find_recipes(query):
    sql = """SELECT id, title
             FROM recipes
             WHERE title LIKE ? OR notes LIKE ?
             ORDER BY id DESC"""
    match = "%" + query + "%"
    return db.query(sql, [match, match])