import streamlit as st
import time
from streamlit_extras.let_it_rain import rain

st.set_page_config(page_title="Happy Birthday Sir Ameen Alam 🎉", page_icon="🎂", layout="centered")

st.title("Happy Birthday Sir Ameen Alam🎉")

# Create three columns
col1, col2, col3 = st.columns([1, 2, 1])

# Use the middle column to center the image
with col2:
    st.image(
        "https://res.cloudinary.com/dd4xvwf8d/image/upload/v1748032715/pic_pq6vcn.jpg",
        width=300,
        caption="Sir Ameen Alam"
    )


st.markdown("""
### Warmest birthday wishes to you, Sir!

Your dedication, hard work, and guidance have shown us new paths every day.  
Everything we are learning is priceless because of your support.

You are not just a teacher to us, but a true inspiration.  
May every day bring you happiness, and may you continue to reach greater heights.

Working alongside you on new projects and technologies has been an exciting journey.  
With your mentorship, we can achieve even more.

Once again, happy birthday! We all pray for your health, happiness, and success.

**- Your students**
""")

if st.button("Celebrate 🎂"):
    with st.spinner("Loading birthday wishes..."):
        time.sleep(1)
    rain(emoji="🎉", font_size=50, falling_speed=3, animation_length=3)
    st.success("Happy Birthday Sir! 🎉🎊")

st.markdown("---")
st.markdown("Build with ❤️ by *Syed Shurem Ali*")
