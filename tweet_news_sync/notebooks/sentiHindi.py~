import json,string,io,codecs
model={}
model2={}
with io.open("HSWN_WN.txt",encoding="utf-8") as f:
	content = f.readlines()

for line in content:
	words = line.split()
	pscore=float(words[2])
	nscore=float(words[3])
	synonyms=words[4].split(',')
	#print synonyms
	for eachWord in synonyms:
		if eachWord not in model:
			check=abs(pscore-nscore)
			if check>=0.1:	#can change
				if pscore>nscore:
					tag=1	
				else:
					tag=-1
			else:
				tag=0
			model[eachWord]=tag

with codecs.open("sentiment_model.txt","w","utf-8") as f:
	json.dump(model,f)


