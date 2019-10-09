from source.db_connect import *

def populate_dict_from_db(dataset):
    dictionary = {}

    try:
        connection = mysql_connection()
        with connection.cursor() as cursor:
        
            cursor.execute(f"SELECT * FROM {dataset};")
            results = cursor.fetchall()

            for row in results:
                key = row[0]
                value = row[1]

                dictionary[key] = value

            return dictionary

    except Exception as e:
        print(e)
        print("Issue connecting to the database")
    
    finally:
        cursor.close()
        connection.close()


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
    people_tbl = populate_dict_from_db("people_tbl")
    print(new_person.capitalize() + " has been added.")

def add_drink(new_drink):
    create_new_record("drinks_tbl", new_drink.capitalize())
    drinks_tbl = populate_dict_from_db("drinks_tbl")
    print(new_drink.capitalize() + " has been added.")
    return drinks_tbl

def create_round(maker):
    try:
        connection = mysql_connection()
        with connection.cursor() as cursor:
            # round = Round(maker, [maker])

            sql = f"""INSERT INTO round (maker, active) VALUES ({maker}, 1);"""
            cursor.execute(sql)
            connection.commit()
            # round_id = cursor.lastrowid
            # round.add_id(round_id)
            
            return round
    except Exception as e:
        print("Unable to create round.")
        print(e)
    finally:
        connection.close()

def get_all_orders_in_round(id):
    try:
        connection = mysql_connection()
        with connection.cursor() as cursor:

            sql = f"""SELECT * FROM orders WHERE round_id = {id};"""

            cursor.execute(sql)
            rows = cursor.fetchall()
            connection.commit()

            return rows
    except:
        return 0
    finally:
        connection.close()

def get_a_rounds_info(id):
    try:
        connection = mysql_connection()
        with connection.cursor() as cursor:

            sql = f"""SELECT * FROM round WHERE id = {id};"""

            cursor.execute(sql)
            rows = cursor.fetchone()
            connection.commit()
            return rows
    except:
        return 0
    finally:
        connection.close()


def get_active_round_id():
    try:
        connection = mysql_connection()
        with connection.cursor() as cursor:

            sql = f"SELECT id FROM round WHERE active = 1 ORDER BY id DESC LIMIT 1;"
            cursor.execute(sql)
            rows = cursor.fetchall()
            connection.commit()

            if len(rows) == 0:
                return 0
            
            id_row = rows[0]
            id = id_row[0]
            return id
            print(id)

    except:
        return 0
    
    finally:
        connection.close()

def end_round(id):
    try:
        connection = mysql_connection()
        with connection.cursor() as cursor:

            sql = f"UPDATE round SET active = 0 WHERE id = {id};"
            cursor.execute(sql)
            connection.commit()

    except:
        print("Failed to end round.")
    
    finally:
        connection.close()

def add_round_order(round_id, person_id, drink_id):
    try:
        connection = mysql_connection()
        with connection.cursor() as cursor:

            sql = f"""INSERT INTO orders (
                    round_id,
                    person_id,
                    drink_id)
                    VALUES (
                     '{round_id}',
                     '{person_id}',
                     '{drink_id}'
                    );"""
            cursor.execute(sql)
            connection.commit()

    except Exception as e:
        print("Issue adding order")
        print(e)
    
    finally:
        connection.close()


def modify_preferences(person_id, drink_id):
    try:
        connection = mysql_connection()
        with connection as cursor:

            sql = f"UPDATE preferences_tbl SET drink_id = {drink_id} WHERE person_id = {person_id};"
            cursor.execute(sql)
            connection.commit()

    except Exception as e:
        print(e)
        print(f"Failed to update preferences for {person_id} with {drink_id}")
    finally:
        connection.close()


def add_preferences(person_id, drink_id):
    try:
        connection = mysql_connection()
        with connection as cursor:

            sql = f"INSERT INTO preferences_tbl VALUES ({person_id}, {drink_id});"
            cursor.execute(sql)
            connection.commit()
            return populate_dict_from_db("preferences_tbl")

    except Exception as e:
        print(e)
        print(f"Failed to update preferences for {person_id} with {drink_id}")
    finally:
        connection.close()


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
        with mysql_connection() as connection:
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

def search_peoples_name(person_name):
    try:
        with mysql_connection() as connection:
            cursor = connection.cursor()

            sql = f"SELECT * FROM people_tbl ORDER BY id WHERE (name) = {person_name} LIMIT 1;"
            cursor.execute(sql)
            results = cursor.fetchall()
            connection.close()

            return results
    except:
        print("Issue searching person")