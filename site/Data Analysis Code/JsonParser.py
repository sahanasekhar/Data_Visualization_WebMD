__author__ = 'Rakesh'


import json
from pprint import pprint

fileLoc='C:/Users/Rakesh/Desktop/webmd-dataset/'
'''
with open(fileLoc+'new_webmd-question.json') as data_file:
    data = json.load(data_file)
'''
#pprint(data)

def readfile(param):
    with open(fileLoc+param) as f:
        yield f
    pass



for f in readfile("new-webmd-answer.json"):
    answer_data = json.load(f, strict=False)

for f in readfile("new_webmd-question.json"):
    question_data = json.load(f, strict=False)

for f in readfile("new_webmd-topics.json"):
    topics_data = json.load(f, strict=False)


for f in readfile("new-webmd-member.json"):
    members_data = json.load(f, strict=False)
#print(members_data)
q_Dict={};

for d in question_data:
    q_Dict[d['questionId']]= d
t_Dict={};
for d in topics_data:
    t_Dict[d['topicId']]= d
m_dict={}
for d in members_data:
    if d['memberName'] is not None:
        d['memberName']=d['memberName'].split(",")[0]
    else:
        d['memberName']=d['memberId']
    m_dict[d['memberId']]= d

a_dict=[]
for d in answer_data:
    d.update(q_Dict[d['questionId']])
    #print(d["answerMemberId"])
    if(d["answerMemberId"] in m_dict):
        d.update(m_dict[d["answerMemberId"]])
    #qTopic=q_Dict[d['questionTopicId']]
    #print(qTopic)
    #print(t_Dict[['questionTopicId']])
    #d.update(t_Dict[])
    a_dict.append(d)
print(a_dict[0].keys())

with open(fileLoc+"mainData.json", "w") as jsonFile:
    jsonFile.write(json.dumps(a_dict))

'''
for d in a_dict:
    pprint(d)


with open(fileLoc+"new_webmd-topics.json") as f:
    answer_data = json.load(f, strict=False)
q_Dict={}
for d in answer_data:
    q_Dict[d['topicId']]= d

#pprint(q_Dict)
answer_data2=[]
for d in answer_data:
    d['some']=q_Dict[d['topicId']]
    answer_data2.append(q_Dict[d['topicId']])

for d in answer_data2:
    pprint(d)
'''



