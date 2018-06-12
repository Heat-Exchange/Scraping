from time import sleep
from modules import XMLprocess
from modules import get_url
import sqlite3


class get_FFRate:
    #アクセスマップの入ったファイルを指定
    def __init__(self,path,filename,index):
        #アクセスするurlのリストを取得
        __scr=get_url.site_map(path,filename)
        self.urlList=__scr.get_url(index)
    #日付取得用の関数
    def get_date(self):   
        __XML=XMLprocess(self.urlList[0])
        __strdate=__XML.get_cutedData("dc:date",0,10)
        __XML=None
        return __strdate
    
    def get_rate(self,url):
        __XML=XMLprocess(url)
        __rate=__XML.get_floatData("cb:value")
        __XML=None
        return __rate
    #urlのリストに基づいてデータを取得していく
    def get_list(self):
        rateList=[]
        #日付をリストに入れる(主キーのつもり)
        rateList.append(self.get_date())

        for __url in self.urlList:
            __rate=self.get_rate(__url)
            rateList.append(__rate)
            #1秒間待つ
            sleep(1)
        __XML=None
        return rateList
a=get_url.site_map("target","siteMap.json")
b=a.get_index()
print(b)
for idx in b:
    #今後の発展性を持たせるためのテスト
    ff=get_FFRate("target","siteMap.json",idx)

print(ff.get_list())

"""
Namelist=["FF","M01","M03","M06","Y01","Y02","Y03","Y05","Y10","Y20","Y30"]
rateList=[]
rateList.append(get_date(url))
for Namelist in Namelist:
    rateList.append(float(get_rate(url1,url2,Namelist)))
    sleep(0.01)
print(rateList)
"""