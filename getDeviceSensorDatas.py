"""
Body 请求参数
1. {//已隐藏相关信息,请自行请求获取
2. "userId": "2******80",//用户 Id 必选参数
 "groupId":17, //设备分组条件 可选参数
3. "isDelete":0,//设备状态 0 未删除 1 已删除 2 已禁用 可选参数，默认查询所有的设备
4. "isLine":1,//设备在线状态 0 不在线，1 在线 ，可选参数，默认查询在线和不在线的数据
5. "isAlarms":"0",//设备是否报警，0 未报警，1 已报警，可选参数，默认查询报警和未报警数
据
6. "currPage":1,//当前页码，必选参数，默认 1 即第一页
7. "pageSize":10//每页返回的数据条数，可选参数,默认返回 10 条，最大设置不能超过 100 条
8. }

返回参数
1. {//已隐藏相关信息,请自行请求获取
2. "msg": "",
3. "flag": "00", //00 表示请求成功 01 表示请求失败
4. "currPage": 0, //当前页码
5. "pages": 1, //总页数
6. "pageSize": 10, //每页数据条数
7. "rowCount": 1, //数据总条数
8. "dataList": [
9. {
10. "createDate": "2019-09-24 08:49:48", //设备添加时间
11. "defaultTimescale": "60", //设备掉线延时(秒)
12. "deviceName": "modbus 设备重命名", //设备名称
13. "deviceNo": "W86********07I", //设备编号
14. "id": 20******76, //设备 Id
15. "iocUrl": "/images/device-icon/non_online-1.png", //图标
16. "isAlarms": "", //是否报警 0 或""表示未报警 1 表示报警
17. "isDelete": 1, //是否删除 0 否，1 是
18. "isLine": 0, //是否在线 0 否，1 是
19. "lat": "22.56381", //设备在地图上的纬度
20. "linktype": "modbus", //设备连接的协议
21. "lng": "114.074567", //设备在地图上的经度
22. "sensorsList": [
23. { //传感器数据
24. "decimalPlacse": "4",//小数位
25. "deviceId": 200******76,//设备 Id
26. "flag": "",
27. "heartbeatDate": null,//心跳包时间
28. "id": 20******92,//传感器 ID
29. "iocUrl": "/images/temperature.png",//传感器图标
30. "isAlarms": 0,//是否报警 0 或"" 表示未报警 1 表示报警
31. "isDelete": 1,//是否删除 0 否 ，1 是
32. "isLine": 0,//是否在线 0 否，1 是
33. "isMapping": 0,
34. "lat": "",//定位型传感器数据纬度
35. "lng": "",//定位型传感器数据经度
36. "ordernum": 0,//排序编号
37. "sensorMapping": null,
38. "sensorName": "传感器-1",//传感器名称
39. "sensorTypeId": 1,//传感器类型，1 数值型， 2/5 开关型 ，3 定位型，4 图片性，6
档位型，7 视频，8 字符串型
40. "switcher": "",/开关型传感器数据
41. "tp_flag": "",
42. "unit": "个",//数值型传感器单位
43. "updateDate": null,//数据最后的上报时间
44. "userId": 0,//用户 Id
45. "value": "",//数值 图片 档位 字符串型传感器数据
 "hls":"", //视频监控地址
"rtmp":"", //视频监控地址
"live":"", //视频直播地址
"replay":"", //视频回放地址
"accessToken":"", //视频 token
"appkey":"", //视频 key
"openysId":"", //关联视频配置 Id
"secret":"", //视频密钥
"fialtime":"" //有效时间
46. },
47. {
48. "decimalPlacse": "4",
49. "deviceId": 200****76,
50. "flag": "",
51. "heartbeatDate": null,
52. "id": 20******93,
53. "iocUrl": "/images/temperature.png",
54. "isAlarms": 0,
55. "isDelete": 1,
56. "isLine": 0,
57. "isMapping": 0,
58. "lat": "",
59. "lng": "",
60. "ordernum": 0,
61. "sensorMapping": null,
62. "sensorName": "传感器-2",
63. "sensorTypeId": 1,
64. "switcher": "",
65. "tp_flag": "",
66. "unit": "个",
67. "updateDate": null,
68. "userId": 0,
69. "value": "",
"hls":"", //视频监控地址
"rtmp":"", //视频监控地址
"live":"", //视频直播地址
"replay":"", //视频回放地址
"accessToken":"", //视频 token
"appkey":"", //视频 key
"openysId":"", //关联视频配置 Id
"secret":"", //视频密钥
"fialtime":"" //有效时间
70. }
71. ],
72. "userId": 1*****08,
73. "userName": ""
74. }
75. ]
76. }

"""

import refreshToken
import requests

token = refreshToken.getToken()
print("getToken: ", token)

url = "https://app.dtuip.com/api/device/getDeviceSensorDatas"
 
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