from mysql.connector import connect

con = connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='********'
)

print(type(con))

con.close()