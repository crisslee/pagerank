import json
import mysql.connector
#result = []
#with open('result.json', 'r') as f:
    #for line in f.readlines():
        #result.append(json.loads(line))
#print(result)
db = mysql.connector.connect(user='root', database='weibo')
#print(db)
#result = [1, 2, 3, 4]

cursor = db.cursor()

sql = "SELECT user_id FROM content"
#print(sql)
cursor.execute(sql)
data = cursor.fetchone()
db.close()
result_dict = {}
init_r = data[0]
count = 0
for i in data:
    if init_r != i:
        result_dict[init_r] = count
        count = 0
        init_r = i
    count += 1
result_dict = sorted(result_dict.items(), key=lambda item:item[1])
jsonoj = json.dumps(result_dict)
fileoj = open('final.json', 'w')
fileoj.write(jsonoj)
fileoj.close()
#print(data)
#db.close()


