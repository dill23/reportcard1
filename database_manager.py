from replit import db
"""This function interacts with the database and adds the info"""
def add_info(name_key, name, id_key, id, grade_key, grade):
    db[name_key] = name
    db[id_key] = id
    db[grade_key] = grade
"""This funtion interacts with the database and gets the contact"""
def get_info(name):
    number = db.get(name)
    return number
"""This function looks for the keys in the database"""
def search_info(search):
    match_keys = db.prefix(search)
    return {k: db[k] for k in match_keys}
"""Updates the info in the database"""
def update_info(old_name, new_number):
    db[old_name] = new_number
"""This updates the key if you need to on the database."""
def update_key(old_name, new_name, new_number):
    db[new_name] = new_number
    del db[old_name]
"""This function deletes the info from the database"""
def delete_info(name):
    del db[name]
"""This function gets all the keys and values from the database and prints them to the console."""
def list_info():
    for keys in db.keys():
        print(keys, db[keys])