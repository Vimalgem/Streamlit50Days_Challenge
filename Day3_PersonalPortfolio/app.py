import streamlit as st

# Set page configuration
st.set_page_config(page_title="About Me", page_icon="👤")

# Main Title
st.title("👤 About Me")

# Profile Image
st.image("my_photo.png", width=200, caption="Vimalraj Manoharan")

# Short Bio
st.markdown("""
Hi! I'm **Vimalraj Manoharan**, an aspiring AI and Data Solutions Creator.  
I’m passionate about:
- Building AI apps and tools
- Exploring GenAI and freelancing
- Trading and digital marketing
- Creative drawing skills

Currently on a mission to learn, earn, and grow in the world of tech 🚀
""")

# Contact and Links
st.subheader("🔗 Connect with Me")

st.markdown("""
- 📧 [Email Me](mailto:vimalgem288.com)  
- 💼 [LinkedIn](www.linkedin.com/in/vimalgem)  
- 🌐 [My Demo site](https://vimalgem.rf.gd/?i=1)  
- 🧠 [My Projects GitHub](https://github.com/Vimalgem)  
- 📺 [YouTube Channel](https://www.youtube.com/@Vimalgem)
""")

# Footer
st.write("---")
st.caption("Made with ❤️ using Streamlit")
