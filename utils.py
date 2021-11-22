import datetime as dt
import pandas as pd

thre_time=dt.time(1,44)  # threshold in time   (User Input)
attendance=[]
names=[]

def attendance_writer(name):
    """ Takes name & append,returns dictionary of Id_names,entry_time,attendance_status """
    name=str.title(name)  # converts all name to title-format (ex: Abhijit Sutar)
    if (name not in names)==False:
        print("Id:'{}'  Already Exists....".format(name))
    else:
        names.append(name)
        entry_time=dt.datetime.now().time()
        if (entry_time < thre_time):  # True if in-time
            attendance.append([name,entry_time.strftime('%I:%M:%S %p'),"In-time"])
            print("Id:'{}'  Added Successfuly....".format(name))
        else:
            attendance.append([name,entry_time.strftime('%I:%M:%S %p'),"Late"])
            print("Id:'{}'  Added Successfuly....".format(name))
    return attendance



def write_dataframe(attendance):
    """ Takes List of Attendance-data & convert to pandas-dataframe"""
    df=pd.DataFrame(attendance,columns=["Name","In-Time","Attendance-Status"])
    print("DataFrame Created Successfully ....")
    return df