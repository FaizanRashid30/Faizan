import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()


col1, col2, col3 = st.columns(3)
col2.image(Image.open('dp.png'))

st.header('Code Anime')

st.info('Code animation create video into animation')

icon_size = 20

st_button('youtube', 'https://www.tiktok.com/@code.animation?is_from_webapp=1&sender_device=pc', 'Tiktok', icon_size)

