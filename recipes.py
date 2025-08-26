import db

def add_recipe(title, notes, ingredients, instructions, user_id):
    sql = "INSERT INTO recipes (title, notes, ingredients, instructions, user_id) VALUES (?, ?, ?, ?, ?)"
    db.execute(sql, [title, notes, ingredients, instructions, user_id])