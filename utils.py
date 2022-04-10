import datetime as dt
import os
import csv


## variable
threshold_in_time="20:10:10"
entry= {}



def attendance_writer(name,threshold_in_time):
    """ Takes 'Id(names)' & 'entry_time' && creates attendance-dictionary
    creates CSV with today's date """

    now = dt.datetime.now().strftime('%H:%M:%S')
    name=name.title()

    if name not in entry.keys():                  # Entry possible if (in-time & non-duplicate Id)
        if now <= threshold_in_time:
            entry[name] = now
            print("Added !!!", name)

        else:
            print("You'r Late !!!")

    else:
        print("Already exists ...", name)

    return

# for i in range(15):
#     name=input("Name: ")
#     attendance_writer(name,threshold_in_time)
# print(entry)


def generate_today_csv():
    """ Creates date-wise csv file for attendance-sheet(Id,In-time) """
    path = r"database\master_csv"

    ## generate date-wise file name for csv
    date = dt.datetime.today().strftime("%Y %b %d").replace(" ", "_")    # 2022_Apr_10
    csv_out = os.path.join(path, (date + ".csv"))

    ## Generate .csv file
    with open(csv_out, 'w') as csvfile:
        csvfile.writelines(f'{"Id"},{"In_time"}')                # column name for csv : "Id", In-time
        for id_,in_time in entry.items():
            csvfile.writelines(f'\n{id_},{in_time}')
