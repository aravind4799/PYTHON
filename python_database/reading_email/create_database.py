import sqlite3

conn = sqlite3.connect("org_db.sqlite")
cur=conn.cursor()

cur.execute("DROP TABLE IF EXISTS Counts")

cur.execute("CREATE TABLE Counts (org TEXT,count INTERGER)")

fh=open("mbox.txt")

for line in fh:
    if not line.startswith("From:"):continue
    words=line.split()
    org=words[1].split("@")[1]
    cur.execute("SELECT count from Counts WHERE org= ?",(org,))
    row=cur.fetchone()
    if row is None:
        cur.execute("INSERT INTO Counts(org,count) VALUES(?,1)",(org,))
    else:
        cur.execute("UPDATE Counts SET count= count+1 WHERE org=?",(org,))
conn.commit()

sqlstr="SELECT * FROM Counts ORDER BY count DESC LIMIT 10"
for row in cur.execute(sqlstr):
    print(str(row[0]),row[1])
