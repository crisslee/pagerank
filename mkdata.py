import json

with open('final.json', 'r') as f:
    result_dict = json.load(f)
result_dict = dict(result_dict)
#过滤掉微博数小于50的人
A_level_user = {}
B_level_user = {}
C_level_user = {}
D_level_user = {}
#A级用户为微博数大于1000的人，为他们每人分配？？？-？？？个用户
#B级用户为微博数在700-1000的人，为他们每人分配？？？-？？？个用户
#C级用户为微博数在300-700的人，为他们每人分配？？？-？？？个用户
#D级用户为微博数在50-300的人，为他们每人分配？？？-？？？个用户
#微博数量小于50的人会被过滤掉


