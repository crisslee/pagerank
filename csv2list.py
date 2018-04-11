import csv
import json

result =[]
csvFile = open("D:\\NLP\weibo.csv", 'r', encoding='utf8')

reader = csv.reader(csvFile)

for item in reader:
    result.append(item[0])
csvFile.close()

init_r = result[0]
result_dict = {}
count = 0
for i in result:
    if i != init_r:
        result_dict[init_r] = count
        count = 0
        init_r = i
    count += 1
result_dict = sorted(result_dict.items(), key = lambda item:item[1])
print(result_dict)
jsonoj = json.dumps(result_dict)
fileoj = open('final.json', 'w')
fileoj.write(jsonoj)
fileoj.close()
