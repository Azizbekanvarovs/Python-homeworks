import sqlite3

conn = sqlite3.connect("roster.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS Roster")
cur.execute("""
CREATE TABLE Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
""")

cur.executemany("""
INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)
""", [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
])

cur.execute("UPDATE Roster SET Name = 'Ezri Dax' WHERE Name = 'Jadzia Dax'")

print("Bajoran Characters:")
for row in cur.execute("SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'"):
    print(row)

cur.execute("DELETE FROM Roster WHERE Age > 100")

cur.execute("ALTER TABLE Roster ADD COLUMN Rank TEXT")

cur.execute("UPDATE Roster SET Rank = 'Captain' WHERE Name = 'Benjamin Sisko'")
cur.execute("UPDATE Roster SET Rank = 'Lieutenant' WHERE Name = 'Ezri Dax'")
cur.execute("UPDATE Roster SET Rank = 'Major' WHERE Name = 'Kira Nerys'")

print("\nCharacters by Age (Descending):")
for row in cur.execute("SELECT * FROM Roster ORDER BY Age DESC"):
    print(row)

conn.commit()
conn.close()