import os
import streamlit as st
from generate import generate,load_image



def app():
    head = st.container()

    with head:
        st.title("Generate Known Database")

    # Upload Image:
        st.subheader("Upload Image")
        col1, col2, col3 = st.columns(3)
        with col1:
            image_file = st.file_uploader("Upload Images", type=["png", "jpg", "jpeg"])
            if image_file is not None:
                st.image(load_image(image_file), width=250)
        with col3:
                name = st.text_input("Add Name")

        if st.button('Add'):
            with open(os.path.join(r"D:\Projects\face attendance system\Input_images",name+".jpg"),"wb") as f:
                f.write(image_file.getbuffer())
            st.success("Added Successfully")

    # Generate Known Database
        st.subheader("Generate Known-Database")

        if st.button('Generate'):
            generate(r"Input_images")
            st.success("Generated Successfully")
