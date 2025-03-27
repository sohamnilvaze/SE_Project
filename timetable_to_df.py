import pandas as pd
import tabula-py
import openpyxl
import pdfplumber

pdf_path = "/timetable.pdf"
tables = []

#Extracting all the tables from the pdf
with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        extracted_table = page.extract_table()
        if extracted_table:
            tables.append(pd.DataFrame(extracted_table))

#only the first table is useful
df_overall = tables[0]

#correcting the weekday names
for i in range(len(df_overall[0])):
  if df_overall[0][i]:
    if 'M' in df_overall[0][i]:
      df_overall[0][i] = 'Monday'
    elif 'T' in df_overall[0][i] and 'e' in df_overall[0][i]:
      df_overall[0][i] = 'Tuesday'
    elif 'W' in df_overall[0][i]:
      df_overall[0][i] = 'Wednesday'
    elif 'T' in df_overall[0][i] and 'h' in df_overall[0][i]:
      df_overall[0][i] = 'Thursday'
    elif 'F' in df_overall[0][i]:
      df_overall[0][i] = 'Friday'

#Correcting all the entries in days column
days_srno = []
for i in range(len(df_overall[0])):
  if df_overall[0][i]:
    if( 'Monday' in df_overall[0][i]):
      days_srno.append(i)
    if( 'Tuesday' in df_overall[0][i]):
      days_srno.append(i)
    if( 'Wednesday' in df_overall[0][i]):
      days_srno.append(i)
    if( 'Thursday' in df_overall[0][i]):
      days_srno.append(i)
    if( 'Friday' in df_overall[0][i]):
      days_srno.append(i)
print(days_srno)

for i in range(days_srno[0],days_srno[1]):
  df_overall[0][i] = 'Monday'

for i in range(days_srno[1],days_srno[2]):
  df_overall[0][i] = 'Tuesday'

for i in range(days_srno[2],days_srno[3]):
  df_overall[0][i] = 'Wednesday'

for i in range(days_srno[3],days_srno[4]):
  df_overall[0][i] = 'Thursday'

for i in range(days_srno[4],len(df_overall[0])):
  df_overall[0][i] = 'Friday'

df_overall.columns = [0,'8:30','9:30','10:30','11:30','12:30','13:30','14:30','15:30','16:30','17:30','18:30']

#creating the database
import sqlite3

conn = sqlite3.connect("room_availability_ac.db")
cursor = conn.cursor()

# cursor.execute("""DROP TABLE acFloor1""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS acFloor1 (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        day TEXT(10),
        time_slot TEXT(10)
        r101 TEXT(10),
        r102 TEXT(10),
        r103 TEXT(10),
        r104 TEXT(10)
    )
""")

cursor.execute("""DROP TABLE acFloor2""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS acFloor2 (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        day TEXT(10),
        time_slot TEXT(10)
        r201 TEXT(10),
        r202 TEXT(10),
        r203 TEXT(10),
        r204 TEXT(10)
    )
""")

conn.commit()
conn.close()

#inserting the extracted data from the timetable pdf into the database
conn = sqlite3.connect("room_availability_ac.db")
cursor = conn.cursor()

for i in range(len(df_overall[0])):
  if df_overall['8:30'][i]:
    if('AC-101' in df_overall['8:30'][i]):
      cursor.execute("INSERT INTO acFloor1(day,time_slot,r101,r102,r103,r104) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'8am-9am','Occupied','Vacant','Vacant','Vacant'))
    elif('AC-102' in df_overall['8:30'][i]):
      cursor.execute("INSERT INTO acFloor1(day,time_slot,r101,r102,r103,r104) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'8am-9am','Vacant','Occupied','Vacant','Vacant'))
    elif('AC-103' in df_overall['8:30'][i]):
      cursor.execute("INSERT INTO acFloor1(day,time_slot,r101,r102,r103,r104) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'8am-9am','Vacant','Vacant','Occupied','Vacant'))
    elif('AC-104' in df_overall['8:30'][i]):
      cursor.execute("INSERT INTO acFloor1(day,time_slot,r101,r102,r103,r104) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'8am-9am','Vacant','Vacant','Vacant','Occupied'))
    elif('AC-201' in df_overall['8:30'][i]):
      cursor.execute("INSERT INTO acFloor2(day,time_slot,r201,r202,r203,r204) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'8am-9am','Occupied','Vacant','Vacant','Vacant'))
    elif('AC-202' in df_overall['8:30'][i]):
      cursor.execute("INSERT INTO acFloor2(day,time_slot,r201,r202,r203,r204) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'8am-9am','Vacant','Occupied','Vacant','Vacant'))
    elif('AC-203' in df_overall['8:30'][i]):
      cursor.execute("INSERT INTO acFloor2(day,time_slot,r201,r202,r203,r204) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'8am-9am','Vacant','Vacant','Occupied','Vacant'))
    elif('AC-204' in df_overall['8:30'][i]):
      cursor.execute("INSERT INTO acFloor2(day,time_slot,r201,r202,r203,r204) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'8am-9am','Vacant','Vacant','Vacant','Occupied'))

for i in range(len(df_overall[0])):
  if df_overall['9:30'][i]:
    if('AC-101' in df_overall['9:30'][i]):
      cursor.execute("INSERT INTO acFloor1(day,time_slot,r101,r102,r103,r104) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'9am-10am','Occupied','Vacant','Vacant','Vacant'))
    elif('AC-102' in df_overall['9:30'][i]):
      cursor.execute("INSERT INTO acFloor1(day,time_slot,r101,r102,r103,r104) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'9am-10am','Vacant','Occupied','Vacant','Vacant'))
    elif('AC-103' in df_overall['9:30'][i]):
      cursor.execute("INSERT INTO acFloor1(day,time_slot,r101,r102,r103,r104) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'9am-10am','Vacant','Vacant','Occupied','Vacant'))
    elif('AC-104' in df_overall['9:30'][i]):
      cursor.execute("INSERT INTO acFloor1(day,time_slot,r101,r102,r103,r104) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'9am-10am','Vacant','Vacant','Vacant','Occupied'))
    elif('AC-201' in df_overall['9:30'][i]):
      cursor.execute("INSERT INTO acFloor2(day,time_slot,r201,r202,r203,r204) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'9am-10am','Occupied','Vacant','Vacant','Vacant'))
    elif('AC-202' in df_overall['9:30'][i]):
      cursor.execute("INSERT INTO acFloor2(day,time_slot,r201,r202,r203,r204) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'9am-10am','Vacant','Occupied','Vacant','Vacant'))
    elif('AC-203' in df_overall['9:30'][i]):
      cursor.execute("INSERT INTO acFloor2(day,time_slot,r201,r202,r203,r204) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'9am-10am','Vacant','Vacant','Occupied','Vacant'))
    elif('AC-204' in df_overall['9:30'][i]):
      cursor.execute("INSERT INTO acFloor2(day,time_slot,r201,r202,r203,r204) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'9am-10am','Vacant','Vacant','Vacant','Occupied'))

for i in range(len(df_overall[0])):
  if df_overall['10:30'][i]:
    if('AC-101' in df_overall['10:30'][i]):
      cursor.execute("INSERT INTO acFloor1(day,time_slot,r101,r102,r103,r104) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'10am-11am','Occupied','Vacant','Vacant','Vacant'))
    elif('AC-102' in df_overall['10:30'][i]):
      cursor.execute("INSERT INTO acFloor1(day,time_slot,r101,r102,r103,r104) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'10am-11am','Vacant','Occupied','Vacant','Vacant'))
    elif('AC-103' in df_overall['10:30'][i]):
      cursor.execute("INSERT INTO acFloor1(day,time_slot,r101,r102,r103,r104) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'10am-1am','Vacant','Vacant','Occupied','Vacant'))
    elif('AC-104' in df_overall['10:30'][i]):
      cursor.execute("INSERT INTO acFloor1(day,time_slot,r101,r102,r103,r104) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'10am-11am','Vacant','Vacant','Vacant','Occupied'))
    elif('AC-201' in df_overall['10:30'][i]):
      cursor.execute("INSERT INTO acFloor2(day,time_slot,r201,r202,r203,r204) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'10am-11am','Occupied','Vacant','Vacant','Vacant'))
    elif('AC-202' in df_overall['10:30'][i]):
      cursor.execute("INSERT INTO acFloor2(day,time_slot,r201,r202,r203,r204) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'10am-11am','Vacant','Occupied','Vacant','Vacant'))
    elif('AC-203' in df_overall['10:30'][i]):
      cursor.execute("INSERT INTO acFloor2(day,time_slot,r201,r202,r203,r204) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'10am-1am','Vacant','Vacant','Occupied','Vacant'))
    elif('AC-204' in df_overall['10:30'][i]):
      cursor.execute("INSERT INTO acFloor2(day,time_slot,r201,r202,r203,r204) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'10am-11am','Vacant','Vacant','Vacant','Occupied'))

for i in range(len(df_overall[0])):
  if df_overall['11:30'][i]:
    if('AC-101' in df_overall['11:30'][i]):
      cursor.execute("INSERT INTO acFloor1(day,time_slot,r101,r102,r103,r104) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'11am-12pm','Occupied','Vacant','Vacant','Vacant'))
    elif('AC-102' in df_overall['11:30'][i]):
      cursor.execute("INSERT INTO acFloor1(day,time_slot,r101,r102,r103,r104) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'11am-12pm','Vacant','Occupied','Vacant','Vacant'))
    elif('AC-103' in df_overall['11:30'][i]):
      cursor.execute("INSERT INTO acFloor1(day,time_slot,r101,r102,r103,r104) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'11am-12pm','Vacant','Vacant','Occupied','Vacant'))
    elif('AC-104' in df_overall['11:30'][i]):
      cursor.execute("INSERT INTO acFloor1(day,time_slot,r101,r102,r103,r104) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'11am-12pm','Vacant','Vacant','Vacant','Occupied'))
    elif('AC-201' in df_overall['11:30'][i]):
      cursor.execute("INSERT INTO acFloor2(day,time_slot,r201,r202,r203,r204) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'11am-12pm','Occupied','Vacant','Vacant','Vacant'))
    elif('AC-202' in df_overall['11:30'][i]):
      cursor.execute("INSERT INTO acFloor2(day,time_slot,r201,r202,r203,r204) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'11am-12pm','Vacant','Occupied','Vacant','Vacant'))
    elif('AC-203' in df_overall['11:30'][i]):
      cursor.execute("INSERT INTO acFloor2(day,time_slot,r201,r202,r203,r204) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'11am-12pm','Vacant','Vacant','Occupied','Vacant'))
    elif('AC-204' in df_overall['11:30'][i]):
      cursor.execute("INSERT INTO acFloor2(day,time_slot,r201,r202,r203,r204) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'11am-12pm','Vacant','Vacant','Vacant','Occupied'))

for i in range(len(df_overall[0])):
  if df_overall['12:30'][i]:
    if('AC-101' in df_overall['12:30'][i]):
      cursor.execute("INSERT INTO acFloor1(day,time_slot,r101,r102,r103,r104) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'12pm-1pm','Occupied','Vacant','Vacant','Vacant'))
    elif('AC-102' in df_overall['12:30'][i]):
      cursor.execute("INSERT INTO acFloor1(day,time_slot,r101,r102,r103,r104) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'12pm-1pm','Vacant','Occupied','Vacant','Vacant'))
    elif('AC-103' in df_overall['12:30'][i]):
      cursor.execute("INSERT INTO acFloor1(day,time_slot,r101,r102,r103,r104) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'12pm-1pm','Vacant','Vacant','Occupied','Vacant'))
    elif('AC-104' in df_overall['12:30'][i]):
      cursor.execute("INSERT INTO acFloor1(day,time_slot,r101,r102,r103,r104) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'12pm-1pm','Vacant','Vacant','Vacant','Occupied'))
    elif('AC-201' in df_overall['12:30'][i]):
      cursor.execute("INSERT INTO acFloor2(day,time_slot,r201,r202,r203,r204) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'12pm-1pm','Occupied','Vacant','Vacant','Vacant'))
    elif('AC-202' in df_overall['12:30'][i]):
      cursor.execute("INSERT INTO acFloor2(day,time_slot,r201,r202,r203,r204) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'12pm-1pm','Vacant','Occupied','Vacant','Vacant'))
    elif('AC-203' in df_overall['12:30'][i]):
      cursor.execute("INSERT INTO acFloor2(day,time_slot,r201,r202,r203,r204) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'12pm-1pm','Vacant','Vacant','Occupied','Vacant'))
    elif('AC-204' in df_overall['12:30'][i]):
      cursor.execute("INSERT INTO acFloor2(day,time_slot,r201,r202,r203,r204) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'12pm-1pm','Vacant','Vacant','Vacant','Occupied'))

for i in range(len(df_overall[0])):
  if df_overall['13:30'][i]:
    if('AC-101' in df_overall['13:30'][i]):
      cursor.execute("INSERT INTO acFloor1(day,time_slot,r101,r102,r103,r104) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'1pm-2pm','Occupied','Vacant','Vacant','Vacant'))
    elif('AC-102' in df_overall['13:30'][i]):
      cursor.execute("INSERT INTO acFloor1(day,time_slot,r101,r102,r103,r104) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'1pm-2pm','Vacant','Occupied','Vacant','Vacant'))
    elif('AC-103' in df_overall['13:30'][i]):
      cursor.execute("INSERT INTO acFloor1(day,time_slot,r101,r102,r103,r104) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'1pm-2pm','Vacant','Vacant','Occupied','Vacant'))
    elif('AC-104' in df_overall['13:30'][i]):
      cursor.execute("INSERT INTO acFloor1(day,time_slot,r101,r102,r103,r104) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'1pm-2pm','Vacant','Vacant','Vacant','Occupied'))
    elif('AC-201' in df_overall['13:30'][i]):
      cursor.execute("INSERT INTO acFloor2(day,time_slot,r201,r202,r203,r204) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'1pm-2pm','Occupied','Vacant','Vacant','Vacant'))
    elif('AC-202' in df_overall['13:30'][i]):
      cursor.execute("INSERT INTO acFloor2(day,time_slot,r201,r202,r203,r204) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'1pm-2pm','Vacant','Occupied','Vacant','Vacant'))
    elif('AC-203' in df_overall['13:30'][i]):
      cursor.execute("INSERT INTO acFloor2(day,time_slot,r201,r202,r203,r204) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'1pm-2pm','Vacant','Vacant','Occupied','Vacant'))
    elif('AC-204' in df_overall['13:30'][i]):
      cursor.execute("INSERT INTO acFloor2(day,time_slot,r201,r202,r203,r204) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'1pm-2pm','Vacant','Vacant','Vacant','Occupied'))

for i in range(len(df_overall[0])):
  if df_overall['14:30'][i]:
    if('AC-101' in df_overall['14:30'][i]):
      cursor.execute("INSERT INTO acFloor1(day,time_slot,r101,r102,r103,r104) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'2pm-3pm','Occupied','Vacant','Vacant','Vacant'))
    elif('AC-102' in df_overall['14:30'][i]):
      cursor.execute("INSERT INTO acFloor1(day,time_slot,r101,r102,r103,r104) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'2pm-3pm','Vacant','Occupied','Vacant','Vacant'))
    elif('AC-103' in df_overall['14:30'][i]):
      cursor.execute("INSERT INTO acFloor1(day,time_slot,r101,r102,r103,r104) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'2pm-3pm','Vacant','Vacant','Occupied','Vacant'))
    elif('AC-104' in df_overall['14:30'][i]):
      cursor.execute("INSERT INTO acFloor1(day,time_slot,r101,r102,r103,r104) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'2pm-3pm','Vacant','Vacant','Vacant','Occupied'))
    elif('AC-201' in df_overall['14:30'][i]):
      cursor.execute("INSERT INTO acFloor2(day,time_slot,r201,r202,r203,r204) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'2pm-3pm','Occupied','Vacant','Vacant','Vacant'))
    elif('AC-202' in df_overall['14:30'][i]):
      cursor.execute("INSERT INTO acFloor2(day,time_slot,r201,r202,r203,r204) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'2pm-3pm','Vacant','Occupied','Vacant','Vacant'))
    elif('AC-203' in df_overall['14:30'][i]):
      cursor.execute("INSERT INTO acFloor2(day,time_slot,r201,r202,r203,r204) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'2pm-3pm','Vacant','Vacant','Occupied','Vacant'))
    elif('AC-204' in df_overall['14:30'][i]):
      cursor.execute("INSERT INTO acFloor2(day,time_slot,r201,r202,r203,r204) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'2pm-3pm','Vacant','Vacant','Vacant','Occupied'))

for i in range(len(df_overall[0])):
  if df_overall['15:30'][i]:
    if('AC-101' in df_overall['15:30'][i]):
      cursor.execute("INSERT INTO acFloor1(day,time_slot,r101,r102,r103,r104) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'3pm-4pm','Occupied','Vacant','Vacant','Vacant'))
    elif('AC-102' in df_overall['15:30'][i]):
      cursor.execute("INSERT INTO acFloor1(day,time_slot,r101,r102,r103,r104) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'3pm-4pm','Vacant','Occupied','Vacant','Vacant'))
    elif('AC-103' in df_overall['15:30'][i]):
      cursor.execute("INSERT INTO acFloor1(day,time_slot,r101,r102,r103,r104) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'3pm-4pm','Vacant','Vacant','Occupied','Vacant'))
    elif('AC-104' in df_overall['15:30'][i]):
      cursor.execute("INSERT INTO acFloor1(day,time_slot,r101,r102,r103,r104) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'3pm-4pm','Vacant','Vacant','Vacant','Occupied'))
    elif('AC-201' in df_overall['15:30'][i]):
      cursor.execute("INSERT INTO acFloor2(day,time_slot,r201,r202,r203,r204) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'3pm-4pm','Occupied','Vacant','Vacant','Vacant'))
    elif('AC-202' in df_overall['15:30'][i]):
      cursor.execute("INSERT INTO acFloor2(day,time_slot,r201,r202,r203,r204) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'3pm-4pm','Vacant','Occupied','Vacant','Vacant'))
    elif('AC-203' in df_overall['15:30'][i]):
      cursor.execute("INSERT INTO acFloor2(day,time_slot,r201,r202,r203,r204) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'3pm-4pm','Vacant','Vacant','Occupied','Vacant'))
    elif('AC-204' in df_overall['15:30'][i]):
      cursor.execute("INSERT INTO acFloor2(day,time_slot,r201,r202,r203,r204) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'3pm-4pm','Vacant','Vacant','Vacant','Occupied'))

for i in range(len(df_overall[0])):
  if df_overall['16:30'][i]:
    if('AC-101' in df_overall['16:30'][i]):
      cursor.execute("INSERT INTO acFloor1(day,time_slot,r101,r102,r103,r104) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'4pm-5pm','Occupied','Vacant','Vacant','Vacant'))
    elif('AC-102' in df_overall['16:30'][i]):
      cursor.execute("INSERT INTO acFloor1(day,time_slot,r101,r102,r103,r104) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'4pm-5pm','Vacant','Occupied','Vacant','Vacant'))
    elif('AC-103' in df_overall['16:30'][i]):
      cursor.execute("INSERT INTO acFloor1(day,time_slot,r101,r102,r103,r104) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'4pm-5pm','Vacant','Vacant','Occupied','Vacant'))
    elif('AC-104' in df_overall['16:30'][i]):
      cursor.execute("INSERT INTO acFloor1(day,time_slot,r101,r102,r103,r104) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'4pm-5pm','Vacant','Vacant','Vacant','Occupied'))
    elif('AC-201' in df_overall['16:30'][i]):
      cursor.execute("INSERT INTO acFloor2(day,time_slot,r201,r202,r203,r204) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'4pm-5pm','Occupied','Vacant','Vacant','Vacant'))
    elif('AC-202' in df_overall['16:30'][i]):
      cursor.execute("INSERT INTO acFloor2(day,time_slot,r201,r202,r203,r204) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'4pm-5pm','Vacant','Occupied','Vacant','Vacant'))
    elif('AC-203' in df_overall['16:30'][i]):
      cursor.execute("INSERT INTO acFloor2(day,time_slot,r201,r202,r203,r204) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'4pm-5pm','Vacant','Vacant','Occupied','Vacant'))
    elif('AC-204' in df_overall['16:30'][i]):
      cursor.execute("INSERT INTO acFloor2(day,time_slot,r201,r202,r203,r204) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'4pm-5pm','Vacant','Vacant','Vacant','Occupied'))


for i in range(len(df_overall[0])):
  if df_overall['17:30'][i]:
    if('AC-101' in df_overall['17:30'][i]):
      cursor.execute("INSERT INTO acFloor1(day,time_slot,r101,r102,r103,r104) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'5pm-6pm','Occupied','Vacant','Vacant','Vacant'))
    elif('AC-102' in df_overall['17:30'][i]):
      cursor.execute("INSERT INTO acFloor1(day,time_slot,r101,r102,r103,r104) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'5pm-6pm','Vacant','Occupied','Vacant','Vacant'))
    elif('AC-103' in df_overall['17:30'][i]):
      cursor.execute("INSERT INTO acFloor1(day,time_slot,r101,r102,r103,r104) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'5pm-6pm','Vacant','Vacant','Occupied','Vacant'))
    elif('AC-104' in df_overall['17:30'][i]):
      cursor.execute("INSERT INTO acFloor1(day,time_slot,r101,r102,r103,r104) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'5pm-6pm','Vacant','Vacant','Vacant','Occupied'))
    elif('AC-201' in df_overall['17:30'][i]):
      cursor.execute("INSERT INTO acFloor2(day,time_slot,r201,r202,r203,r204) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'5pm-6pm','Occupied','Vacant','Vacant','Vacant'))
    elif('AC-202' in df_overall['17:30'][i]):
      cursor.execute("INSERT INTO acFloor2(day,time_slot,r201,r202,r203,r204) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'5pm-6pm','Vacant','Occupied','Vacant','Vacant'))
    elif('AC-203' in df_overall['17:30'][i]):
      cursor.execute("INSERT INTO acFloor2(day,time_slot,r201,r202,r203,r204) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'5pm-6pm','Vacant','Vacant','Occupied','Vacant'))
    elif('AC-204' in df_overall['17:30'][i]):
      cursor.execute("INSERT INTO acFloor2(day,time_slot,r201,r202,r203,r204) VALUES(?,?,?,?,?,?)",(df_overall[0][i],'5pm-6pm','Vacant','Vacant','Vacant','Occupied'))

#printing all the data from the database acFloor1
cursor.execute("""SELECT * from acFloor1""")
rows = cursor.fetchall()

for row in rows:
  print(row)

#printing all the data from the database acFloor2
cursor.execute("""SELECT * from acFloor2""")
rows = cursor.fetchall()

for row in rows:
  print(row)

conn.close()
            
            