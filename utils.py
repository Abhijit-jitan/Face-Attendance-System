import datetime as dt
import pandas as pd
import os
import csv

attendance=[]
names=[]

columns = ["Name", "In-Time", "Attendance-Status"]
date=dt.datetime.today()
date_=date.strftime("%d %b %y").replace(" ","_")   # '20_Dec_21'
csv_name=date_+".csv"

file_name=os.path.join("csv_sheet",csv_name)

def attendance_writer(name,thre_time):
    """ Takes name & "Id_names,entry_time,attendance_status" Append to CSV  """
    name=str.title(name)  # converts all name to title-format (ex: Abhijit Sutar)
    if (name not in names)==False:
        print("Id:'{}'  Already Exists....".format(name))
    else:
        names.append(name)
        entry_time=dt.datetime.now().time()
        if (entry_time < thre_time):  # True if in-time
            print("Id:'{}'  Added Successfuly....".format(name))
            with open(file_name, "a", newline='') as f:
                writer = csv.writer(f, delimiter=',')
                writer.writerow([name,entry_time.strftime('%I:%M:%S %p'),"In-time"])

        else:
            print("Id:'{}'  Added Successfuly....".format(name))
            with open(file_name, "a", newline='') as f:
                writer = csv.writer(f, delimiter=',')
                writer.writerow([name,entry_time.strftime('%I:%M:%S %p'),"Late"])

    return

