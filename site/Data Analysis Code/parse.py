import json
from pprint import pprint
import csv
import re
import string

with open('new_webmd-question1.json') as data_file:
    data = json.load(data_file, strict=False)

resultFile = open('returns.csv', 'wb')
wr = csv.writer(resultFile, dialect='excel')    

print(len(data))
for d in data:

	string1 = d["questionTopicId"]
	string3 = d["questionPostDate"]
	#print(string3)
	date = str(string3)
	if(',' in date):
		new_date = date.replace("\n", "")
		all = string.maketrans('','')
		nodigs = all.translate(all, string.digits)
		intermediate = new_date.translate(all, nodigs)
		final = int(intermediate) % 10000
		final_date = final
	else:
		match = re.search('\d{4}',date)
		if(match):
			final_date = match.group()
		else:
			pass	

	#date_final = date.replace(',','')
	if(d["questionTopicId"] == ""):
		pass 

	elif(',' in d["questionTopicId"]):
		#print d["questionTopicId"]
		#print d["questionPostDate"]
		string2 = string1.split(',')
		for i in string2:
			d = str(i)
			f = d.replace("\r\n","")
			topic = []
			topic.append(f)
			topic.append(final_date)
			wr.writerow(topic)
	else:
		original = []
		original.append(string1)
		original.append(final_date)
		wr.writerow(original)		
					
	

				


		
		


  



