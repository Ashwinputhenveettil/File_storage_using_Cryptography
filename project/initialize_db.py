import sqlite3

DB_PATH = "database_file/file_split.db"

def initialize_database():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # Create tables
    c.execute('''
        CREATE TABLE IF NOT EXISTS user (
            username TEXT,
            password TEXT,
            email TEXT,
            dob TEXT,
            city TEXT,
            cno TEXT
        )
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS owner (
            username TEXT,
            password TEXT,
            email TEXT,
            dob TEXT,
            city TEXT,
            cno TEXT
        )
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS file (
            data BLOB,
            filename TEXT,
            CDate TEXT,
            content TEXT,
            owner TEXT,
            f1 TEXT,
            f2 TEXT,
            f3 TEXT
        )
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS cloudadata (
            filename TEXT,
            owner TEXT,
            f1 TEXT,
            skey TEXT,
            f2 TEXT,
            skey1 TEXT,
            f3 TEXT,
            skey2 TEXT,
            data TEXT
        )
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS request (
            filename TEXT,
            data TEXT,
            owner TEXT,
            status TEXT,
            email TEXT,
            s1 TEXT,
            s2 TEXT,
            s3 TEXT,
            p1 TEXT,
            p2 TEXT,
            p3 TEXT
        )
    ''')

    conn.commit()
    conn.close()
    print(" Database initialized with required tables.")

if __name__ == "__main__":
    initialize_database()
