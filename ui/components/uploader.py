import streamlit as st
import os

def upload_image():
    uploaded_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

    if uploaded_file:
        image_path = f"data/images/{uploaded_file.name}"

        os.makedirs("data/images", exist_ok=True)

        with open(image_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.image(image_path, caption="Uploaded Image", width=300)

        return image_path

    return None