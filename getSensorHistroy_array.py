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

import refreshToken
import requests
import json

token = refreshToken.getToken()
print("getToken: ", token)

url = "https://app.dtuip.com/api/device/getSensorHistroy"
 
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + token,
    "tlinkAppId": "721832e2e7bd42cfa6825995797cf656",
    "cache-control": "no-cache"
    }

 
data = {#已隐藏相关信息,请自行请求获取
    "userId": "73766",#用户 Id 必选参数
    "sensorId":"2640293", #传感器 Id,2640293是环境温度ID
    "startDate":"2022-10-07 00:00:00", #开始时间
    "endDate":"2022-10-07 00:59:59", #结束时间
    "pagingState":"",#下一页参数 为空表示首页
    "pageSize":100 #返回的数据条数
    }
 
response = requests.get(url, headers=headers, json=data)

json_array = response.json()["dataList"]
#print("json_array: ", json_array)

store_list = []

for item in json_array:
    store_details = {"addTime":None, "val":None}
    store_details['addTime'] = item['addTime']
    store_details['val'] = item['val']
    store_list.append(store_details)

print("store_list: ", store_list)
 
#print("Status Code ", response.status_code)
#print("JSON Response ", response.json())