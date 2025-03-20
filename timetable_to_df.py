import pandas
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

conn = sqlite3.connect("room_availability.db")
cursor = conn.cursor()

# cursor.execute("""DROP TABLE room_availability""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS room_availability (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        room_no TEXT(10),
        start_time TEXT(10),
        end_time TEXT(10),
        day TEXT(10)
    )
""")

conn.commit()
conn.close()

#inserting the extracted data from the timetable pdf into the database
conn = sqlite3.connect("room_availability.db")
cursor = conn.cursor()

for i in range(len(df_overall[0])):
  if df_overall['8:30'][i]:
    if('AC-101' in df_overall['8:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-101','8:30','9:30',df_overall[0][i]))
    elif('AC-102' in df_overall['8:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-102','8:30','9:30',df_overall[0][i]))
    elif('AC-103' in df_overall['8:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-103','8:30','9:30',df_overall[0][i]))
    elif('AC-104' in df_overall['8:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-104','8:30','9:30',df_overall[0][i]))
    elif('AC-201' in df_overall['8:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-201','8:30','9:30',df_overall[0][i]))
    elif('AC-202' in df_overall['8:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-202','8:30','9:30',df_overall[0][i]))
    elif('AC-203' in df_overall['8:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-203','8:30','9:30',df_overall[0][i]))
    elif('AC-204' in df_overall['8:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-204','8:30','9:30',df_overall[0][i]))
  
for i in range(len(df_overall[0])):
  if df_overall['9:30'][i]:
    if('AC-101' in df_overall['9:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-101','9:30','10:30',df_overall[0][i]))
    elif('AC-102' in df_overall['9:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-102','9:30','10:30',df_overall[0][i]))
    elif('AC-103' in df_overall['9:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-103','9:30','10:30',df_overall[0][i]))
    elif('AC-104' in df_overall['9:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-104','9:30','10:30',df_overall[0][i]))
    elif('AC-201' in df_overall['9:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-201','9:30','10:30',df_overall[0][i]))
    elif('AC-202' in df_overall['9:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-202','9:30','10:30',df_overall[0][i]))
    elif('AC-203' in df_overall['9:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-203','9:30','10:30',df_overall[0][i]))
    elif('AC-204' in df_overall['9:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-204','9:30','10:30',df_overall[0][i]))

for i in range(len(df_overall[0])):
  if df_overall['10:30'][i]:
    if('AC-101' in df_overall['10:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-101','10:30','11:30',df_overall[0][i]))
    elif('AC-102' in df_overall['10:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-102','10:30','11:30',df_overall[0][i]))
    elif('AC-103' in df_overall['10:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-103','10:30','11:30',df_overall[0][i]))
    elif('AC-104' in df_overall['10:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-104','10:30','11:30',df_overall[0][i]))
    elif('AC-201' in df_overall['10:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-201','10:30','11:30',df_overall[0][i]))
    elif('AC-202' in df_overall['10:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-202','10:30','11:30',df_overall[0][i]))
    elif('AC-203' in df_overall['10:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-203','10:30','11:30',df_overall[0][i]))
    elif('AC-204' in df_overall['10:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-204','10:30','11:30',df_overall[0][i]))

for i in range(len(df_overall[0])):
  if df_overall['11:30'][i]:
    if('AC-101' in df_overall['11:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-101','11:30','12:30',df_overall[0][i]))
    elif('AC-102' in df_overall['11:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-102','11:30','12:30',df_overall[0][i]))
    elif('AC-103' in df_overall['11:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-103','11:30','12:30',df_overall[0][i]))
    elif('AC-104' in df_overall['11:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-104','11:30','12:30',df_overall[0][i]))
    elif('AC-201' in df_overall['11:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-201','11:30','12:30',df_overall[0][i]))
    elif('AC-202' in df_overall['11:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-202','11:30','12:30',df_overall[0][i]))
    elif('AC-203' in df_overall['11:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-203','11:30','12:30',df_overall[0][i]))
    elif('AC-204' in df_overall['11:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-204','11:30','12:30',df_overall[0][i]))

for i in range(len(df_overall[0])):
  if df_overall['12:30'][i]:
    if('AC-101' in df_overall['12:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-101','12:30','13:30',df_overall[0][i]))
    elif('AC-102' in df_overall['12:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-102','12:30','13:30',df_overall[0][i]))
    elif('AC-103' in df_overall['12:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-103','12:30','13:30',df_overall[0][i]))
    elif('AC-104' in df_overall['12:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-104','12:30','13:30',df_overall[0][i]))
    elif('AC-201' in df_overall['12:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-201','12:30','13:30',df_overall[0][i]))
    elif('AC-202' in df_overall['12:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-202','12:30','13:30',df_overall[0][i]))
    elif('AC-203' in df_overall['12:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-203','12:30','13:30',df_overall[0][i]))
    elif('AC-204' in df_overall['12:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-204','12:30','13:30',df_overall[0][i]))

for i in range(len(df_overall[0])):
  if df_overall['13:30'][i]:
    if('AC-101' in df_overall['13:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-101','13:30','14:30',df_overall[0][i]))
    elif('AC-102' in df_overall['13:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-102','13:30','14:30',df_overall[0][i]))
    elif('AC-103' in df_overall['13:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-103','13:30','14:30',df_overall[0][i]))
    elif('AC-104' in df_overall['13:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-104','13:30','14:30',df_overall[0][i]))
    elif('AC-201' in df_overall['13:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-201','13:30','14:30',df_overall[0][i]))
    elif('AC-202' in df_overall['13:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-202','13:30','14:30',df_overall[0][i]))
    elif('AC-203' in df_overall['13:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-203','13:30','14:30',df_overall[0][i]))
    elif('AC-204' in df_overall['13:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-204','13:30','14:30',df_overall[0][i]))

for i in range(len(df_overall[0])):
  if df_overall['14:30'][i]:
    if('AC-101' in df_overall['14:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-101','14:30','15:30',df_overall[0][i]))
    elif('AC-102' in df_overall['14:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-102','14:30','15:30',df_overall[0][i]))
    elif('AC-103' in df_overall['14:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-103','14:30','15:30',df_overall[0][i]))
    elif('AC-104' in df_overall['14:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-104','14:30','15:30',df_overall[0][i]))
    elif('AC-201' in df_overall['14:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-201','14:30','15:30',df_overall[0][i]))
    elif('AC-202' in df_overall['14:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-202','14:30','15:30',df_overall[0][i]))
    elif('AC-203' in df_overall['14:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-203','14:30','15:30',df_overall[0][i]))
    elif('AC-204' in df_overall['14:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-204','14:30','15:30',df_overall[0][i]))

for i in range(len(df_overall[0])):
  if df_overall['15:30'][i]:
    if('AC-101' in df_overall['15:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-101','15:30','16:30',df_overall[0][i]))
    elif('AC-102' in df_overall['15:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-102','15:30','16:30',df_overall[0][i]))
    elif('AC-103' in df_overall['15:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-103','15:30','16:30',df_overall[0][i]))
    elif('AC-104' in df_overall['15:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-104','15:30','16:30',df_overall[0][i]))
    elif('AC-201' in df_overall['15:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-201','15:30','16:30',df_overall[0][i]))
    elif('AC-202' in df_overall['15:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-202','15:30','16:30',df_overall[0][i]))
    elif('AC-203' in df_overall['15:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-203','15:30','16:30',df_overall[0][i]))
    elif('AC-204' in df_overall['15:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-204','15:30','16:30',df_overall[0][i]))

for i in range(len(df_overall[0])):
  if df_overall['16:30'][i]:
    if('AC-101' in df_overall['16:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-101','16:30','17:30',df_overall[0][i]))
    elif('AC-102' in df_overall['16:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-102','16:30','17:30',df_overall[0][i]))
    elif('AC-103' in df_overall['16:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-103','16:30','17:30',df_overall[0][i]))
    elif('AC-104' in df_overall['16:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-104','16:30','17:30',df_overall[0][i]))
    elif('AC-201' in df_overall['16:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-201','16:30','17:30',df_overall[0][i]))
    elif('AC-202' in df_overall['16:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-202','16:30','17:30',df_overall[0][i]))
    elif('AC-203' in df_overall['16:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-203','16:30','17:30',df_overall[0][i]))
    elif('AC-204' in df_overall['16:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-204','16:30','17:30',df_overall[0][i]))

for i in range(len(df_overall[0])):
  if df_overall['17:30'][i]:
    if('AC-101' in df_overall['17:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-101','17:30','18:30',df_overall[0][i]))
    elif('AC-102' in df_overall['17:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-102','17:30','18:30',df_overall[0][i]))
    elif('AC-103' in df_overall['17:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-103','17:30','18:30',df_overall[0][i]))
    elif('AC-104' in df_overall['17:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-104','17:30','18:30',df_overall[0][i]))
    elif('AC-201' in df_overall['17:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-201','17:30','18:30',df_overall[0][i]))
    elif('AC-202' in df_overall['17:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-202','17:30','18:30',df_overall[0][i]))
    elif('AC-203' in df_overall['17:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-203','17:30','18:30',df_overall[0][i]))
    elif('AC-204' in df_overall['17:30'][i]):
      cursor.execute("INSERT INTO room_availability(room_no,start_time,end_time,day) VALUES(?,?,?,?)",('AC-204','17:30','18:30',df_overall[0][i]))

#printing all the data from the database
cursor.execute("""SELECT * from room_availability""")
rows = cursor.fetchall()

for row in rows:
  print(row)

conn.close()
            
            
