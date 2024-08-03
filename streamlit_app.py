import streamlit as st
from st_functions import st_button, load_css
from st_social_media_links import SocialMediaIcons
from PIL import Image

load_css()


col1, col2, col3 = st.columns(3)
col2.image(Image.open('dp.png'))

st.header('Code Anime')

st.info('Code animation create video into animation')

icon_size = 20

st_button('turtle', 'https://www.tiktok.com/@code.animation?is_from_webapp=1&sender_device=pc', 'Tiktok', icon_size)
st_button('youtube', 'https://www.tiktok.com/@code.animation?is_from_webapp=1&sender_device=pc', 'Tiktok', icon_size)

social_media_links = [
    "https://www.facebook.com/ThisIsAnExampleLink",
    "https://www.youtube.com/ThisIsAnExampleLink",
    "https://www.instagram.com/ThisIsAnExampleLink",
    "https://www.github.com/jlnetosci/st-social-media-links",
]

social_media_icons = SocialMediaIcons(social_media_links)

social_media_icons.render()
