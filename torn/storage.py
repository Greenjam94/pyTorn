import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """
    Create a connection to a SQlite database
    Can create a temp db in memory by passing ':memory:' as db_file
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def create_table(conn, create_sql):
    """
    Create a table in conn db param using the create_sql param
    """
    try:
        c = conn.cursor()
        c.execute(create_sql)
    except Error as e:
        print(e)

def sqlite_query(db_file, query):
    """
    Run query param againt SQlite db_file for reading info from database
    """
    # start time
    conn = create_connection(db_file)
    with conn:
        c = conn.cursor()
        c.execute(query)

        data = c.fetchall()
    conn.close()
    # end time
    # log time to run = end - start
    return data

####
# Create various tables here, record what is currently useful to save memory
####

def create_keys_table(db_file):
    keys_conn = create_connection(db_file)
    keys_table = """CREATE TABLE IF NOT EXISTS keys (
                    id integer PRIMARY KEY,
                    player_id integer NOT NULL,
                    value text NOT NULL,
                    access_level text,
                    last_used_timestamp integer
                );"""
    # Requires users table to be created first
    create_table(keys_conn, keys_table)

def create_users_table(db_file):
    user_conn = create_connection(db_file)
    user_table = """CREATE TABLE IF NOT EXISTS users (
                        player_id integer PRIMARY KEY,
                        level integer,
                        age integer,
                        donator integer,
                        name text,
                        revivable integer,
                        life_current integer,
                        life_maximum integer,
                        life_fulltime integer,
                        status_state text,
                        status_description text,
                        status_until integer,
                        faction_id integer,
                        states_hospital integer,
                        states_jail integer,
                        last_action_status text,
                        last_action_timestamp integer
                    );"""
    # Requires factions table to be created first
    create_table(user_conn, user_table)

def create_faction_table(db_file):
    faction_conn = create_connection(db_file)
    faction_table = """CREATE TABLE IF NOT EXISTS factions (
                        faction_id integer PRIMARY KEY,
                        name text,
                        tag text,
                        leader_playerid integer,
                        coleader_playerid integer,
                        respect integer,
                        capacity integer,
                        best_chain integer
                    );"""
                        #ranked_wars
    create_table(faction_conn, faction_table)

####
# INSERT into various tables here
####

def insert_user(conn, user):
    sql = '''INSERT or REPLACE into users(player_id, level, age,
        donator, name, revivable, life_current, life_maximum,
        life_fulltime, status_state, status_description, status_until,
        faction_id, states_hospital, states_jail, last_action_status,
        last_action_timestamp) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, user)
    conn.commit()
