import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect("internship.db")
cursor = conn.cursor()

# Create interns table
cursor.execute("""
CREATE TABLE IF NOT EXISTS interns (
    id INTEGER PRIMARY KEY,
    name TEXT,
    track TEXT,
    stipend INTEGER
)
""")

# Create mentors table
cursor.execute("""
CREATE TABLE IF NOT EXISTS mentors (
    mentor_id INTEGER PRIMARY KEY,
    mentor_name TEXT,
    track TEXT
)
""")

# Insert interns
intern_data = [
    (1, "Ankit", "Data Science", 15000),
    (2, "Megha", "Web Dev", 12000),
    (3, "Sai", "Data Science", 18000),
    (4, "Priya", "Cyber Security", 20000),
    (5, "Ethan", "Web Dev", 14000)
]

cursor.executemany("""
INSERT OR REPLACE INTO interns VALUES (?, ?, ?, ?)
""", intern_data)

# Insert mentors
mentor_data = [
    (1, "Dr. Smith", "Data Science"),
    (2, "Ms. Johnson", "Web Dev"),
    (3, "Mr. Lee", "Cyber Security")
]

cursor.executemany("""
INSERT OR REPLACE INTO mentors VALUES (?, ?, ?)
""", mentor_data)

conn.commit()

# INNER JOIN query
query = """
SELECT interns.name, interns.track, mentors.mentor_name
FROM interns
INNER JOIN mentors
ON interns.track = mentors.track
"""

df = pd.read_sql_query(query, conn)

print(df)

conn.close()