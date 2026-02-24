import sqlite3
import pandas as pd

# 1️. Connect to database
conn = sqlite3.connect("internship.db")
cursor = conn.cursor()

# 2️. Create interns table
cursor.execute("""
CREATE TABLE IF NOT EXISTS interns (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    track TEXT NOT NULL,
    stipend INTEGER NOT NULL
)
""")

# 3️. Insert sample data
intern_data = [
    (1, "Aishu", "Data Science", 15000),
    (2, "Deepu", "Web Dev", 12000),
    (3, "priya", "Data Science", 18000),
    (4, "Sai", "Cyber Security", 20000),
    (5, "Prem", "Web Dev", 14000),
    (6, "Sona", "Data Science", 4000)  # below 5000 (for filter test)
]

cursor.executemany("""
INSERT OR REPLACE INTO interns (id, name, track, stipend)
VALUES (?, ?, ?, ?)
""", intern_data)

conn.commit()

# 4️. FILTER:

query_filter = """
SELECT *
FROM interns
WHERE track = 'Data Science'
AND stipend > 5000
"""
df_filter = pd.read_sql_query(query_filter, conn)

print("\n--- Data Science Interns with Stipend > 5000 ---")
print(df_filter)

# 5️.AGGREGATE: 
query_avg = """
SELECT track, AVG(stipend) AS avg_stipend
FROM interns
GROUP BY track
"""
df_avg = pd.read_sql_query(query_avg, conn)

print("\n--- Average Stipend Per Track ---")
print(df_avg)

# 6️. COUNT: 
query_count = """
SELECT track, COUNT(*) AS intern_count
FROM interns
GROUP BY track
"""
df_count = pd.read_sql_query(query_count, conn)

print("\n--- Intern Count Per Track ---")
print(df_count)

# Close connection
conn.close()