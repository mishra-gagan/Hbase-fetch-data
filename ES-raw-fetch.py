from happybase import Connection
from msgpack import loads
import subprocess

conn = Connection('cdh-3')



tables = conn.tables()

for my_table in tables:
        if "eflow" in my_table:
                subprocess.call("curl cdh-2:9200/%s/_search?pretty" %my_table, shell = True)

table = conn.table('ad_log_2018_07_03')
row = table.row(b'0c471853f2900000000001e848033e0000002cfef6b')
#for key, values in loads(row["c:d"]).items():
#       print key, values
