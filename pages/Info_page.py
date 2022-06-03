import os
from PIL import Image
import streamlit as st
from Backend.Analytics import get_month_wise_csv_list,get_day_wise_df,get_names_list,get_img

def app():
    head = st.container()

    with head:
        st.title("Individual Information")

        info = st.container()
        with info:
            name_list= get_names_list()
            selected_name= st.selectbox("Select End-Date : ", name_list)

            if st.button('Show Details'):
                st.subheader("Information of {}".format(selected_name))
                img_path=get_img(selected_name)
                image = Image.open(img_path)
                st.image(image,caption=selected_name)

            ####
