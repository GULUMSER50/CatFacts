
from db_conn import create_db_table, get_cat_facts, save_cat_facts, get_cat_facts_from_db, create_connection
from constant import db_file, url, max_retries, retry_delay


if __name__ == "__main__":
    # create the database connection
    conn = create_connection(db_file)
    # create the database table
    create_db_table(db_file)
    # get cat facts
    data = get_cat_facts(url, max_retries, retry_delay)
    # save cat facts to the database
    save_cat_facts(db_file, data)
    # get cat facts from the database
    facts = get_cat_facts_from_db(db_file)
    print(facts)
