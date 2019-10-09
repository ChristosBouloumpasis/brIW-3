import pymysql
from os import environ
import sys

import subprocess

def mysql_connection():
# Connect to the database
    try:
        password = get_db_pass_from_keychain()
    except FileNotFoundError:
        try:
            password = environ["DB_PASS"]
        except KeyError:
            print("Cannot find password for db. Exiting")
            sys.exit(1)

    connection = pymysql.connect(
        host=environ.get("ACAD_SQL_HOST"),
        user=environ.get("ACAD_SQL_USER"),
        password=password,
        db=environ.get("ACAD_SQL_USER"),
        autocommit=True)
    return connection

def get_db_pass_from_keychain(name="academy_database_login"):
    pipe = subprocess.Popen(["security", "find-generic-password", "-s", f"{name}", "-w"],
                            stdout=subprocess.PIPE, text=True)
    out, err = pipe.communicate()
    return None if err else out.strip(" \n")
        