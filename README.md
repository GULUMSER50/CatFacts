# Cat Facts Project

This project is a Python application designed to fetch cat facts from an online API, store them in a SQLite database, and retrieve them for display. The project consists of several components:

## Components

1. **Database Connection (`db_conn.py`)**:
   - Functions to create a connection to a SQLite database.
   - Functions to create a table (`cat_facts`) in the database.
   - Functions to save cat facts to the database.
   - Functions to retrieve cat facts from the database.

2. **Constants (`constants.py`)**:
   - Contains configuration constants such as the database file name, API URL, maximum retries, and retry delay.

3. **Main Application (`main.py`)**:
   - Orchestrates the workflow of the application:
     - Establishes a connection to the SQLite database.
     - Creates the `cat_facts` table if it does not exist.
     - Fetches cat facts from the API with retry logic.
     - Saves the fetched cat facts to the database.
     - Retrieves and prints the cat facts from the database.

4. **API Interaction**:
   - Uses the `requests` library to fetch data from the `catfact.ninja` API.
   - Implements retry logic to handle transient errors when fetching data from the API.

The project is structured to handle errors gracefully, ensuring that the application can retry fetching data in case of failures and log appropriate messages for debugging.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/GulumserEskiturk/cat-facts-project.git
   cd cat-facts-project