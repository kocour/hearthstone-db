import json
import os
import sqlite3

def main():
    conn = sqlite3.connect('all-cards.db')
    c = conn.cursor()
    sets = {"gvg": "Goblins vs Gnomes",
            "tgt": "The Grand Tournament",
            "brm": "Blackrock Mountain",
            "loe": "The League of Explorers",
            "con": "Curse of Naxxramas"}
    result = None
    myfile = os.path.join("cards", "all-cards.json")
    c.execute('''CREATE TABLE IF NOT EXISTS heroes
                 (id integer primary key, name text unique)''')
    c.execute('''CREATE TABLE IF NOT EXISTS types
                 (id integer primary key, name text unique)''')
    c.execute('''CREATE TABLE IF NOT EXISTS qualities
                 (id integer primary key, name text unique)''')
    c.execute('''CREATE TABLE IF NOT EXISTS subtypes
                 (id integer primary key, type_id integer, name text unique, FOREIGN KEY(type_id) REFERENCES types(id))''')
    c.execute('''CREATE TABLE IF NOT EXISTS sets
                 (id integer primary key, name text unique, abbreviation text unique)''')
    c.execute('''CREATE TABLE IF NOT EXISTS cards
                 (id integer primary key, name text unique, description text, hero_id integer, type_id integer, quality_id integer,
                 subtype_id integer, set_id integer, image_url text, mana integer, attack integer, health integer,
                 collectible integer, FOREIGN KEY(hero_id) REFERENCES heroes(id), FOREIGN KEY(type_id) REFERENCES types(id),
                 FOREIGN KEY(quality_id) REFERENCES qualities(id), FOREIGN KEY(subtype_id) REFERENCES subtypes(id),
                 FOREIGN KEY(set_id) REFERENCES sets(id))''')
    c.execute('''CREATE TABLE IF NOT EXISTS effects
                 (id integer primary key, name text unique)''')
    c.execute('''CREATE TABLE IF NOT EXISTS card_effects
                 (id integer primary key, card_id integer, effect_id integer, description text, FOREIGN KEY(card_id) REFERENCES cards(id), FOREIGN KEY(effect_id) REFERENCES effects(id))''')
    with open(myfile) as fp:
        stuff = json.load(fp)
        id = None
        name = None
        description = None
        image_url = None
        hero = None
        type = None
        quality = None
        race = None
        set = None
        mana = None
        attack = None
        health = None
        collectible = None
        effect_list = None
        for k, v in stuff.items():
            if k == "cards":
                for card in v:
                    hero_id = insert_or_get_id(c, "heroes", {"name": card["hero"]})
                    type_id = insert_or_get_id(c, "types", {"name": card["type"]})
                    quality_id = insert_or_get_id(c, "qualities", {"name": card["quality"]})
                    if card["race"] is not None:
                        subtype_id = insert_or_get_id(c, "subtypes", {"name": card["race"], "type_id": type_id})
                    else:
                        subtype_id = None
                    set_id = insert_or_get_id(c, "sets", {"name": sets[card["set"]] if card["set"] in sets else card["set"], "abbreviation": card["set"] if card["set"] in sets else None})
                    for effect in card["effect_list"]:
                        effect_id = insert_or_get_id(c, "effects", {"name": effect["effect"]})
                        card_effect_id = insert_or_get_id(c, "card_effects", {"card_id": card_id, "effect_id": effect_id, "description": effect["extra"]})
                    card_id = insert_or_get_id(c, "cards", { "id": card["id"], "name": card["name"], "description": card["description"], "image_url": card["image_url"],
                                                              "hero_id": hero_id, "type_id": type_id, "quality_id": quality_id, "subtype_id": subtype_id, "set_id": set_id,
                                                              "mana": card["mana"],
                                                              "attack": card["attack"],
                                                              "health": card["health"],
                                                              "collectible": card["collectible"] })
    conn.commit()
def insert_or_get_id(cursor, table, args):
    keys = []
    values = []
    for key in args.keys():
        if args[key]:
            keys.append("\"" + key + "\"")
            values.append("\"" + str(args[key]) + "\"")
    if not keys:
        return None
    query = "INSERT OR IGNORE INTO " + table + "(" + ", ".join(keys) + ")" +" VALUES(" + ", ".join(values) + ");"
    cursor.execute(query)
    if "name" in args:
        cursor.execute("SELECT id from {} WHERE name = ?".format(table), (args["name"], ) )
        result = cursor.fetchone()
        if result is not None:
            return result[0]
    return None
if __name__ == "__main__":
    main()
