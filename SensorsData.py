"""
Body 请求参数
1. {//单个传感器限（50 次/天）
2. "userId":200******80, //用户 Id
3. "sensorId":200*****372, //传感器 Id
4. "startDate":"2020-05-08 00:00:00", //开始时间
5. "endDate":"2020-05-08 00:59:59", //结束时间
6. "pagingState":"0x000a00080000125f4c1a8aeff07ffffe6ff07ffffe6f",//下一页参数 为空表示首页
7. "pageSize":100 //返回的数据条数
8. }

返回参数
1. {
2. "msg": "",
3. "unit": ".", //传感器单位
4. "flag": "00",
5. "sensorName": "传感器-1", //传感器名称
6. "nextPage": null, //下一页参数 null 表示已经到了尾页
7. "deviceName": "91TCP", //设备名称
8. "sensorTypeId": 1, //传感器类型
9. "sensorId": 200027372, //传感器 Id
10. "dataList": [
11. {
12. "addTime": "2020-05-08 00:09:57", //更新时间
13. "lat": "", //定位纬度
14. "lng": "", //定位经度
15. "switcher": "", //开关
16. "val": "1.0000" //数值
17. },
18. {
19. "addTime": "2020-05-08 00:09:47",
20. "lat": "",
21. "lng": "",
22. "switcher": "",
23. "val": "1.0000"
24. }]
25. }

"""
import pandas as pd
from pandas import Series, DataFrame
from datetime import datetime
import requests
from Token import Token

class SensorsData():
    def __init__(self, DataMap, reampleTime):
        self.dataDict = dict(DataMap)
        self.resampleTime = reampleTime

        self.token = Token().getToken()
        print("getToken: ", self.token)
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.token,
            "tlinkAppId": "721832e2e7bd42cfa6825995797cf656",
            "cache-control": "no-cache"
            }
        
        self.url = "https://app.dtuip.com/api/device/getSensorHistroy"

        self.sensor = {#已隐藏相关信息,请自行请求获取
            "userId": "73766",#用户 Id 必选参数
            "sensorId":11111, #传感器 Id,2640293是环境温度ID
            "startDate":"2022-10-07 00:01:00", #开始时间
            "endDate":"2022-10-07 01:00:00", #结束时间
            "pagingState":"",#下一页参数 为空表示首页
            "pageSize":100 #返回的数据条数
            }
    
    def getData(self, start="2022-10-07 00:01:00", end="2022-10-07 01:00:00"):
        self.sensor["startDate"] = start
        self.sensor["endDate"] = end
        for fieldName in self.dataDict.keys(): #key就是sql的filedname
            self.dataDict[fieldName] = self.getSensorJsonData(self.dataDict[fieldName]) #获取传感器历史数据Json
            #print(fieldName)
            self.dataDict[fieldName] = self.transformToDataframe(self.dataDict[fieldName],fieldName) #转换成Dataframe，保留测试时间和测量值，列名就是数据库字段名

        df = self.mergeData() #将各传感器数据拼接成一张表
        df = self.cleanData(df) #重新对齐时序、排序、重采样
        #print(df)
        return df

    def getSensorJsonData(self, sensorID):
        
        self.sensor["sensorId"] = sensorID
        self.sensor["pagingState"] = "" #取首页数据
        json_array = []
        while True:
            jsondata = requests.get(self.url, headers=self.headers, json=self.sensor).json()
            json_array = json_array + jsondata["dataList"]
            self.sensor["pagingState"] = jsondata["nextPage"] #取下页数据
            if jsondata["nextPage"] == "":  #空表示没有下页数据
                break

        return json_array

    def transformToDataframe(self, json_array, fieldName):

        store_dict = {"Sample_DateTime":[], fieldName:[]}

        for item in json_array:
            store_dict["Sample_DateTime"].append(datetime.strptime(item['addTime'], '%Y-%m-%d %H:%M:%S')) 
            store_dict[fieldName].append(item['val'])

        df = DataFrame(store_dict) 
        
        return df

    def mergeData(self): #合并各传感器数据

        df = DataFrame()
        for fieldName in self.dataDict.keys():
            if df.empty :
                df = self.dataDict[fieldName]
            else:
                df = pd.merge(df, self.dataDict[fieldName],on='Sample_DateTime')
        return df

    def cleanData(self, df): #数据清洗一遍

        df["DateTime"] = df["Sample_DateTime"] #保留采样时间以便对比时间   #.round('1min') #采样数据的时间不一定正好是整分钟，人为取整时间，规则为取距离最近。
        
        df = df.set_index('DateTime').sort_index()  #API数据为时间倒序，这里重排过来

        df = df.resample(self.resampleTime, closed='right', label='right').ffill()  #按给定时间间隔重采样数据
        print(df)

        return df