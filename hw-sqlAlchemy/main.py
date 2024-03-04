from app import app
from db import create_tables


if __name__ == "__main__":
    # create_tables.Tables().create_tables()
    # create_tables.Tables().insert_authors_and_books()
    app.run()
