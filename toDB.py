
import MySQLdb
from sqlalchemy import create_engine

import pandas as pd
from pandas import Series, DataFrame

import getFieldMap
from SensorsData import SensorsData

def getDataTime():
    from datetime import datetime, timedelta

    last_hour_date_time = datetime.now() - timedelta(hours = 1)
    start = last_hour_date_time.replace(minute=0, second=0, microsecond=0)
    end = start + timedelta(hours = 1)
    return start.strftime('%Y-%m-%d %H:%M:%S'), end.strftime('%Y-%m-%d %H:%M:%S')

engine = create_engine('mysql+mysqldb://root:Ss_123456789@sh-cynosdbmysql-grp-ci7pxc9i.sql.tencentcdb.com:22257/SolarGenenator')

#db = MySQLdb.connect(host="sh-cynosdbmysql-grp-ci7pxc9i.sql.tencentcdb.com",port=22257,user="root",password="Ss_123456789",database="SolarGenenator")
#cursor = db.cursor()
#tableName = "Meteorological"

dataDict = getFieldMap.getFieldMap() #该字典用于保存dataframe形式的数据,FieldMap构建了数据库字段和传感器ID之间的关系，通过传感器ID从塔石云API中获取字段的数据

startTime, endTime = getDataTime()
df = SensorsData(dataDict,'5min').getData(start=startTime, end=endTime)

df.to_sql('Meteorological', engine, if_exists="append", index=False)