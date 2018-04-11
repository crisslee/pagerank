import csv
import json
csvFile = open("D:\\NLP\weibo.csv", 'r', encoding='utf8')
reader = csv.reader(csvFile)

result = []
for item in reader:
    result.append(item[0])
csvFile.close()
result_set = set(result)


fileoj = open('result.json', 'w')
for ip in result_set:
    fileoj.write(ip)
    fileoj.write('\n')
fileoj.close()