import csv
import time
import mysql.connector

conn = mysql.connector.connect(user='root', database='weibo')
cursor = conn.cursor()

f = open("partial.csv")
f_csv = csv.reader(f)
fails = []
for ind, row in enumerate(f_csv):
    try:
        cursor.execute('insert into content (user_id, reposts_count, comment_count, resource, create_at, text) values (%s, %s, %s, %s, %s, %s)', [row[0], row[1], row[2], row[3], row[4], row[5]])
    except Exception as e:
        print(e)
        fails.append(row)

print(fails)
conn.commit()
cursor.close()
conn.close()
f.close()

