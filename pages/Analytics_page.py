import os
import streamlit as st
import pandas as pd
from Backend.Analytics import get_month_wise_csv_list,get_day_wise_df,get_names_list,get_day_name_wise_df

def app():
    head = st.container()

    with head:
        st.title("Analytics")

        day_wise_analytics=st.container()
        with day_wise_analytics:
            st.subheader("Day-Wise Analytics")
            month_wise_csv_list, month_list = get_month_wise_csv_list()    # return available month-list
            day_list=["1","2","3","4","5","6","7","8","9","10","11","12"]  # return available day-list
            year_list=["2020","2021","2022"]                               # return available year-list

            col1, col2, col3 ,col4= st.columns(4)
            with col1:
                year = st.selectbox("Select A Year : ", year_list)
            with col2:
                month = st.selectbox("Select A Month : ", month_list)
            with col3:
                day_start=st.selectbox("Select A Start-Date : ",day_list)
                day_start = "0" + day_start if len(day_start) == 1 else day_start  # if 1:'01'; 17:'17'
            with col4:
                day_end = st.selectbox("Select A End-Date : ", day_list)
                day_end = "0" + day_end if len(day_end) == 1 else day_end

            start_row = day_start+"-"+month+"-"+year    # start-date for month_wise_analytics
            end_row = day_end+"-"+month+"-"+year        # end-date for month_wise_analytics
            if st.button('Show Day-Wise Analytics Dataframe'):
                day_wise_df = get_day_wise_df(start_row,end_row)
                if isinstance(day_wise_df,pd.DataFrame): # checks if it's df or string
                    st.dataframe(day_wise_df)
                else:
                    st.warning(day_wise_df)



        ## Name wise filters
        name_wise_analytics = st.container()
        with name_wise_analytics:
            st.subheader("Name-Wise Analytics")
            name_list_1 = get_names_list()
            month_wise_csv_list_1, month_list_1 = get_month_wise_csv_list()  # return available month-list
            day_list_1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]  # return available day-list
            year_list_1 = ["2020", "2021", "2022"]  # return available year-list


            col11,col12,col13,col14,col15=st.columns(5)
            with col11:
                year_1 = st.selectbox("Select Year : ", year_list_1)
            with col12:
                month_1 = st.selectbox("Select Month : ", month_list_1)
            with col13:
                day_start_1 = st.selectbox("Select Start-Date : ", day_list_1)
                day_start_1 = "0" + day_start_1 if len(day_start_1) == 1 else day_start_1  # if 1:'01'; 17:'17'
            with col14:
                day_end_1 = st.selectbox("Select End-Date : ", day_list_1)
                day_end_1 = "0" + day_end_1 if len(day_end_1) == 1 else day_end_1
            with col15:
                names_1 = st.multiselect("Select Names : ", name_list_1)

            start_row_1 = day_start_1 + "-" + month_1 + "-" + year_1  # start-date for month_wise_analytics
            end_row_1 = day_end_1 + "-" + month_1 + "-" + year_1  # end-date for month_wise_analytics
            if st.button('Show Name-Wise Analytics Dataframe'):
                day_name_wise_df = get_day_name_wise_df(start_row_1, end_row_1,names_1)
                if isinstance(day_name_wise_df, pd.DataFrame):  # checks if it's df or string
                    st.dataframe(day_name_wise_df)
                else:
                    st.warning(day_name_wise_df)