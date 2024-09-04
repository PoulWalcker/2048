import sqlite3

bd = sqlite3.connect('2048.sql')
cursor = bd.cursor()

cursor.execute(("""
create table if not exists RECORDS (
    name text,
    score integer
)
"""))


def insert_result(name, score):
    cursor.execute("""
    INSERT into RECORDS values (
    ?,
    ?
    )""", (name, score))
    bd.commit()

def get_best():
    cursor.execute("""
    SELECT name,  max(score) as score  from RECORDS
    GROUP by name
    ORDER by score DESC
    limit 3
    """)

    return cursor.fetchall()
