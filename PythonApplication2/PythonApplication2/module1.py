import os
import json

name=os.path.dirname(os.path.abspath(__name__)) 
path=name+'/target/' +"FFRate.json"
abspath=os.path.normpath(path)

f = open(abspath, 'r')

jsonData=json.load(f)
prefix=jsonData["static"]["prefix"]
suffix=jsonData["static"]["suffix"]

cmb="combination"
indexList = jsonData[cmb].keys()
indexList=list(indexList)
print(indexList)
urlList=[]
for index in indexList:
    text=jsonData[cmb][index]
    part=text+index
    urlList.append(prefix+part+suffix)
f.close
print(urlList)


