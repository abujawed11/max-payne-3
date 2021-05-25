import sqlite3
new = sqlite3.connect('schooltest.db')
cur = new.cursor()
cur.execute("ALTER TABLE student ADD USN int")
new.commit()
