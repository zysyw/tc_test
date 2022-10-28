
import sys
import MySQLdb

db = MySQLdb.connect(host="sh-cynosdbmysql-grp-ci7pxc9i.sql.tencentcdb.com",port=22257,user="root",password="Ss_123456789",database="SolarGenenator")


# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# 使用execute方法执行SQL语句
cursor.execute("SELECT * FROM Meteorological")

# 使用 fetchone() 方法获取一条数据
data = cursor.fetchone()

print(data)

# 关闭数据库连接
db.close()

def add_row(cursor, tablename, rowdict):
    # XXX tablename not sanitized
    # XXX test for allowed keys is case-sensitive

    # filter out keys that are not column names
    cursor.execute("describe %s" % tablename)
    allowed_keys = set(row[0] for row in cursor.fetchall())
    keys = allowed_keys.intersection(rowdict)

    if len(rowdict) > len(keys):
        unknown_keys = set(rowdict) - allowed_keys
        print >> sys.stderr, "skipping keys:", ", ".join(unknown_keys)

    columns = ", ".join(keys)
    values_template = ", ".join(["%s"] * len(keys))

    sql = "insert into %s (%s) values (%s)" % (
        tablename, columns, values_template)
    values = tuple(rowdict[key] for key in keys)
    cursor.execute(sql, values)
