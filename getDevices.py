"""
Body 请求参数
1. {//已隐藏相关信息,请自行请求获取
2. "userId": "20******080",//用户 Id 必选参数
3. "groupId":17, //设备分组条件 可选参数
4. "isDelete":0,//设备状态 0 未删除 1 已删除 2 已禁用 可选参数，默认查询所有的设备
5. "isLine":1,//设备在线状态 0 不在线，1 在线 ，可选参数，默认查询在线和不在线的数据
6. "isAlarms":"0",//设备是否报警，0 未报警，1 已报警，可选参数，默认查询报警和未报警数据
7. "currPage":1,//当前页码，必选参数，默认 1 即第一页
8. "pageSize":10//每页返回的数据条数，可选参数,默认返回 10 条，最大设置不能超过 100 条
9. }

返回参数
1. {//已隐藏相关信息,请自行请求获取
2. "msg": "",
3. "flag": "00", //00 表示请求成功 01 表示请求失败
4. "currPage": 0,//当前页
5. "pages": 2,//总页数
6. "pageSize": 10,//返回的数据条数
7. "rowCount": 11,//总记录数
8. "dataList": [
9. {
10. "createDate": "2017-04-25 22:58:39",//添加时间
11. "defaultTimescale": "300",//掉线延时单位（秒）
12. "deviceName": "39TCP",//设备名称
13. "deviceNo": "VQ5V******ZBWC",//编号
14. "id": 200******85,//id
15. "iocUrl": "/images/device-icon/non_online-2.png",//图标
16. "isAlarms": "",//是否报警 0 和 “”表示未报警，1 报警
17. "isDelete": 0,//是否已删除 0 否 1 是
18. "isLine": 1,//是否在线 0 否 1 是
19. "lat": "22.431759",//设备在地图上的纬度
20. "linktype": "tcp",//协议类型
21. "lng": "113.644051",//设备在地图上的经度
22. "userId": 20******80,//用户 Id
23. "userName": "test" //用户名称
24. },
25. {
26. "createDate": "2017-04-25 23:00:11",
27. "defaultTimescale": "300",
28. "deviceName": "39MBRTU",
29. "deviceNo": "6G3Z******0Y98",
30. "id": 200******86,
31. "iocUrl": "/images/device-icon/non_online-20.png",
32. "isAlarms": "",
33. "isDelete": 0,
34. "isLine": 1,
35. "lat": "22.626998",
36. "linktype": "modbus",
37. "lng": "114.008333",
38. "userId": 20******80,
39. "userName": "test"
40. }
41. ]
42. }

"""

import refreshToken
import requests

token = refreshToken.getToken()
print("getToken: ", token)

url = "https://app.dtuip.com/api/device/getDevices"
 
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + token,
    "tlinkAppId": "721832e2e7bd42cfa6825995797cf656",
    "cache-control": "no-cache"
    }

 
data = {#已隐藏相关信息,请自行请求获取
    "userId": "73766",#用户 Id 必选参数
    "groupId":40125, #设备分组条件 可选参数
    "isDelete":0,#设备状态 0 未删除 1 已删除 2 已禁用 可选参数，默认查询所有的设备
    #"isLine":1,#设备在线状态 0 不在线，1 在线 ，可选参数，默认查询在线和不在线的数据
    #"isAlarms":"0",#设备是否报警，0 未报警，1 已报警，可选参数，默认查询报警和未报警数据
    "currPage":1,#当前页码，必选参数，默认 1 即第一页
    "pageSize":10#每页返回的数据条数，可选参数,默认返回 10 条，最大设置不能超过 100 条
    }
 
response = requests.get(url, headers=headers, json=data)
 
print("Status Code", response.status_code)
print("JSON Response ", response.json())