from source.db_connect import *

def populate_dict_from_db(dataset):
    dictionary = {}

    try:
        connection = mysql_connection()
        cursor = connection.cursor()

        cursor.execute(f"SELECT * FROM {dataset}")
        results = cursor.fetchall()

        for row in results:
            key = row[0]
            value = row[1]

            dictionary[key] = value
        return dictionary

        connection.close()

    except Exception as e:
        print(e)
        print("Issue connecting to the database")
    
    finally:
        cursor.close()


def save_dictionary(dataset, dictionary_to_save):
    try:
        connection = mysql_connection()
        cursor = connection.cursor()

        for key, value in dictionary_to_save.items():
            sql = f"UPDATE {dataset} SET name = '{value}' WHERE id = {key}"
            rows = cursor.execute(sql)
        
        # connection.commit()
        connection.close()
    except Exception as e:
        print(e)
        print(f"Failed to write to the database for {dataset}")


def create_new_record(db_table, value):
    try:
        connection = mysql_connection()
        cursor = connection.cursor()

        sql = f"INSERT INTO {db_table} (name) VALUES ('{value}')"
        cursor.execute(sql)
        connection.commit()
        connection.close()

    except Exception as e:
        print(e)
        print(f"Failed to write to the database for {dataset}")

def add_person(new_person):
    create_new_record("people_tbl", new_person.capitalize())
    # people_tbl = populate_dict_from_db("people_tbl")
    print(new_person.capitalize() + " has been added.")

def add_drink(new_drink):
    create_new_record("drinks_tbl", new_drink.capitalize())
    drinks_tbl = populate_dict_from_db("drinks_tbl")
    print(new_drink.capitalize() + " has been added.")
    return drinks_tbl

# def create_round(maker, people_list):
#     round = Round(maker, [maker])
#     round_data = Round.get_all_data()

#     try:
#         connection = mysql_connection()
#         cursor = connection.cursor()
# # id maker people_ids active
#         sql = f"INSERT INTO round (
#             maker,
#             people_ids,
#             active)
#             VALUES (
#                 '{maker}',
#                 '
#             );"


def modify_preferences(person_id, drink_id):
    try:
        connection = mysql_connection()
        cursor = connection.cursor()

        sql = f"UPDATE preferences_tbl SET person_id = '{person_id}' AND SET drink_id = {drink_id}"
        cursor.execute(sql)
        connection.commit()
        connection.close()
        return populate_dict_from_db("preferences_tbl")

    except Exception as e:
        print(e)
        print(f"Failed to update preferences for {person_id} with {drink_id}")

def remove_person(remove_person): 
    try:
        connection = mysql_connection()
        cursor = connection.cursor()

        sql = f"DELETE FROM people_tbl WHERE id = {remove_person};"
        cursor.execute(sql)
        connection.commit()
        connection.close()

        # removing_person = people_tbl.pop(remove_person)
        print(f"ID {remove_person} has been removed.")
        dictionary = populate_dict_from_db("people_tbl")
        return dictionary

    except Exception as e:
        print(e)
        print("Issue removing person")


def remove_drink(remove_drink):
    try:
        connection = mysql_connection()
        cursor = connection.cursor()

        sql = f"DELETE FROM drinks_tbl WHERE id = {remove_drink};"
        cursor.execute(sql)
        connection.commit()
        connection.close()

        # removing_person = people_tbl.pop(remove_person)
        print(f"ID {remove_drink} has been removed.")
        dictionary = populate_dict_from_db("drinks_tbl")
        return dictionary
    except:
        print("Issue removing drink")