import datetime,calendar,os
import pandas as pd
import numpy as np


def base_df(names_list, today, current_month_yr, csv_out_path):
    """ Takes Names list ; creates all columns for that month-csv """
    day, row, num_days = 1, [], calendar.monthrange(today.year, today.month)[1]

    for i in range(num_days):
        d = "0" + str(day) if len(str(day)) == 1 else str(day)  # if 1:'01'; 17:'17'
        row.append(d + "-" + current_month_yr)
        day += 1

    """ generates static df with name & day-wise column(default 0) """
    df = pd.DataFrame(0, columns=names_list, index=row)
    df.to_csv(csv_out_path, index=True)
    print("CSV created @ ", csv_out_path)
##
# base_df(names_list,today,current_month_yr,csv_out_path)


def data_entry_verifier(df, name, names_list, threshold_in_time):
    """ Takes [name] , name , today & now; to apped data """
    name = name.title()
    row = datetime.datetime.today().day - 1  # today's day as Row_id
    col = names_list.index(name) + 1  # Name index as Col_id

    # ### Entry if person in-time & no duplicate entry allowed
    if datetime.datetime.now().time() <= threshold_in_time.time():  # if now <= threshold
        if df.iloc[row, col] == "0" or df.iloc[
            row, col] == 0:  # if in-time not-there then add (no duplicate data entry)
            now = datetime.datetime.now().strftime('%H:%M:%S')
            df.iloc[row, col] = now  # Append In-time in (row,col)
            print("Added {} @ {} !!!".format(name, now))
        else:
            print("{} Already added".format(name))
    elif datetime.datetime.now().time() > threshold_in_time.time():
        print("You are late !!!")
##
# data_entry_verifier(df,"Mark",names_list,threshold_in_time)


def csv_writer(name, threshold_in_time):
    ## parameters
    directory_path = os.path.dirname(os.getcwd())

    names_list = np.load(os.path.join(directory_path,r"known_faces_database\known_face_labels.npy")).tolist()
    names_list = [i.title() for i in names_list]

    today = datetime.datetime.today()
    current_month_yr = today.strftime("%b-%Y")  # current month & year (eg- "May-2022" )
    threshold_in_time = threshold_in_time
    out_csv_name = current_month_yr + ".csv"
    csv_out_path_ = os.path.join(directory_path, r"database\master_csv")
    csv_out_path = os.path.join(csv_out_path_ ,out_csv_name)

    # print("dir_path", directory_path)
    # print("label path", os.path.join(directory_path, r"known_faces_database\known_face_labels.npy"))
    # print("dir_path", csv_out_path)

    if out_csv_name not in os.listdir(os.path.join(directory_path,r"database\master_csv")):
        base_df(names_list, today, current_month_yr, csv_out_path)  # create base structure for csv
        df = pd.read_csv(csv_out_path)
        data_entry_verifier(df, name, names_list, threshold_in_time)
        df.to_csv(csv_out_path, index=False)
    else:
        df = pd.read_csv(csv_out_path)
        data_entry_verifier(df, name, names_list, threshold_in_time)
        df.to_csv(csv_out_path, index=False)
#
#threshold_in_time = datetime.datetime.strptime("23:30:00", '%H:%M:%S')  # threshold In-time
#csv_writer('Jeff Bezos', threshold_in_time)


"D:\Projects\face attendance system\known_faces_database\known_face_encodings.npy"