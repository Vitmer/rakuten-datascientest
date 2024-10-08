import streamlit as st
import pandas as pd
from PIL import Image

img_Rakuten_challenge = Image.open("Images/1_Introduction/Rakuten_challenge.png")
img_ecommerce = Image.open("Images/1_Introduction/ecommerce.jpg")
# URL you want to link to
url = "https://challengedata.ens.fr/challenges/35"

def app():
    st.title("1. Description of the project:")

    st.write(
        """
        <p style="font-size: 25px;">
        E-commerce has revolutionized business and 
        shopping, with retail sales soaring from $1.336 
        billion in 2014 to $5.311 billion in 2022. 
        Effective product cataloging is vital for 
        personalized marketing, inventory management, 
        and improved user experiences. Given the vast 
        number of products, automatic classification 
        models are essential. 
        </p>
        """,
        unsafe_allow_html=True
    )

    st.image(img_ecommerce)

    st.write(
        """
        <p style="font-size: 25px;">
        This project uses a 
        dataset from Rakuten France to predict product 
        categories from textual titles, descriptions, 
        images, and type codes. It evaluates various 
        Machine and Deep Learning models for accuracy, 
        including data inspection, preprocessing, and 
        model comparisons, concluding with insights 
        on business and scientific impacts.
        </p>
        """,
        unsafe_allow_html=True
    )

    # st.write(
    #     """
    #     <p style="font-size: 25px;">
    #     Cataloging products according to different data (texts and images) 
    #     is important for e-commerce since it allows for various applications 
    #     such as product recommendation and personalized research. It is then 
    #     a question of predicting the type code of the products knowing textual 
    #     data (designation and description of the products) as well as image data 
    #     (image of the product).
    #     </p>
    #     """,
    #     unsafe_allow_html=True
    # )

    
    
    with st.container():
        text_column, image_column = st.columns((3.6,2))
        with text_column:
            st.header("Resources to refer to:")
            st.markdown(
            """
            <p style="font-size: 25px;">
            This project is part of the Rakuten France Multimodal 
            Product Data Classification challenge, the data and 
            their description are available at: 
            <a href="https://challengedata.ens.fr/challenges/35" target="_blank">https://challengedata.ens.fr/challenges/35</a>
            </p>

            <p style="font-size: 25px;">
            Text data: ~60 mb
            </p>

            <p style="font-size: 25px;">
            Image data: ~2.2 gb
            </p>

            <p style="font-size: 25px;">
            99k data with 27 classes.
            </p>
            """
            ,
            unsafe_allow_html=True
        )
    
    with image_column:
        st.image(img_Rakuten_challenge)
    

#END