import os, re
import pandas as pd
import numpy as np

## months list
def get_month_wise_csv_list():
    """ Takes File path & returns month_wise_csv_list of specific format """
    month_wise_csv_list,month_list = [],[]
    for file in os.listdir(r"D:\Projects\face attendance system\Backend\database\master_csv"):  # \*.csv
        if file.endswith(".csv") and re.match('[Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec]{3}[-]\d{4}',file):  # find only 'mmm-yyyy' format (i.e 'May-2022.csv')
            month_wise_csv_list.append(file)
            month_list.append(file.split("-")[0])
    return month_wise_csv_list,month_list
##
#month_wise_csv_list,month_list = get_month_wise_csv_list()
#print(month_wise_csv_list,month_list)


## date-wise all persons attendance
def get_day_wise_df(start_date, end_date):
    """ Takes start-date & end-date returns df(all persons attendance during that date-range) """
    csv_path = r"D:\Projects\face attendance system\Backend\database\master_csv"
    csv_name = start_date[3:] + ".csv"

    if csv_name in os.listdir(csv_path):  # If setected CSV exists
        df_day_wise = pd.read_csv(os.path.join(csv_path, csv_name))
        df_day_wise.set_index("Unnamed: 0", inplace=True)

        if (start_date in df_day_wise.index) and (end_date in df_day_wise.index) and int(start_date[:2]) < int(end_date[:2]): ## check for correct range of start & end date ; start-date < end-date
            df_month_wise = df_day_wise.loc[start_date:end_date, :]
            return df_month_wise
        elif (start_date in df_day_wise.index) and (end_date in df_day_wise.index) and int(start_date[:2]) == int(end_date[:2]): ## check for correct range of start & end date ; start-date == end-date
            df_day_wise = df_day_wise.loc[start_date]
            return df_day_wise
        elif (start_date not in df_day_wise.index) or (end_date not in df_day_wise.index) or int(start_date[:2]) > int(end_date[:2]):
            return "Select Start-date & End-date correctly"

    elif start_date[3:] + ".csv" not in os.listdir(csv_path):
        return "No Data Found"
##
# start_date,end_date="02-May-2022","12-May-2022"
# df=get_day_wise_df(start_date,end_date)
# df



def get_names_list():
    """ Returns all available names as a list """
    names_list = np.load(os.path.join(r"D:\Projects\face attendance system\Backend\known_faces_database\known_face_labels.npy")).tolist()
    return [i.title() for i in names_list]
##
#names_list=get_names_list()
#print(names_list)


def get_day_name_wise_df(start_date,end_date,name):
    """ Takes start-date & end-date & [names] returns df(selected persons attendance during that date-range) """
    csv_path = r"D:\Projects\face attendance system\Backend\database\master_csv"
    csv_name = start_date[3:] + ".csv"

    if csv_name in os.listdir(csv_path):  # If setected CSV exists
        df_day_wise = pd.read_csv(os.path.join(csv_path, csv_name))
        df_day_wise.set_index("Unnamed: 0", inplace=True)

        if (start_date in df_day_wise.index) and (end_date in df_day_wise.index) and int(start_date[:2]) < int(end_date[:2]) and len(name)>0: ## check for correct range of start & end date ; start-date < end-date
            df_month_wise = df_day_wise.loc[start_date:end_date,name]
            return df_month_wise
        elif (start_date in df_day_wise.index) and (end_date in df_day_wise.index) and int(start_date[:2]) == int(end_date[:2]) and len(name)>0: ## check for correct range of start & end date ; start-date == end-date
            df_day_wise = df_day_wise.loc[start_date,name]
            return df_day_wise
        elif (start_date not in df_day_wise.index) or (end_date not in df_day_wise.index) or int(start_date[:2]) > int(end_date[:2]):
            return "Select Start-date & End-date correctly"
        elif (start_date not in df_day_wise.index) or (end_date not in df_day_wise.index) or int(start_date[:2]) > int(end_date[:2]) or len(name)==0:
            return "Select Start-date & End-date correctly with Name "

    elif start_date[3:] + ".csv" not in os.listdir(csv_path):
        return "No Data Found"
##
# names=['Abdul Kalam', 'Barack Obama', 'Elon Musk', 'Guido Van Rossum']
# start,end="12-May-2022","15-May-2022"
# get_day_name_wise_df(start_date,end_date,names)


def get_img(name):
    """ Takes a known-name of person & returns image path of that known-person """
    path=r"D:\Projects\face attendance system\Input_images"

    for img in os.listdir(path):
        if name==img.split(".")[0].title():
            return os.path.join(path,img)
##
# img_path=get_img("Abdul Kalam")
# img_path

