import sqlite3
import datetime

user_db_file_location = "database_file/file_split.db"

def db_connect():
    return sqlite3.connect(user_db_file_location)

def user_reg(email, password, dob, city, cno):
    _conn = db_connect()
    _c = _conn.cursor()
    _c.execute("INSERT INTO user (email, password, dob, city, cno) VALUES (?, ?, ?, ?, ?)",
               (email, password, dob, city, cno))
    _conn.commit()
    _conn.close()
    return True


def user_loginact(email, password):
    _conn = db_connect()
    _c = _conn.cursor()
    _c.execute("SELECT * FROM user WHERE email=? AND password=?", (email, password))
    result = _c.fetchall()
    _conn.close()
    return bool(result)  # Return True if a user is found, False otherwise

def owner_reg(email, password, dob, city, cno):
    _conn = db_connect()
    _c = _conn.cursor()
    _c.execute("INSERT INTO owner (email, password, dob, city, cno) VALUES (?, ?, ?, ?, ?)",
               (email, password, dob, city, cno))
    _conn.commit()
    _conn.close()
    return True


def owner_login(email, password):
    _conn = db_connect()
    _c = _conn.cursor()
    _c.execute("SELECT * FROM owner WHERE email=? AND password=?", (email, password))
    result = _c.fetchall()
    _conn.close()
    return bool(result)


def upload_file(filename, file, email, pk, mk):
    _conn = db_connect()
    _c = _conn.cursor()
    current_timestamp = str(datetime.datetime.now())
    name = file.filename
    data = file.read()
    _c.execute("INSERT INTO file VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
               (data, filename, current_timestamp, data.decode('utf-8'), email, "no", "no", "no"))
    _conn.commit()
    _conn.close()
    return True

def owner_viewfiles(username):
    _conn = db_connect()
    _c = _conn.cursor()
    _c.execute("SELECT rowid, filename, data, CDate, owner FROM file WHERE owner=?", (username,))
    result = _c.fetchall()
    _conn.commit()
    _conn.close()
    return result

def upload_clouddata(data, fname, owner, desencrypted, DESkey_16, aesencrypted, AESkey_16, rsaencrypted, RSAkey_16):
    _conn = db_connect()
    _c = _conn.cursor()
    _c.execute("INSERT INTO cloudadata VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
               (fname, owner, desencrypted, DESkey_16, aesencrypted, AESkey_16, rsaencrypted, RSAkey_16, data))
    _conn.commit()
    _conn.close()
    return True

def onwer_viewdata(username):
    _conn = db_connect()
    _c = _conn.cursor()
    _c.execute("SELECT filename, f1, f2, f3 FROM cloudadata WHERE owner=?", (username,))
    result = _c.fetchall()
    _conn.commit()
    _conn.close()
    return result

def user_request(owner_username):
    _conn = db_connect()
    _c = _conn.cursor()
    _c.execute("""
        SELECT request.filename, request.data, request.owner, request.email
        FROM request
        WHERE request.owner = ?
    """, (owner_username,))
    result = _c.fetchall()
    _conn.commit()
    _conn.close()
    return result

def owner_request(fname, owner, email):
    _conn = db_connect()
    _c = _conn.cursor()
    _c.execute("SELECT skey, skey1, skey2, f1, f2, f3 FROM cloudadata WHERE owner=? AND filename=?", (owner, fname))
    result = _c.fetchall()
    _conn.commit()
    _conn.close()
    return result

def owner_update(result, fname, owner, email):
    if result:
        for skey, skey1, skey2, f1, f2, f3 in result:
            _conn = db_connect()
            _c = _conn.cursor()
            _c.execute("""
                UPDATE request
                SET status = ?, s1 = ?, s2 = ?, s3 = ?, p1 = ?, p2 = ?, p3 = ?
                WHERE filename = ? AND email = ? AND owner = ?
            """, ('yes', skey, skey1, skey2, f1, f2, f3, fname, email, owner))
            _conn.commit()
            _conn.close()
    return True

def user_viewfile(email):
    _conn = db_connect()
    _c = _conn.cursor()
    _c.execute("SELECT filename, data, owner FROM file")
    result = _c.fetchall()
    _conn.commit()
    _conn.close()
    return result

def user_viewfiledata(fname, owner, data, email):
    _conn = db_connect()
    _c = _conn.cursor()
    _c.execute("INSERT INTO request (filename, data, owner, status, email) VALUES (?, ?, ?, ?, ?)",
               (fname, data, owner, 'No', email))
    _conn.commit()
    _conn.close()
    return True

def user_down(email):
    _conn = db_connect()
    _c = _conn.cursor()
    _c.execute("SELECT filename, owner FROM request WHERE email=? AND status='yes'", (email,))
    result = _c.fetchall()
    _conn.commit()
    _conn.close()
    return result

def user_down1(email, fname):
    _conn = db_connect()
    _c = _conn.cursor()
    _c.execute("SELECT filename, owner FROM request WHERE email=? AND status='yes' AND filename=?", (email, fname))
    result = _c.fetchall()
    _conn.commit()
    _conn.close()
    return result

def verify_user(filename, dkey):
    _conn = db_connect()
    _c = _conn.cursor()
    _c.execute("SELECT filename, owner FROM cloudadata WHERE filename=? AND skey=?", (filename, dkey))
    result = _c.fetchall()
    _conn.commit()
    _conn.close()
    return result

def verify_user2(filename, dkey):
    _conn = db_connect()
    _c = _conn.cursor()
    _c.execute("SELECT filename, owner FROM cloudadata WHERE filename=? AND skey1=?", (filename, dkey))
    result = _c.fetchall()
    _conn.commit()
    _conn.close()
    return result

def user_finaldown(filename, dkey):
    _conn = db_connect()
    _c = _conn.cursor()
    _c.execute("SELECT filename, owner FROM cloudadata WHERE filename=? AND skey2=?", (filename, dkey))
    result = _c.fetchall()
    _conn.commit()
    _conn.close()
    return result

def user_lastdownload(filename, owner):
    _conn = db_connect()
    _c = _conn.cursor()
    _c.execute("SELECT skey, skey1, skey2, f1, f2, f3 FROM cloudadata WHERE owner=? AND filename=?", (owner, filename))
    result = _c.fetchall()
    _conn.commit()
    _conn.close()
    return result

if __name__ == "__main__":
    print(db_connect())