import tabula-
import pandas
import openpyxl
import pdfplumber
import sqlite3

pdf_path = "/timetable.pdf"

#Extracting all the tables from the pdf
tables = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)

#Further processing the timetable table from the pdf
df_overall = tables[0]

#Seperating the tables for each weekday
df_Mon = df_overall[1:7]
df_Tue = df_overall[7:13]
df_Wed = df_overall[13:19]
df_Thu = df_overall[19:23]
df_Fri = df_overall[23:28]
df_Mon.columns = ['0','8:30','9:30','10:30','11:30','12:30','13:30','14:30','15:30','16:30','17:30','18:30']
df_Tue.columns = ['0','8:30','9:30','10:30','11:30','12:30','13:30','14:30','15:30','16:30','17:30','18:30']
df_Wed.columns = ['0','8:30','9:30','10:30','11:30','12:30','13:30','14:30','15:30','16:30','17:30','18:30']
df_Thu.columns = ['0','8:30','9:30','10:30','11:30','12:30','13:30','14:30','15:30','16:30','17:30','18:30']
df_Fri.columns = ['0','8:30','9:30','10:30','11:30','12:30','13:30','14:30','15:30','16:30','17:30','18:30']
df_Mon.drop('0',axis=1,inplace=True)
df_Tue.drop('0',axis=1,inplace=True)
df_Wed.drop('0',axis=1,inplace=True)
df_Thu.drop('0',axis=1,inplace=True)
df_Fri.drop('0',axis=1,inplace=True)

#creating the database and then a table in it
conn = sqlite3.connect("room_availability.db")
cursor = conn.cursor()

# cursor.execute("""DROP TABLE rooms_availability""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS room_availability (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        room_no TEXT(10),
        start_time TEXT(10),
        end_time TEXT(10)
    )
""")

conn.commit()
conn.close()

#inserting the entries into the table
#for Monday
conn = sqlite3.connect("room_availability.db")
cursor = conn.cursor()

for course in df_Mon['8:30']:
  if course:
    if('AC-101' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-101','8:30','9:30'))
    elif('AC-102' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-102','8:30','9:30'))
    elif('AC-103' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-103','8:30','9:30'))
    elif('AC-104' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-104','8:30','9:30'))
    elif('AC-201' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-201','8:30','9:30'))
    elif('AC-202' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-202','8:30','9:30'))
    elif('AC-203' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-203','8:30','9:30'))
    elif('AC-204' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-204','8:30','9:30'))

for course in df_Mon['10:30']:
  if course:
    if('AC-101' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-101','10:30','11:30'))
    elif('AC-102' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-102','10:30','11:30'))
    elif('AC-103' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-103','10:30','11:30'))
    elif('AC-104' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-104','10:30','11:30'))
    elif('AC-201' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-201','10:30','11:30'))
    elif('AC-202' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-202','10:30','11:30'))
    elif('AC-203' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-203','10:30','11:30'))
    elif('AC-204' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-204','10:30','11:30'))

for course in df_Mon['9:30']:
  if course:
    if('AC-101' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-101','9:30','10:30'))
    elif('AC-102' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-102','9:30','10:30'))
    elif('AC-103' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-103','9:30','10:30'))
    elif('AC-104' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-104','9:30','10:30'))
    elif('AC-201' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-201','9:30','10:30'))
    elif('AC-202' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-202','9:30','10:30'))
    elif('AC-203' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-203','9:30','10:30'))
    elif('AC-204' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-204','9:30','10:30'))

for course in df_Mon['11:30']:
  if course:
    if('AC-101' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-101','11:30','12:30'))
    elif('AC-102' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-102','11:30','12:30'))
    elif('AC-103' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-103','11:30','12:30'))
    elif('AC-104' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-104','11:30','12:30'))
    elif('AC-201' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-201','11:30','12:30'))
    elif('AC-202' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-202','11:30','12:30'))
    elif('AC-203' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-203','11:30','12:30'))
    elif('AC-204' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-204','11:30','12:30'))

for course in df_Mon['12:30']:
  if course:
    if('AC-101' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-101','12:30','12:30'))
    elif('AC-102' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-102','12:30','13:30'))
    elif('AC-103' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-103','12:30','13:30'))
    elif('AC-104' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-104','12:30','13:30'))
    elif('AC-201' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-201','12:30','13:30'))
    elif('AC-202' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-202','12:30','13:30'))
    elif('AC-203' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-203','12:30','13:30'))
    elif('AC-204' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-204','12:30','13:30'))

for course in df_Mon['13:30']:
  if course:
    if('AC-101' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-101','13:30','14:30'))
    elif('AC-102' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-102','13:30','14:30'))
    elif('AC-103' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-103','13:30','14:30'))
    elif('AC-104' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-104','13:30','14:30'))
    elif('AC-201' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-201','13:30','14:30'))
    elif('AC-202' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-202','13:30','14:30'))
    elif('AC-203' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-203','13:30','14:30'))
    elif('AC-204' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-204','13:30','14:30'))

for course in df_Mon['14:30']:
  if course:
    if('AC-101' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-101','14:30','15:30'))
    elif('AC-102' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-102','14:30','15:30'))
    elif('AC-103' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-103','14:30','15:30'))
    elif('AC-104' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-104','14:30','15:30'))
    elif('AC-201' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-201','14:30','15:30'))
    elif('AC-202' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-202','14:30','15:30'))
    elif('AC-203' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-203','14:30','15:30'))
    elif('AC-204' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-204','14:30','15:30'))

for course in df_Mon['15:30']:
  if course:
    if('AC-101' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-101','15:30','16:30'))
    elif('AC-102' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-102','15:30','16:30'))
    elif('AC-103' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-103','15:30','16:30'))
    elif('AC-104' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-104','15:30','16:30'))
    elif('AC-201' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-201','15:30','16:30'))
    elif('AC-202' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-202','15:30','16:30'))
    elif('AC-203' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-203','15:30','16:30'))
    elif('AC-204' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-204','15:30','16:30'))

for course in df_Mon['16:30']:
  if course:
    if('AC-101' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-101','16:30','17:30'))
    elif('AC-102' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-102','16:30','17:30'))
    elif('AC-103' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-103','16:30','17:30'))
    elif('AC-104' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-104','16:30','17:30'))
    elif('AC-201' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-201','16:30','17:30'))
    elif('AC-202' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-202','16:30','17:30'))
    elif('AC-203' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-203','16:30','17:30'))
    elif('AC-204' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-204','16:30','17:30'))

for course in df_Mon['17:30']:
  if course:
    if('AC-101' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-101','17:30','18:30'))
    elif('AC-102' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-102','17:30','18:30'))
    elif('AC-103' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-103','17:30','18:30'))
    elif('AC-104' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-104','17:30','18:30'))
    elif('AC-201' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-201','17:30','18:30'))
    elif('AC-202' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-202','17:30','18:30'))
    elif('AC-203' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-203','17:30','18:30'))
    elif('AC-204' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-204','17:30','18:30'))


#for Tuesday
for course in df_Tue['8:30']:
  if course:
    if('AC-101' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-101','8:30','9:30'))
    elif('AC-102' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-102','8:30','9:30'))
    elif('AC-103' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-103','8:30','9:30'))
    elif('AC-104' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-104','8:30','9:30'))
    elif('AC-201' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-201','8:30','9:30'))
    elif('AC-202' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-202','8:30','9:30'))
    elif('AC-203' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-203','8:30','9:30'))
    elif('AC-204' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-204','8:30','9:30'))

for course in df_Tue['10:30']:
  if course:
    if('AC-101' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-101','10:30','11:30'))
    elif('AC-102' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-102','10:30','11:30'))
    elif('AC-103' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-103','10:30','11:30'))
    elif('AC-104' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-104','10:30','11:30'))
    elif('AC-201' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-201','10:30','11:30'))
    elif('AC-202' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-202','10:30','11:30'))
    elif('AC-203' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-203','10:30','11:30'))
    elif('AC-204' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-204','10:30','11:30'))

for course in df_Tue['9:30']:
  if course:
    if('AC-101' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-101','9:30','10:30'))
    elif('AC-102' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-102','9:30','10:30'))
    elif('AC-103' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-103','9:30','10:30'))
    elif('AC-104' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-104','9:30','10:30'))
    elif('AC-201' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-201','9:30','10:30'))
    elif('AC-202' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-202','9:30','10:30'))
    elif('AC-203' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-203','9:30','10:30'))
    elif('AC-204' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-204','9:30','10:30'))

for course in df_Tue['11:30']:
  if course:
    if('AC-101' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-101','11:30','12:30'))
    elif('AC-102' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-102','11:30','12:30'))
    elif('AC-103' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-103','11:30','12:30'))
    elif('AC-104' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-104','11:30','12:30'))
    elif('AC-201' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-201','11:30','12:30'))
    elif('AC-202' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-202','11:30','12:30'))
    elif('AC-203' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-203','11:30','12:30'))
    elif('AC-204' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-204','11:30','12:30'))

for course in df_Tue['12:30']:
  if course:
    if('AC-101' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-101','12:30','12:30'))
    elif('AC-102' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-102','12:30','13:30'))
    elif('AC-103' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-103','12:30','13:30'))
    elif('AC-104' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-104','12:30','13:30'))
    elif('AC-201' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-201','12:30','13:30'))
    elif('AC-202' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-202','12:30','13:30'))
    elif('AC-203' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-203','12:30','13:30'))
    elif('AC-204' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-204','12:30','13:30'))

for course in df_Tue['13:30']:
  if course:
    if('AC-101' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-101','13:30','14:30'))
    elif('AC-102' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-102','13:30','14:30'))
    elif('AC-103' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-103','13:30','14:30'))
    elif('AC-104' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-104','13:30','14:30'))
    elif('AC-201' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-201','13:30','14:30'))
    elif('AC-202' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-202','13:30','14:30'))
    elif('AC-203' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-203','13:30','14:30'))
    elif('AC-204' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-204','13:30','14:30'))

for course in df_Tue['14:30']:
  if course:
    if('AC-101' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-101','14:30','15:30'))
    elif('AC-102' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-102','14:30','15:30'))
    elif('AC-103' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-103','14:30','15:30'))
    elif('AC-104' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-104','14:30','15:30'))
    elif('AC-201' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-201','14:30','15:30'))
    elif('AC-202' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-202','14:30','15:30'))
    elif('AC-203' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-203','14:30','15:30'))
    elif('AC-204' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-204','14:30','15:30'))

for course in df_Tue['15:30']:
  if course:
    if('AC-101' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-101','15:30','16:30'))
    elif('AC-102' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-102','15:30','16:30'))
    elif('AC-103' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-103','15:30','16:30'))
    elif('AC-104' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-104','15:30','16:30'))
    elif('AC-201' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-201','15:30','16:30'))
    elif('AC-202' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-202','15:30','16:30'))
    elif('AC-203' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-203','15:30','16:30'))
    elif('AC-204' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-204','15:30','16:30'))

for course in df_Tue['16:30']:
  if course:
    if('AC-101' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-101','16:30','17:30'))
    elif('AC-102' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-102','16:30','17:30'))
    elif('AC-103' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-103','16:30','17:30'))
    elif('AC-104' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-104','16:30','17:30'))
    elif('AC-201' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-201','16:30','17:30'))
    elif('AC-202' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-202','16:30','17:30'))
    elif('AC-203' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-203','16:30','17:30'))
    elif('AC-204' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-204','16:30','17:30'))

for course in df_Tue['17:30']:
  if course:
    if('AC-101' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-101','17:30','18:30'))
    elif('AC-102' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-102','17:30','18:30'))
    elif('AC-103' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-103','17:30','18:30'))
    elif('AC-104' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-104','17:30','18:30'))
    elif('AC-201' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-201','17:30','18:30'))
    elif('AC-202' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-202','17:30','18:30'))
    elif('AC-203' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-203','17:30','18:30'))
    elif('AC-204' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-204','17:30','18:30'))

#for Wednesday
for course in df_Wed['8:30']:
  if course:
    if('AC-101' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-101','8:30','9:30'))
    elif('AC-102' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-102','8:30','9:30'))
    elif('AC-103' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-103','8:30','9:30'))
    elif('AC-104' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-104','8:30','9:30'))
    elif('AC-201' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-201','8:30','9:30'))
    elif('AC-202' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-202','8:30','9:30'))
    elif('AC-203' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-203','8:30','9:30'))
    elif('AC-204' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-204','8:30','9:30'))

for course in df_Wed['10:30']:
  if course:
    if('AC-101' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-101','10:30','11:30'))
    elif('AC-102' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-102','10:30','11:30'))
    elif('AC-103' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-103','10:30','11:30'))
    elif('AC-104' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-104','10:30','11:30'))
    elif('AC-201' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-201','10:30','11:30'))
    elif('AC-202' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-202','10:30','11:30'))
    elif('AC-203' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-203','10:30','11:30'))
    elif('AC-204' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-204','10:30','11:30'))

for course in df_Wed['9:30']:
  if course:
    if('AC-101' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-101','9:30','10:30'))
    elif('AC-102' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-102','9:30','10:30'))
    elif('AC-103' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-103','9:30','10:30'))
    elif('AC-104' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-104','9:30','10:30'))
    elif('AC-201' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-201','9:30','10:30'))
    elif('AC-202' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-202','9:30','10:30'))
    elif('AC-203' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-203','9:30','10:30'))
    elif('AC-204' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-204','9:30','10:30'))

for course in df_Wed['11:30']:
  if course:
    if('AC-101' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-101','11:30','12:30'))
    elif('AC-102' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-102','11:30','12:30'))
    elif('AC-103' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-103','11:30','12:30'))
    elif('AC-104' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-104','11:30','12:30'))
    elif('AC-201' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-201','11:30','12:30'))
    elif('AC-202' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-202','11:30','12:30'))
    elif('AC-203' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-203','11:30','12:30'))
    elif('AC-204' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-204','11:30','12:30'))

for course in df_Wed['12:30']:
  if course:
    if('AC-101' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-101','12:30','12:30'))
    elif('AC-102' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-102','12:30','13:30'))
    elif('AC-103' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-103','12:30','13:30'))
    elif('AC-104' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-104','12:30','13:30'))
    elif('AC-201' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-201','12:30','13:30'))
    elif('AC-202' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-202','12:30','13:30'))
    elif('AC-203' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-203','12:30','13:30'))
    elif('AC-204' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-204','12:30','13:30'))

for course in df_Wed['13:30']:
  if course:
    if('AC-101' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-101','13:30','14:30'))
    elif('AC-102' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-102','13:30','14:30'))
    elif('AC-103' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-103','13:30','14:30'))
    elif('AC-104' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-104','13:30','14:30'))
    elif('AC-201' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-201','13:30','14:30'))
    elif('AC-202' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-202','13:30','14:30'))
    elif('AC-203' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-203','13:30','14:30'))
    elif('AC-204' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-204','13:30','14:30'))

for course in df_Wed['14:30']:
  if course:
    if('AC-101' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-101','14:30','15:30'))
    elif('AC-102' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-102','14:30','15:30'))
    elif('AC-103' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-103','14:30','15:30'))
    elif('AC-104' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-104','14:30','15:30'))
    elif('AC-201' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-201','14:30','15:30'))
    elif('AC-202' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-202','14:30','15:30'))
    elif('AC-203' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-203','14:30','15:30'))
    elif('AC-204' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-204','14:30','15:30'))

for course in df_Wed['15:30']:
  if course:
    if('AC-101' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-101','15:30','16:30'))
    elif('AC-102' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-102','15:30','16:30'))
    elif('AC-103' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-103','15:30','16:30'))
    elif('AC-104' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-104','15:30','16:30'))
    elif('AC-201' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-201','15:30','16:30'))
    elif('AC-202' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-202','15:30','16:30'))
    elif('AC-203' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-203','15:30','16:30'))
    elif('AC-204' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-204','15:30','16:30'))

for course in df_Wed['16:30']:
  if course:
    if('AC-101' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-101','16:30','17:30'))
    elif('AC-102' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-102','16:30','17:30'))
    elif('AC-103' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-103','16:30','17:30'))
    elif('AC-104' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-104','16:30','17:30'))
    elif('AC-201' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-201','16:30','17:30'))
    elif('AC-202' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-202','16:30','17:30'))
    elif('AC-203' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-203','16:30','17:30'))
    elif('AC-204' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-204','16:30','17:30'))

for course in df_Wed['17:30']:
  if course:
    if('AC-101' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-101','17:30','18:30'))
    elif('AC-102' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-102','17:30','18:30'))
    elif('AC-103' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-103','17:30','18:30'))
    elif('AC-104' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-104','17:30','18:30'))
    elif('AC-201' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-201','17:30','18:30'))
    elif('AC-202' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-202','17:30','18:30'))
    elif('AC-203' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-203','17:30','18:30'))
    elif('AC-204' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-204','17:30','18:30'))

#for Thursday
for course in df_Thu['8:30']:
  if course:
    if('AC-101' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-101','8:30','9:30'))
    elif('AC-102' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-102','8:30','9:30'))
    elif('AC-103' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-103','8:30','9:30'))
    elif('AC-104' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-104','8:30','9:30'))
    elif('AC-201' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-201','8:30','9:30'))
    elif('AC-202' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-202','8:30','9:30'))
    elif('AC-203' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-203','8:30','9:30'))
    elif('AC-204' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-204','8:30','9:30'))

for course in df_Thu['10:30']:
  if course:
    if('AC-101' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-101','10:30','11:30'))
    elif('AC-102' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-102','10:30','11:30'))
    elif('AC-103' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-103','10:30','11:30'))
    elif('AC-104' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-104','10:30','11:30'))
    elif('AC-201' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-201','10:30','11:30'))
    elif('AC-202' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-202','10:30','11:30'))
    elif('AC-203' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-203','10:30','11:30'))
    elif('AC-204' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-204','10:30','11:30'))

for course in df_Thu['9:30']:
  if course:
    if('AC-101' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-101','9:30','10:30'))
    elif('AC-102' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-102','9:30','10:30'))
    elif('AC-103' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-103','9:30','10:30'))
    elif('AC-104' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-104','9:30','10:30'))
    elif('AC-201' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-201','9:30','10:30'))
    elif('AC-202' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-202','9:30','10:30'))
    elif('AC-203' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-203','9:30','10:30'))
    elif('AC-204' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-204','9:30','10:30'))

for course in df_Thu['11:30']:
  if course:
    if('AC-101' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-101','11:30','12:30'))
    elif('AC-102' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-102','11:30','12:30'))
    elif('AC-103' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-103','11:30','12:30'))
    elif('AC-104' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-104','11:30','12:30'))
    elif('AC-201' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-201','11:30','12:30'))
    elif('AC-202' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-202','11:30','12:30'))
    elif('AC-203' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-203','11:30','12:30'))
    elif('AC-204' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-204','11:30','12:30'))

for course in df_Thu['12:30']:
  if course:
    if('AC-101' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-101','12:30','12:30'))
    elif('AC-102' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-102','12:30','13:30'))
    elif('AC-103' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-103','12:30','13:30'))
    elif('AC-104' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-104','12:30','13:30'))
    elif('AC-201' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-201','12:30','13:30'))
    elif('AC-202' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-202','12:30','13:30'))
    elif('AC-203' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-203','12:30','13:30'))
    elif('AC-204' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-204','12:30','13:30'))

for course in df_Thu['13:30']:
  if course:
    if('AC-101' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-101','13:30','14:30'))
    elif('AC-102' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-102','13:30','14:30'))
    elif('AC-103' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-103','13:30','14:30'))
    elif('AC-104' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-104','13:30','14:30'))
    elif('AC-201' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-201','13:30','14:30'))
    elif('AC-202' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-202','13:30','14:30'))
    elif('AC-203' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-203','13:30','14:30'))
    elif('AC-204' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-204','13:30','14:30'))

for course in df_Thu['14:30']:
  if course:
    if('AC-101' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-101','14:30','15:30'))
    elif('AC-102' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-102','14:30','15:30'))
    elif('AC-103' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-103','14:30','15:30'))
    elif('AC-104' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-104','14:30','15:30'))
    elif('AC-201' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-201','14:30','15:30'))
    elif('AC-202' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-202','14:30','15:30'))
    elif('AC-203' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-203','14:30','15:30'))
    elif('AC-204' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-204','14:30','15:30'))

for course in df_Thu['15:30']:
  if course:
    if('AC-101' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-101','15:30','16:30'))
    elif('AC-102' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-102','15:30','16:30'))
    elif('AC-103' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-103','15:30','16:30'))
    elif('AC-104' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-104','15:30','16:30'))
    elif('AC-201' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-201','15:30','16:30'))
    elif('AC-202' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-202','15:30','16:30'))
    elif('AC-203' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-203','15:30','16:30'))
    elif('AC-204' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-204','15:30','16:30'))

for course in df_Thu['16:30']:
  if course:
    if('AC-101' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-101','16:30','17:30'))
    elif('AC-102' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-102','16:30','17:30'))
    elif('AC-103' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-103','16:30','17:30'))
    elif('AC-104' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-104','16:30','17:30'))
    elif('AC-201' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-201','16:30','17:30'))
    elif('AC-202' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-202','16:30','17:30'))
    elif('AC-203' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-203','16:30','17:30'))
    elif('AC-204' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-204','16:30','17:30'))

for course in df_Thu['17:30']:
  if course:
    if('AC-101' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-101','17:30','18:30'))
    elif('AC-102' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-102','17:30','18:30'))
    elif('AC-103' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-103','17:30','18:30'))
    elif('AC-104' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-104','17:30','18:30'))
    elif('AC-201' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-201','17:30','18:30'))
    elif('AC-202' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-202','17:30','18:30'))
    elif('AC-203' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-203','17:30','18:30'))
    elif('AC-204' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-204','17:30','18:30'))

#For Friday
for course in df_Fri['8:30']:
  if course:
    if('AC-101' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-101','8:30','9:30'))
    elif('AC-102' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-102','8:30','9:30'))
    elif('AC-103' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-103','8:30','9:30'))
    elif('AC-104' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-104','8:30','9:30'))
    elif('AC-201' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-201','8:30','9:30'))
    elif('AC-202' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-202','8:30','9:30'))
    elif('AC-203' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-203','8:30','9:30'))
    elif('AC-204' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-204','8:30','9:30'))

for course in df_Fri['10:30']:
  if course:
    if('AC-101' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-101','10:30','11:30'))
    elif('AC-102' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-102','10:30','11:30'))
    elif('AC-103' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-103','10:30','11:30'))
    elif('AC-104' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-104','10:30','11:30'))
    elif('AC-201' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-201','10:30','11:30'))
    elif('AC-202' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-202','10:30','11:30'))
    elif('AC-203' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-203','10:30','11:30'))
    elif('AC-204' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-204','10:30','11:30'))

for course in df_Fri['9:30']:
  if course:
    if('AC-101' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-101','9:30','10:30'))
    elif('AC-102' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-102','9:30','10:30'))
    elif('AC-103' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-103','9:30','10:30'))
    elif('AC-104' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-104','9:30','10:30'))
    elif('AC-201' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-201','9:30','10:30'))
    elif('AC-202' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-202','9:30','10:30'))
    elif('AC-203' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-203','9:30','10:30'))
    elif('AC-204' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-204','9:30','10:30'))

for course in df_Fri['11:30']:
  if course:
    if('AC-101' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-101','11:30','12:30'))
    elif('AC-102' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-102','11:30','12:30'))
    elif('AC-103' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-103','11:30','12:30'))
    elif('AC-104' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-104','11:30','12:30'))
    elif('AC-201' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-201','11:30','12:30'))
    elif('AC-202' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-202','11:30','12:30'))
    elif('AC-203' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-203','11:30','12:30'))
    elif('AC-204' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-204','11:30','12:30'))

for course in df_Fri['12:30']:
  if course:
    if('AC-101' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-101','12:30','12:30'))
    elif('AC-102' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-102','12:30','13:30'))
    elif('AC-103' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-103','12:30','13:30'))
    elif('AC-104' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-104','12:30','13:30'))
    elif('AC-201' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-201','12:30','13:30'))
    elif('AC-202' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-202','12:30','13:30'))
    elif('AC-203' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-203','12:30','13:30'))
    elif('AC-204' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-204','12:30','13:30'))

for course in df_Fri['13:30']:
  if course:
    if('AC-101' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-101','13:30','14:30'))
    elif('AC-102' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-102','13:30','14:30'))
    elif('AC-103' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-103','13:30','14:30'))
    elif('AC-104' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-104','13:30','14:30'))
    elif('AC-201' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-201','13:30','14:30'))
    elif('AC-202' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-202','13:30','14:30'))
    elif('AC-203' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-203','13:30','14:30'))
    elif('AC-204' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-204','13:30','14:30'))

for course in df_Fri['14:30']:
  if course:
    if('AC-101' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-101','14:30','15:30'))
    elif('AC-102' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-102','14:30','15:30'))
    elif('AC-103' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-103','14:30','15:30'))
    elif('AC-104' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-104','14:30','15:30'))
    elif('AC-201' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-201','14:30','15:30'))
    elif('AC-202' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-202','14:30','15:30'))
    elif('AC-203' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-203','14:30','15:30'))
    elif('AC-204' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-204','14:30','15:30'))

for course in df_Fri['15:30']:
  if course:
    if('AC-101' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-101','15:30','16:30'))
    elif('AC-102' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-102','15:30','16:30'))
    elif('AC-103' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-103','15:30','16:30'))
    elif('AC-104' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-104','15:30','16:30'))
    elif('AC-201' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-201','15:30','16:30'))
    elif('AC-202' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-202','15:30','16:30'))
    elif('AC-203' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-203','15:30','16:30'))
    elif('AC-204' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-204','15:30','16:30'))

for course in df_Fri['16:30']:
  if course:
    if('AC-101' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-101','16:30','17:30'))
    elif('AC-102' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-102','16:30','17:30'))
    elif('AC-103' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-103','16:30','17:30'))
    elif('AC-104' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-104','16:30','17:30'))
    elif('AC-201' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-201','16:30','17:30'))
    elif('AC-202' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-202','16:30','17:30'))
    elif('AC-203' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-203','16:30','17:30'))
    elif('AC-204' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-204','16:30','17:30'))

for course in df_Fri['17:30']:
  if course:
    if('AC-101' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-101','17:30','18:30'))
    elif('AC-102' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-102','17:30','18:30'))
    elif('AC-103' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-103','17:30','18:30'))
    elif('AC-104' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-104','17:30','18:30'))
    elif('AC-201' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-201','17:30','18:30'))
    elif('AC-202' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-202','17:30','18:30'))
    elif('AC-203' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-203','17:30','18:30'))
    elif('AC-204' in course):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time) VALUES(?,?,?)",('AC-204','17:30','18:30'))

#displaying all the table entries
cursor.execute("""SELECT * from room_availability""")
rows = cursor.fetchall()

for row in rows:
  print(row)

conn.close()