import sqlite3

import requests
import time

# create connection to the database
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connection to {db_file} established successfully")
    except sqlite3.Error as e:
        print(e)
    return conn


# an alternative way to get cat facts
def get_cat_facts(url, max_retries=5, retry_delay=5):
    """
    Get cat facts from the API
    :param url:
    :param max_retries:
    :param retry_delay:
    :return:
    """
    for attempt in range(max_retries):
        try:
            response = requests.get(url)
            response.raise_for_status()  # raise an exception for 4xx/5xx status codes
            print(f"Request to {url} is successful. Status code: {response.status_code}")
            return response.json()['data']
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}. Attempt {attempt + 1}/{max_retries}. Retrying in {retry_delay} seconds...")
            time.sleep(retry_delay)
    return None


def create_db_table(db_file):
    """
    Create a table in the database
    :param db_file:
    :return:
    """
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS cat_facts (fact TEXT)")
    print("Table cat_facts created successfully")
    conn.commit()
    conn.close()


def save_cat_facts(db_file, data):
    """
    Save cat facts to the database
    :param db_file:
    :param data:
    :return:
    """
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    for fact in data:
        c.execute("INSERT INTO cat_facts VALUES (?)", (fact['fact'],))
        print(f"Fact '{fact['fact']}' saved successfully to cat_facts table")
    conn.commit()
    conn.close()


def get_cat_facts_from_db(db_file):
    """
    Get cat facts from the database
    :param db_file:
    :return:
    """
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute("SELECT fact FROM cat_facts")
    print("Facts retrieved successfully from cat_facts table")
    facts = c.fetchall()
    conn.close()
    return facts




